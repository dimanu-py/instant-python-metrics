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


def _get_engine() -> Engine | None:
    global _engine
    if _engine is None:
        database_url = os.environ.get("DATABASE_URL")
        if database_url:
            _engine = create_engine(database_url)
    return _engine


def _get_repository() -> UsageEventRepository:
    """Provide the usage event repository (overridable in tests)."""
    engine = _get_engine()
    if engine is not None:
        session = Session(engine)
        return PostgresUsageEventRepository(session)
    return MemoryUsageEventRepository()


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
