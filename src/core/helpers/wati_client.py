import requests
from core.config.wati_config import WatiSettings

class WatiClient:
    """
    Handles direct communication with the Wati API.
    """
    
    def __init__(self):
        settings = WatiSettings()
        
        self.api_base_url = settings.WATI_API_URL
        self.headers = {
            'accept': '*/*',
            'Authorization': f'{settings.WATI_API_KEY}'
        }

    def send_message(self, recipient_id: str, message: str) -> bool:
        """
        Sends a session message to the specified recipient.

        :param recipient_id: Phone number or recipient ID.
        :param message: Text message to send.
        :return: True if message was successfully sent, False otherwise.
        """
        
        url = f"{self.api_base_url}/sendSessionMessage/{recipient_id}?messageText={message}"

        try:
            response = requests.post(url, headers=self.headers)
            response.raise_for_status()
            data = response.json()

            return data.get("ok") is True and data.get("result") == "success"

        except requests.RequestException as e:
            print(f"HTTP request failed: {e}")
        except ValueError:
            print("Failed to parse JSON response.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        return False
