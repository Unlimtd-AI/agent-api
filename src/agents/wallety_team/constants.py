from core.config.jinja_config import JinjaSettings
from core.config.llm_config import LlamaSettings


class WalletyAgentConstants:
    def __init__(self):
        jinja = JinjaSettings()
        llama = LlamaSettings()

        # Knowledge URLs
        self.KNOWLEDGE_URLS = [
            "https://r.jina.ai/https://wallety.cash",
            "https://r.jina.ai/https://wallety.cash/company/",
        ]

        # LLM Models
        self.TOOL_MODEL = llama.default_model
        self.EMBEDDING_MODEL = llama.embedding_model
        self.OLLAMA_HOST = "http://ollama-server:11434"

        # Helpdesk Constants
        self.HELPDESK_SESSION_TABLE = "wallety_helpdesk_sessions"
        self.HELPDESK_KNOWLEDGE_TABLE = "wallety_helpdesk_knowledge"
        self.HELPDESK_USER_MEMORY_TABLE = "wallety_helpdesk_user_memories"
        self.HELPDESK_AGENT_ID = "wallety_helpdesk_agent"
        self.HELPDESK_AGENT_NAME = "Wallety Helpdesk Agent"

        self.HELPDESK_DESCRIPTION_TEMPLATE = jinja.render_template("wallety_helpdesk_agent_template_description.jinja2")
        self.HELPDESK_INSTRUCTION_TEMPLATE = jinja.render_template(
            "wallety_helpdesk_agent_template_instructions.jinja2"
        )

        # Transaction Constants
        self.TRANSACTION_SESSION_TABLE = "wallety_transaction_sessions"
        self.TRANSACTION_KNOWLEDGE_TABLE = "wallety_transaction_knowledge"
        self.TRANSACTION_USER_MEMORY_TABLE = "wallety_transaction_user_memories"
        self.TRANSACTION_AGENT_ID = "wallety_transaction_agent"
        self.TRANSACTION_AGENT_NAME = "Wallety Transaction Agent"
