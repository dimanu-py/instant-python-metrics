import os
from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from usage_events.usage_event_model import OrmBase

DEFAULT_DATABASE_URL = "postgresql://ipm:ipm@localhost:5432/instant_python_metrics"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSessionManagerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSessionManagerǁcreate_tables__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSessionManagerǁclean_tables__mutmut: MutantDict = {}  # type: ignore


class SessionManager:
    @_mutmut_mutated(mutants_xǁSessionManagerǁ__init____mutmut)
    def __init__(self, database_url: str) -> None:
        self._engine = create_engine(database_url)
        self._session_factory = sessionmaker(bind=self._engine)
    def xǁSessionManagerǁ__init____mutmut_orig(self, database_url: str) -> None:
        self._engine = create_engine(database_url)
        self._session_factory = sessionmaker(bind=self._engine)
    def xǁSessionManagerǁ__init____mutmut_1(self, database_url: str) -> None:
        self._engine = None
        self._session_factory = sessionmaker(bind=self._engine)
    def xǁSessionManagerǁ__init____mutmut_2(self, database_url: str) -> None:
        self._engine = create_engine(None)
        self._session_factory = sessionmaker(bind=self._engine)
    def xǁSessionManagerǁ__init____mutmut_3(self, database_url: str) -> None:
        self._engine = create_engine(database_url)
        self._session_factory = None
    def xǁSessionManagerǁ__init____mutmut_4(self, database_url: str) -> None:
        self._engine = create_engine(database_url)
        self._session_factory = sessionmaker(bind=None)

    @_mutmut_mutated(mutants_xǁSessionManagerǁcreate_tables__mutmut)
    def create_tables(self) -> None:
        OrmBase.metadata.create_all(bind=self._engine)

    def xǁSessionManagerǁcreate_tables__mutmut_orig(self) -> None:
        OrmBase.metadata.create_all(bind=self._engine)

    def xǁSessionManagerǁcreate_tables__mutmut_1(self) -> None:
        OrmBase.metadata.create_all(bind=None)

    @_mutmut_mutated(mutants_xǁSessionManagerǁclean_tables__mutmut)
    def clean_tables(self) -> None:
        OrmBase.metadata.drop_all(bind=self._engine)
        OrmBase.metadata.create_all(bind=self._engine)

    def xǁSessionManagerǁclean_tables__mutmut_orig(self) -> None:
        OrmBase.metadata.drop_all(bind=self._engine)
        OrmBase.metadata.create_all(bind=self._engine)

    def xǁSessionManagerǁclean_tables__mutmut_1(self) -> None:
        OrmBase.metadata.drop_all(bind=None)
        OrmBase.metadata.create_all(bind=self._engine)

    def xǁSessionManagerǁclean_tables__mutmut_2(self) -> None:
        OrmBase.metadata.drop_all(bind=self._engine)
        OrmBase.metadata.create_all(bind=None)

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

mutants_xǁSessionManagerǁ__init____mutmut['_mutmut_orig'] = SessionManager.xǁSessionManagerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSessionManagerǁ__init____mutmut['xǁSessionManagerǁ__init____mutmut_1'] = SessionManager.xǁSessionManagerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSessionManagerǁ__init____mutmut['xǁSessionManagerǁ__init____mutmut_2'] = SessionManager.xǁSessionManagerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSessionManagerǁ__init____mutmut['xǁSessionManagerǁ__init____mutmut_3'] = SessionManager.xǁSessionManagerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁSessionManagerǁ__init____mutmut['xǁSessionManagerǁ__init____mutmut_4'] = SessionManager.xǁSessionManagerǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁSessionManagerǁcreate_tables__mutmut['_mutmut_orig'] = SessionManager.xǁSessionManagerǁcreate_tables__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSessionManagerǁcreate_tables__mutmut['xǁSessionManagerǁcreate_tables__mutmut_1'] = SessionManager.xǁSessionManagerǁcreate_tables__mutmut_1 # type: ignore # mutmut generated

mutants_xǁSessionManagerǁclean_tables__mutmut['_mutmut_orig'] = SessionManager.xǁSessionManagerǁclean_tables__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSessionManagerǁclean_tables__mutmut['xǁSessionManagerǁclean_tables__mutmut_1'] = SessionManager.xǁSessionManagerǁclean_tables__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSessionManagerǁclean_tables__mutmut['xǁSessionManagerǁclean_tables__mutmut_2'] = SessionManager.xǁSessionManagerǁclean_tables__mutmut_2 # type: ignore # mutmut generated


_session_manager = SessionManager(os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL))
mutants_x_reconfigure__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_reconfigure__mutmut)
def reconfigure(database_url: str) -> None:
    global _session_manager
    _session_manager = SessionManager(database_url)


def x_reconfigure__mutmut_orig(database_url: str) -> None:
    global _session_manager
    _session_manager = SessionManager(database_url)


def x_reconfigure__mutmut_1(database_url: str) -> None:
    global _session_manager
    _session_manager = None


def x_reconfigure__mutmut_2(database_url: str) -> None:
    global _session_manager
    _session_manager = SessionManager(None)

mutants_x_reconfigure__mutmut['_mutmut_orig'] = x_reconfigure__mutmut_orig # type: ignore # mutmut generated
mutants_x_reconfigure__mutmut['x_reconfigure__mutmut_1'] = x_reconfigure__mutmut_1 # type: ignore # mutmut generated
mutants_x_reconfigure__mutmut['x_reconfigure__mutmut_2'] = x_reconfigure__mutmut_2 # type: ignore # mutmut generated


def create_database() -> None:
    _session_manager.create_tables()


def get_db() -> Generator[Session]:
    yield from _session_manager.get_db()
