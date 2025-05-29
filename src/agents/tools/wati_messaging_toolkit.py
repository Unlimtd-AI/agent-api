from config.wati_config import WatiSettings
from agno.tools import Toolkit
import httpx

class WatiMessagingToolkit(Toolkit):
   API_URL = WatiSettings().MESSAGING_API_URL
   ID = WatiSettings().MESSAGE_LOG_TYPE_ID
   
   def __init__(self):
      super().__init__(name="wati_messaging_toolkit")
      
   def send_template(self, to_field: str, body: str) -> str :
      
      data = {
         "MessageLogTypeId": self.ID,
         "Subject": "Wati Service",
         "ToField": to_field,
         "Body": body
      }
      
      response = httpx.post(f"{self.API_URL}/Messaging/CreateOutboundMail", data=data)
      return response.json()
      
      
   