from textwrap import dedent
from typing import Optional

from agents.wallety_team.constants import WalletyAgentConstants
from agno.agent import Agent
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.ollama import Ollama
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from core.config.jinja_config import JinjaSettings

class WalletyWebAgentService(WalletyAgentConstants):
    def __init__(self):
        super().__init__()
        
    def get_web_agent(
        self,
        model_id: str = "llama3.1:8b",
        user_id: Optional[str] = None,
        session_id: Optional[str] = None,
        debug_mode: bool = True,
    ) -> Agent:
        return Agent(
            name="Web Search Agent",
            agent_id="web_search_agent",
            user_id=user_id,
            session_id=session_id,
            model=Ollama(id=model_id),
            # Tools available to the agent
            tools=[DuckDuckGoTools()],
            # Description of the agent
            description=dedent(JinjaSettings().render_template("web_agent_template_description.jinja2")),
            # Instructions for the agent
            instructions=dedent(JinjaSettings().render_template("web_agent_template_instructions.jinja2")),
            # This makes `current_user_id` available in the instructions
            add_state_in_messages=True,
            # -*- Storage -*-
            # Storage chat history and session state in a Postgres table
            storage=PostgresAgentStorage(table_name="web_search_agent_sessions",  db_url=self.DB_URL,),
            # -*- History -*-
            # Send the last 3 messages from the chat history
            add_history_to_messages=True,
            num_history_runs=3,
            # Add a tool to read the chat history if needed
            read_chat_history=True,
            # -*- Memory -*-
            # Enable agentic memory where the Agent can personalize responses to the user
            memory=Memory(
                model=Ollama(id=model_id),
                db=PostgresMemoryDb(table_name="user_memories", db_url=self.DB_URL,),
                delete_memories=False,
                clear_memories=False,
            ),
            enable_agentic_memory=True,
            # -*- Other settings -*-
            # Format responses using markdown
            markdown=True,
            # Add the current date and time to the instructions
            add_datetime_to_instructions=True,
            # Show debug logs
            debug_mode=debug_mode,
        )
