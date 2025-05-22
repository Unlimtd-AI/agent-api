from textwrap import dedent
from typing import Optional

from constants import (
   WALLETY_TOOL_MODEL,
   WALLETY_KNOWLEDGE_URLS,
   WALLETY_EMBEDDING_MODEL,
   WALLETY_HELPDESK_AGENT_ID,
   WALLETY_HELPDESK_AGENT_NAME,
   WALLETY_HELPDESK_SESSION_TABLE,
   WALLETY_HELPDESK_KNOWLEDGE_TABLE,
   WALLETY_HELPDESK_USER_MEMORY_TABLE,
)

from agno.models.ollama import Ollama
from agno.memory.v2.memory import Memory
from agno.knowledge.url import UrlKnowledge
from agno.agent import Agent, AgentKnowledge
from agno.embedder.ollama import OllamaEmbedder
from agno.vectordb.pgvector import PgVector, SearchType
from agno.memory.v2.db.postgres import PostgresMemoryDb
from agno.storage.agent.postgres import PostgresAgentStorage

from config.jinja_config import JinjaSettings
from config.llm_config import LlamaSettings
from db.session import db_url

# Initialize knowledge base
def get_agent_knowledge() -> AgentKnowledge:
   return UrlKnowledge(
      urls=WALLETY_KNOWLEDGE_URLS,    
      vector_db=PgVector(
         table_name=WALLETY_HELPDESK_KNOWLEDGE_TABLE,
         db_url=db_url,
         search_type=SearchType.hybrid,
         embedder=OllamaEmbedder(id=WALLETY_EMBEDDING_MODEL)
      ),
   )
   
def get_agent_storage() -> PostgresAgentStorage:
   return PostgresAgentStorage(
      # store sessions in the ai.sessions table
      table_name=WALLETY_HELPDESK_SESSION_TABLE,
      # db_url: Postgres database URL
      db_url=db_url,
   )
      
def get_agent_memory() -> Memory:
   return Memory(
      model=Ollama(id=LlamaSettings().default_model),
      db=PostgresMemoryDb(table_name=WALLETY_HELPDESK_USER_MEMORY_TABLE, db_url=db_url),
      delete_memories=False,
      clear_memories=False,
   )

def get_wallety_assist_agent(
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
) -> Agent:
   return Agent(
      name=WALLETY_HELPDESK_AGENT_NAME,
      agent_id=WALLETY_HELPDESK_AGENT_ID,
      user_id=user_id,
      session_id=session_id,
      model=Ollama(id=WALLETY_TOOL_MODEL),

      # Description of the agent
      description=dedent(JinjaSettings().render_template("wallety_assist_agent_template_description.jinja2")),
      # Instructions for the agent
      instructions=dedent(JinjaSettings().render_template("wallety_assist_agent_template_instructions.jinja2")),
      # This makes `current_user_id` available in the instructions
      add_state_in_messages=True,

      # *********************** KNOWLEDGE ***********************
      # Add the knowledge base to the agent
      knowledge=get_agent_knowledge(),
      # Give the agent a tool to search the knowledge base (this is True by default but set here for clarity)
      search_knowledge=True,

      # *********************** Storage ***********************
      # Storage chat history and session state in a Postgres table
      storage=get_agent_storage(),

      # *********************** HISTORY ***********************
      # Send the last 3 messages from the chat history
      add_history_to_messages=True,
      num_history_runs=3,
      # Add a tool to read the chat history if needed
      read_chat_history=True,

      # -***********************- MEMORY -***********************-
      # Enable agentic memory where the Agent can personalize responses to the user
      memory=get_agent_memory(),
      enable_agentic_memory=True,

      # *********************** Other settings ***********************
      # Format responses using markdown
      markdown=True,
      # Add the current date and time to the instructions
      add_datetime_to_instructions=True,
      # Show debug logs
      debug_mode=debug_mode,
   )