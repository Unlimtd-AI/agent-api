from os import getenv
from config.base import AppBaseSettings

class DatabaseSettings(AppBaseSettings):
    db_url: str = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        driver = self._get("DB_DRIVER", "postgresql+psycopg")
        user = self._get("DB_USER")
        password = self._get("DB_PASS")
        host = self._get("DB_HOST")
        port = self._get("DB_PORT")
        database = self._get("DB_DATABASE")

        password_part = f":{password}" if password else ""
        self.db_url = f"{driver}://{user}{password_part}@{host}:{port}/{database}"

    def _get(self, key, default=None):
        # Uses pydantic's built-in environment loading
        return getenv(key, default)

    def __str__(self):
        return self.db_url