from config.wati_config import WatiSettings
from agno.tools import Toolkit
import httpx

class WatiMessagingToolkit(Toolkit):
   M_API_URL = WatiSettings().MESSAGING_API_URL
   M_ID = WatiSettings().MESSAGE_LOG_TYPE_ID
   W_API_URL = WatiSettings().WALLETY_API_URL

   def __init__(self):
      super().__init__(name="wati_messaging_toolkit")
      
   # def send_template(self, to_field: str, body: str) -> str :
      
   #    data = {
   #       "MessageLogTypeId": self.M_ID,
   #       "Subject": "Wati Service",
   #       "ToField": to_field,
   #       "Body": body
   #    }
      
   #    response = httpx.post(f"{self.M_API_URL}/Messaging/CreateOutboundMail", data=data)
   #    return response.json()
   
   def get_templates(self) -> str:
      response = httpx.get(f"{self.W_API_URL}/Wati/TemplateList")
      return response.json()
      
      
      
   