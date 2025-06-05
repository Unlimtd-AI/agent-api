from core.helpers.wati_client import WatiClient


class WatiMessagingService:
    """
    Service for handling Wati messaging operations.
    """
    def __init__(self):
        self.wati_client = WatiClient()

    def send_message(self, recipient_id: str, message: str):
        """
        Send a message to a recipient using Wati API.
        
        :param recipient_id: The ID of the recipient.
        :param message: The message content to be sent.
        :return: Response from the Wati API.
        """
        return self.wati_client.send_message(recipient_id, message)