from os import getenv
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class LLMProviderSettings(BaseSettings):
   """Base settings for LLM providers."""
   
   temperature: float = 0.0
   max_tokens: Optional[int] = None
   max_retries: int = 3
   
class OpenAISettings(LLMProviderSettings):
   """Settings for OpenAI."""
   
   api_key: str = getenv("OPENAI_API_KEY")
   default_model: str = "gpt-40"
   embedding_model: str = "text-embedding-3-small"
   
class AnthropicSettings(LLMProviderSettings):
   """Settings for Anthropic."""
   
   api_key: str = getenv("ANTHROPIC_API_KEY")
   default_model: str = "claude-3-5-sonnet-20240620"
   max_tokens: int = 1024
   
class LlamaSettings(LLMProviderSettings):
   """Settings fro Llama."""
   
   api_key: str = getenv("AGNO_API_KEY")
   chat_model: str = "deepseek-r1:8b"
   default_model: str = "llama3.1:70b"
   embedding_model: str = "llama2:70b"