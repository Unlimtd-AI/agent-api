from textwrap import dedent
from typing import Optional

from agno.models.ollama import Ollama
from agno.memory.v2.memory import Memory
from agno.knowledge.url import UrlKnowledge
from agno.agent import Agent, AgentKnowledge
from agno.embedder.ollama import OllamaEmbedder
from agno.vectordb.pgvector import PgVector, SearchType
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.storage.agent.postgres import PostgresAgentStorage

from config.jinja_config import JinjaSettings
from db.session import db_url

# Initialize knowledge base
def get_agent_knowledge() -> AgentKnowledge:
   return UrlKnowledge(
      urls=[
         "https://r.jina.ai/https://wallety.cash",
         "https://r.jina.ai/https://wallety.cash/company/"
      ],    
      vector_db=PgVector(
         table_name="wallety_assist_knowledge",
         db_url=db_url,
         search_type=SearchType.hybrid,
         embedder=OllamaEmbedder(id="llama2:7b")
      ),
   )
   
def get_agent_storage() -> PostgresAgentStorage:
      return PostgresAgentStorage(
      # store sessions in the ai.sessions table
      table_name="wallety_assist_sessions",
      # db_url: Postgres database URL
      db_url=db_url,
   )

def get_wallety_assist_agent(
    model_id: str = "llama3.1:8b",
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
       return Agent(
        name="Wallety Assist Agent",
        agent_id="wallety_assist_agent",
        user_id=user_id,
        session_id=session_id,
        model=Ollama(id=model_id),
        # Description of the agent
        description=dedent(JinjaSettings().render_template("wallety_assist_agent_template_description.jinja2")),
        # Instructions for the agent
        instructions=dedent(JinjaSettings().render_template("wallety_assist_agent_template_instructions.jinja2")),
        # This makes `current_user_id` available in the instructions
        add_state_in_messages=True,
        # -*- Knowledge -*-
        # Add the knowledge base to the agent
        knowledge=get_agent_knowledge(),
        # Give the agent a tool to search the knowledge base (this is True by default but set here for clarity)
        search_knowledge=True,
        # -*- Storage -*-
        # Storage chat history and session state in a Postgres table
        storage=get_agent_storage(),
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
            db=PostgresMemoryDb(table_name="user_memories", db_url=db_url),
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