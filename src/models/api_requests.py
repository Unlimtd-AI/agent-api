from typing import Optional
from config.llm_config import LlamaSettings

from pydantic import BaseModel, Field

class RunRequest(BaseModel):
    """Request model for an running an agent"""

    message: str
    stream: bool = True
    default_model: LlamaSettings = Field(default_factory=lambda: LlamaSettings().default_model)
    embedding_model: LlamaSettings = Field(default_factory=lambda: LlamaSettings().embedding_model)
    user_id: Optional[str] = None
    session_id: Optional[str] = None
