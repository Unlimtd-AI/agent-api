from config.wati_config import WatiSettings
from agno.tools import Toolkit
import httpx

class WatiMessagingToolkit(Toolkit):
   URL = WatiSettings().API_ENDPOINT
   
   def __init__(self):
      super().__init__(name="wati_messaging_toolkit")
      
      
   def send_template(self, to_field: str, body: str) -> str :
      
      "MessageLogTypeId": "76496eb7-bb57-4aef-9f92-6a6bf5a07a37",
      "Subject": "Reset Password",
      "ToField": "njmcloud@gmail.com",
      "Body": "This is a Test",
      "FromName": "Wallety"
      
      httpx.post(f"{API_ENDPOINT}/Messaging/CreateOutboundMail", data=data)
      
      
   