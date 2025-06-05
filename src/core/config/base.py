from os import getenv
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment only once
load_dotenv()

class AppBaseSettings(BaseSettings):
    """
    Common base for all settings. Automatically loads from .env
    """
    class Config:
        extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"
        
    def _get(self, key, default=None):
        # Uses pydantic's built-in environment loading
        return getenv(key, default)