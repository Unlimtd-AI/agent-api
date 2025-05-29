from pydantic import Field
from config.base import AppBaseSettings

class WatiSettings(AppBaseSettings):
   MESSAGING_API_URL = Field(..., env="MESSAGING_API_URL")
   MESSAGE_LOG_TYPE_ID = Field(..., env="MESSAGE_LOG_TYPE_ID")
   