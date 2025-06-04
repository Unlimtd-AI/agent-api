from typing import Optional

from pydantic import BaseModel, Field

from config.llm_config import LlamaSettings


class RunRequest(BaseModel):
    """Request model for an running an agent"""

    message: str
    stream: bool = True
    user_id: Optional[str] = None
    session_id: Optional[str] = None
