from pydantic import Field
from config.base import AppBaseSettings

class WatiSettings(AppBaseSettings):
   WALLETY_API_URL = Field(..., env="WALLETY_API_URL")
   MESSAGING_API_URL = Field(..., env="MESSAGING_API_URL")
   MESSAGE_LOG_TYPE_ID = Field(..., env="MESSAGE_LOG_TYPE_ID")
   