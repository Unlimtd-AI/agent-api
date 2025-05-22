# constants.py

from config.llm_config import LlamaSettings


WALLETY_KNOWLEDGE_URLS = [
    "https://r.jina.ai/https://wallety.cash",
    "https://r.jina.ai/https://wallety.cash/company/"
]

# OLLAMA MODELS
WALLETY_TOOL_MODEL=LlamaSettings().default_model
WALLETY_EMBEDDING_MODEL=LlamaSettings().embedding_model

# Helpdesk constants
WALLETY_HELPDESK_SESSION_TABLE = "wallety_helpdesk_sessions"
WALLETY_HELPDESK_KNOWLEDGE_TABLE = "wallety_helpdesk_knowledge"
WALLETY_HELPDESK_USER_MEMORY_TABLE = "wallety_helpdesk_user_memories"
WALLETY_HELPDESK_AGENT_ID = "wallety_helpdesk_agent"
WALLETY_HELPDESK_AGENT_NAME = "Wallety Helpdesk Agent"

# Transaction constants
WALLETY_TRANSACTION_SESSION_TABLE = "wallety_transaction_sessions"
WALLETY_TRANSACTION_KNOWLEDGE_TABLE = "wallety_transaction_knowledge"
WALLETY_TRANSACTION_USER_MEMORY_TABLE = "wallety_transaction_user_memories"
WALLETY_TRANSACTION_AGENT_ID = "wallety_transaction_agent"
WALLETY_TRANSACTION_AGENT_NAME = "Wallety Transaction Agent"