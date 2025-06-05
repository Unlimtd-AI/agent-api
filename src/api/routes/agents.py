g import getLogger
from typing import List, Optional

from agno.agent import Agent, AgentKnowledge
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse

from agents.selector import AgentType, get_agent, get_available_agents
from core.models.api_requests import RunRequest
from helpers.agent_helper import AgentHelper
from services.wati_messaging import WatiMessagingService
from agents.wallety_team.wallety_helpdesk_agent import WalletyHelpdeskAgentService

logger = getLogger(__name__)

######################################################
## Routes for the Agent Interface
######################################################

agents_router = APIRouter(prefix="/agents", tags=["Agents"])


@agents_router.get("", response_model=List[str])
async def list_agents():
    """
    Returns a list of all available agent IDs.

    Returns:
        List[str]: List of agent identifiers
    """

    return get_available_agents()



@agents_router.post("/{agent_id}/runs", status_code=status.HTTP_200_OK)
async def create_agent_run(agent_id: AgentType, request: dict):
    """
    Sends a message to a specific agent and returns the response.

    Args:
        agent_id: The ID of the agent to interact with
        body: Request parameters including the message

    Returns:
        Either a streaming response or the complete agent response
    """
    
    body = RunRequest(**request)
    
    service = WatiMessagingService()
     
    if body.waId not in ["27724326766", "27658318700"]:
        return 

    try:
        agent: Agent = get_agent(
            agent_id=agent_id,
            user_id=body.waId,
            session_id=body.conversationId,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    if body.stream is None:
        body.stream = True

    if body.stream:
        
        # Buffer to collect the full message
        full_response_parts = []

        async def stream_with_buffer():
            async for part in AgentHelper().chat_response_streamer(agent, body.text):
                full_response_parts.append(part)
                yield part

        async def stream_and_send():
            # Wrap the generator to track completion
            async for part in stream_with_buffer():
                yield part
            # After the full stream is done, send the full message to WhatsApp
            full_message = "".join(full_response_parts)
            
            service.send_message(
                recipient_id=body.waId,
                message=full_message,
            )

        return StreamingResponse(stream_and_send(), media_type="text/event-stream")

@agents_router.post("/{agent_id}/knowledge/load", status_code=status.HTTP_200_OK)
async def load_agent_knowledge(agent_id: AgentType):
    """
    Loads the knowledge base for a specific agent.

    Args:
        agent_id: The ID of the agent to load knowledge for.

    Returns:
        A success message if the knowledge base is loaded.
    """
    agent_knowledge: Optional[AgentKnowledge] = None

    if agent_id == AgentType.WALLETY_TEAM:
        agent_knowledge = WalletyHelpdeskAgentService().get_agent_knowledge()
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Agent {agent_id} does not have a knowledge base.",
        )

    try:
        # await agent_knowledge.aload(upsert=True)
        agent_knowledge.load()
    except Exception as e:
        logger.error(f"Error loading knowledge base for {agent_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to load knowledge base for {agent_id}.",
        )

    return {"message": f"Knowledge base for {agent_id} loaded successfully."}
