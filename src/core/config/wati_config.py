from pydantic import Field
from config.base import AppBaseSettings

class WatiSettings(AppBaseSettings):
   WALLETY_API_URL: str = Field(..., env="WALLETY_API_URL")
   MESSAGING_API_URL: str = Field(..., env="MESSAGING_API_URL")
   MESSAGE_LOG_TYPE_ID: str = Field(..., env="MESSAGE_LOG_TYPE_ID")
   WATI_API_URL: str = Field(..., env="WATI_API_URL")
   WATI_API_KEY: str = Field(..., env="WATI_API_KEY")

   def __init__(self):
      self.WALLETY_API_URL = self._get("WALLETY_API_URL")
      self.MESSAGING_API_URL = self._get("MESSAGING_API_URL")
      self.MESSAGE_LOG_TYPE_ID = self._get("MESSAGE_LOG_TYPE_ID")
      self.WATI_API_URL = self._get("WATI_API_URL")
      self.WATI_API_KEY = self._get("WATI_API_KEY")
