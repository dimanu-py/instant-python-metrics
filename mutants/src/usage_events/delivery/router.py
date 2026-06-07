"""Router for usage events endpoints."""

import os
import re
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from usage_events.application.register_usage_event import RegisterUsageEventUseCase
from usage_events.domain.usage_event_repository import UsageEventRepository
from usage_events.infra.memory_usage_event_repository import MemoryUsageEventRepository
from usage_events.infra.postgres_usage_event_repository import PostgresUsageEventRepository

router = APIRouter()

_SEMVER_PATTERN = re.compile(r"^\d+\.\d+(\.\d+)?([+-].+)?$")

_engine: Engine | None = None
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


def _get_engine() -> Engine | None:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__get_engine__mutmut_orig, x__get_engine__mutmut_mutants, args, kwargs, None)


def x__get_engine__mutmut_orig() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get("DATABASE_URL")
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def x__get_engine__mutmut_1() -> Engine | None:
    global _engine
    if _engine is not None:
        database_url = os.environ.get("DATABASE_URL")
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def x__get_engine__mutmut_2() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = None
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def x__get_engine__mutmut_3() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get(None)
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def x__get_engine__mutmut_4() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get("XXDATABASE_URLXX")
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def x__get_engine__mutmut_5() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get("database_url")
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def x__get_engine__mutmut_6() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get("DATABASE_URL")
        if database_url:
            _engine = None
    return _engine


def x__get_engine__mutmut_7() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get("DATABASE_URL")
        if database_url:
            _engine = create_engine(None)
    return _engine

x__get_engine__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__get_engine__mutmut_1': x__get_engine__mutmut_1, 
    'x__get_engine__mutmut_2': x__get_engine__mutmut_2, 
    'x__get_engine__mutmut_3': x__get_engine__mutmut_3, 
    'x__get_engine__mutmut_4': x__get_engine__mutmut_4, 
    'x__get_engine__mutmut_5': x__get_engine__mutmut_5, 
    'x__get_engine__mutmut_6': x__get_engine__mutmut_6, 
    'x__get_engine__mutmut_7': x__get_engine__mutmut_7
}
x__get_engine__mutmut_orig.__name__ = 'x__get_engine'


def _get_repository() -> UsageEventRepository:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x__get_repository__mutmut_orig, x__get_repository__mutmut_mutants, args, kwargs, None)


def x__get_repository__mutmut_orig() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = _get_engine()
    if engine is not None:
        session = Session(engine)
        return PostgresUsageEventRepository(session)
    return MemoryUsageEventRepository()


def x__get_repository__mutmut_1() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = None
    if engine is not None:
        session = Session(engine)
        return PostgresUsageEventRepository(session)
    return MemoryUsageEventRepository()


def x__get_repository__mutmut_2() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = _get_engine()
    if engine is None:
        session = Session(engine)
        return PostgresUsageEventRepository(session)
    return MemoryUsageEventRepository()


def x__get_repository__mutmut_3() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = _get_engine()
    if engine is not None:
        session = None
        return PostgresUsageEventRepository(session)
    return MemoryUsageEventRepository()


def x__get_repository__mutmut_4() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = _get_engine()
    if engine is not None:
        session = Session(None)
        return PostgresUsageEventRepository(session)
    return MemoryUsageEventRepository()


def x__get_repository__mutmut_5() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = _get_engine()
    if engine is not None:
        session = Session(engine)
        return PostgresUsageEventRepository(None)
    return MemoryUsageEventRepository()

x__get_repository__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x__get_repository__mutmut_1': x__get_repository__mutmut_1, 
    'x__get_repository__mutmut_2': x__get_repository__mutmut_2, 
    'x__get_repository__mutmut_3': x__get_repository__mutmut_3, 
    'x__get_repository__mutmut_4': x__get_repository__mutmut_4, 
    'x__get_repository__mutmut_5': x__get_repository__mutmut_5
}
x__get_repository__mutmut_orig.__name__ = 'x__get_repository'


class RegisterUsageEventRequest(BaseModel):
    ipy_version: str = Field(min_length=1, max_length=255)
    operating_system: str = Field(min_length=1, max_length=255)
    distinct_id: str = Field(min_length=1)
    command: str = Field(min_length=1, max_length=255)
    python_version: str = Field(min_length=1, max_length=255)
    dependency_manager: str = Field(min_length=1, max_length=255)
    template: str = Field(min_length=1, max_length=255)
    built_in_features: list[str] = Field(default_factory=list)

    @field_validator("distinct_id")
    @classmethod
    def validate_distinct_id(cls, value: str) -> str:
        """Validate that distinct_id is a valid UUID v4."""
        try:
            uuid_value = UUID(value)
        except ValueError:
            raise ValueError(f"Invalid UUID format: {value}") from None

        if uuid_value.version != 4:
            raise ValueError("distinct_id must be a UUID v4")

        return value

    @field_validator("ipy_version", "python_version")
    @classmethod
    def validate_semver(cls, value: str) -> str:
        """Validate that the field contains a valid semver string."""
        if not _SEMVER_PATTERN.match(value):
            raise ValueError(f"Invalid semver format: {value}")
        return value


@router.post("/api/v1/events", status_code=201)
def register_usage_event(
    request: RegisterUsageEventRequest,
    repository: UsageEventRepository = Depends(_get_repository),
) -> JSONResponse:
    use_case = RegisterUsageEventUseCase(repository)
    try:
        event_id = use_case.execute(
            ipy_version=request.ipy_version,
            operating_system=request.operating_system,
            distinct_id=request.distinct_id,
            command=request.command,
            python_version=request.python_version,
            dependency_manager=request.dependency_manager,
            template=request.template,
            built_in_features=request.built_in_features,
        )
    except Exception:
        return JSONResponse(
            status_code=503,
            content={"detail": "Service unavailable"},
        )
    return JSONResponse(
        content={"id": str(event_id)},
        status_code=201,
        headers={"Location": f"/api/v1/events/{event_id}"},
    )
