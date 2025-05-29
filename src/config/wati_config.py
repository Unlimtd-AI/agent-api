from pydantic import Field
from config.base import AppBaseSettings

class WatiSettings(AppBaseSettings):
   API_ENDPOINT = Field(..., env="MESSAGING_API_URL")