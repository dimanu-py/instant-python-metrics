import os
from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from usage_events.usage_event_model import OrmBase

DEFAULT_DATABASE_URL = "postgresql://ipm:ipm@localhost:5432/instant_python_metrics"


class SessionManager:
    def __init__(self, database_url: str) -> None:
        self._engine = create_engine(database_url)
        self._session_factory = sessionmaker(bind=self._engine)

    def create_tables(self) -> None:
        OrmBase.metadata.create_all(bind=self._engine)

    def clean_tables(self) -> None:
        OrmBase.metadata.drop_all(bind=self._engine)
        OrmBase.metadata.create_all(bind=self._engine)

    @contextmanager
    def session(self) -> Generator[Session]:
        session = self._session_factory()
        try:
            yield session
        finally:
            session.close()

    def get_db(self) -> Generator[Session]:
        with self.session() as session:
            yield session


_session_manager = SessionManager(os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL))


def reconfigure(database_url: str) -> None:
    global _session_manager
    _session_manager = SessionManager(database_url)


def create_database() -> None:
    _session_manager.create_tables()


def get_db() -> Generator[Session]:
    yield from _session_manager.get_db()
