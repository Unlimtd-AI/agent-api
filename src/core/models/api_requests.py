from typing import Optional
from pydantic import BaseModel, Field

class RunRequest(BaseModel):
    """Request model for an running an agent"""

    waId: str
    text: str
    stream: bool = True
    conversationId: Optional[str] = None
    
