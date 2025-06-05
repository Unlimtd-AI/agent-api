from typing import Optional
from core.config.base import AppBaseSettings
from pydantic import Field

class LLMProviderSettings(AppBaseSettings):
    """Base settings for LLM providers."""
    
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    max_retries: int = 3

class OpenAISettings(LLMProviderSettings):
    """Settings for OpenAI."""

    api_key: Optional[str] = Field(None, env="OPENAI_API_KEY")
    default_model: str = "gpt-40"
    embedding_model: str = "text-embedding-3-small"
    
    def __init__(self):
        self.api_key = self._get("OPENAI_API_KEY")


class AnthropicSettings(LLMProviderSettings):
    """Settings for Anthropic."""
    
    api_key: Optional[str] = Field(None, env="ANTHROPIC_API_KEY")
    default_model: str = "claude-3-5-sonnet-20240620"
    max_tokens: int = 1024
    
    def __init__(self):
        self.api_key = self._get("ANTHROPIC_API_KEY")

class LlamaSettings(LLMProviderSettings):
    """Settings for Llama."""
    
    api_key: Optional[str] = Field(None, env="AGNO_API_KEY")
    chat_model: str = "deepseek-r1:8b"
    default_model: str = "llama3.1:8b"
    embedding_model: str = "llama2:7b"

    def __init__(self):
        self.api_key = self._get("AGNO_API_KEY")