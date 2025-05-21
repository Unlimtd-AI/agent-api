from os import getenv

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class DatabaseSettings(BaseSettings):
    db_url: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        driver = getenv("DB_DRIVER", "postgresql+psycopg")
        user = getenv("DB_USER")
        password = getenv("DB_PASS")
        host = getenv("DB_HOST")
        port = getenv("DB_PORT")
        database = getenv("DB_DATABASE")

        password_part = f":{password}" if password else ""
        self.db_url = f"{driver}://{user}{password_part}@{host}:{port}/{database}"

    def __str__(self) -> str:
        return self.db_url
