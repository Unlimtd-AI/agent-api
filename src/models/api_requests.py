from typing import Optional

from pydantic import BaseModel, Field

from config.llm_config import LlamaSettings


class RunRequest(BaseModel):
    """Request model for an running an agent"""

    message: str
    stream: bool = True
    default_model: str = Field(default_factory=lambda: LlamaSettings().default_model)
    embedding_model: str = Field(default_factory=lambda: LlamaSettings().embedding_model)
    user_id: Optional[str] = None
    session_id: Optional[str] = None
