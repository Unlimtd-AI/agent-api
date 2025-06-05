from typing import Optional

from pydantic import BaseModel, Field

from config.llm_config import LlamaSettings


class RunRequest(BaseModel):
    """Request model for an running an agent"""

    # message: str
    # user_id: Optional[str] = None
    
    waId: str
    text: str
    stream: bool = True
    session_id: Optional[str] = None
    
