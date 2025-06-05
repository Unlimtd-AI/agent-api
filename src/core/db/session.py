from typing import Generator

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.config.db_config import DatabaseSettings

class DbSession:
    """
    Class to manage database sessions using SQLAlchemy.
    
    This class provides a method to create a session that can be used to interact with the database.
    It ensures that the session is properly closed after use.
    """

    def __init__(self):
        # Create SQLAlchemy Engine using a database URL
        self.settings = DatabaseSettings()
        self.db_url: str = self.settings.db_url
        self.db_engine: Engine = create_engine(self.db_url, pool_pre_ping=True)

        # Create a SessionLocal class
        self.SessionLocal: sessionmaker[Session] = sessionmaker(autocommit=False, autoflush=False, bind=self.db_engine)


    def get_db(self) -> Generator[Session, None, None]:
        """
        Dependency to get a database session.

        Yields:
            Session: An SQLAlchemy database session.
        """
        db: Session = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
