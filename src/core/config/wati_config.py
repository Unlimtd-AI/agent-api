from core.config.base import AppBaseSettings

class WatiSettings(AppBaseSettings):
   
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      
      self.WALLETY_API_URL=self._get("WALLETY_API_URL")
      self.MESSAGING_API_URL=self._get("MESSAGING_API_URL")
      self.MESSAGE_LOG_TYPE_ID=self._get("MESSAGE_LOG_TYPE_ID")
      self.WATI_API_URL=self._get("WATI_API_URL")
      self.WATI_API_KEY=self._get("WATI_API_KEY")
