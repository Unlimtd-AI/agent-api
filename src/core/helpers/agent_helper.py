from agno.agent import Agent
from typing import AsyncGenerator


class AgentHelper:
   
   async def chat_response_streamer(agent: Agent, message: str) -> AsyncGenerator:
      """
      Stream agent responses chunk by chunk.

      Args:
         agent: The agent instance to interact with
         message: User message to process

      Yields:
         Text chunks from the agent response
      """
      run_response = await agent.arun(message, stream=True)
      
      async for chunk in run_response:
         # chunk.content only contains the text response from the Agent.
         # For advanced use cases, we should yield the entire chunk
         # that contains the tool calls and intermediate steps.
         yield chunk.content

         # Wrap each chunk in a JSON object
         # data = {"content": chunk.content}
         # yield f"{json.dumps(data)}\n\n"  # Server-Sent Events format
