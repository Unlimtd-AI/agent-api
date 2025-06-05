from textwrap import dedent
from typing import Optional

from agno.agent import Agent, AgentKnowledge
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.ollama import Ollama
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.vectordb.pgvector import PgVector, SearchType
from ollama import Client as OllamaClient

from agents.wallety_team.constants import WalletyAgentConstants
from db.session import db_url


class WalletyHelpdeskAgentService(WalletyAgentConstants):
    def __init__(self):
        super().__init__()
        self.db_url = db_url

    # Initialize knowledge base
    def get_agent_knowledge(self) -> AgentKnowledge:
        return UrlKnowledge(
            urls=self.KNOWLEDGE_URLS,
            vector_db=PgVector(
                table_name=self.HELPDESK_KNOWLEDGE_TABLE,
                db_url=db_url,
                search_type=SearchType.hybrid,
                embedder=OllamaEmbedder(id=self.EMBEDDING_MODEL),
            ),
        )

    def get_agent_storage(self) -> PostgresAgentStorage:
        return PostgresAgentStorage(
            # store sessions in the ai.sessions table
            table_name=self.HELPDESK_SESSION_TABLE,
            # db_url: Postgres database URL
            db_url=db_url,
        )

    def get_agent_memory(self) -> Memory:
        return Memory(
            model=Ollama(id=self.TOOL_MODEL),
            db=PostgresMemoryDb(table_name=self.HELPDESK_USER_MEMORY_TABLE, db_url=db_url),
            delete_memories=False,
            clear_memories=False,
        )

    def get_wallety_helpdesk_agent(
        self,
        user_id: Optional[str] = None,
        session_id: Optional[str] = None,
        debug_mode: bool = True,
    ) -> Agent:
        return Agent(
            name=self.HELPDESK_AGENT_NAME,
            agent_id=self.HELPDESK_AGENT_ID,
            user_id=user_id,
            session_id=session_id,
            model=Ollama(id=self.TOOL_MODEL, host=self.OLLAMA_HOST),
            # Description of the agent
            description=dedent(self.HELPDESK_DESCRIPTION_TEMPLATE),
            # Instructions for the agent
            instructions=dedent(self.HELPDESK_INSTRUCTION_TEMPLATE),
            # This makes `current_user_id` available in the instructions
            add_state_in_messages=True,
            # *********************** KNOWLEDGE ***********************
            # Add the knowledge base to the agent
            knowledge=self.get_agent_knowledge(),
            # Give the agent a tool to search the knowledge base (this is True by default but set here for clarity)
            search_knowledge=True,
            # *********************** Storage ***********************
            # Storage chat history and session state in a Postgres table
            storage=self.get_agent_storage(),
            # *********************** HISTORY ***********************
            # Send the last 3 messages from the chat history
            add_history_to_messages=True,
            num_history_runs=3,
            # Add a tool to read the chat history if needed
            read_chat_history=True,
            # -***********************- MEMORY -***********************-
            # Enable agentic memory where the Agent can personalize responses to the user
            memory=self.get_agent_memory(),
            enable_agentic_memory=True,
            # *********************** Other settings ***********************
            # Format responses using markdown
            markdown=True,
            # Add the current date and time to the instructions
            add_datetime_to_instructions=True,
            # Show debug logs
            debug_mode=debug_mode,
        )
