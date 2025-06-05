from enum import Enum
from typing import List, Optional

from agents.wallety_team.wallety_helpdesk_agent import WalletyHelpdeskAgentService
from agents.web_agent import WalletyWebAgentService

class AgentType(Enum):
    WEB_AGENT = "web_agent"
    WALLETY_HELPDESK_AGENT = "wallety_helpdesk_agent"
    WALLETY_TRANSACTION_AGENT = "wallety_transaction_agent"


def get_available_agents() -> List[str]:
    """Returns a list of all available agent IDs."""
    return [agent.value for agent in AgentType]


def get_agent(
    agent_id: Optional[AgentType] = None,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
):
    model_id = "llama3.1:70b"

    if agent_id == AgentType.WEB_AGENT:
        return WalletyWebAgentService().get_web_agent(model_id=model_id, user_id=user_id, session_id=session_id, debug_mode=debug_mode)
    elif agent_id == AgentType.WALLETY_HELPDESK_AGENT:
        return WalletyHelpdeskAgentService().get_wallety_helpdesk_agent(
            user_id=user_id, session_id=session_id, debug_mode=debug_mode
        )

    raise ValueError(f"Agent: {agent_id} not found")
