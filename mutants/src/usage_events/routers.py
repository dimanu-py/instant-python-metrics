from typing import Annotated

from fastapi import Depends
from fastapi.routing import APIRouter
from pydantic import BaseModel, BeforeValidator, ConfigDict, Field
from sqlalchemy.orm import Session
from starlette import status

from usage_events.session import get_db
from usage_events.usage_event_register import UsageEventRegister
from usage_events.usage_event_repository import PostgresUsageEventRepository
from usage_events.uuid_generator import Uuid7Generator
from usage_events.usage_event_create_request import validate_uuid, validate_relaxed_semver, validate_strict_semver, non_empty_feature

usage_events_router = APIRouter(prefix="/api/v1/events", tags=["Usage Events"])


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class UsageEventCreateRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")

    ipy_version: Annotated[str, BeforeValidator(validate_strict_semver)] = Field(min_length=1, max_length=256)
    python_version: Annotated[str, BeforeValidator(validate_relaxed_semver)] = Field(min_length=1, max_length=256)
    operating_system: str = Field(min_length=1, max_length=256)
    user_id: Annotated[str, BeforeValidator(validate_uuid)] = Field(min_length=1, max_length=256)
    command: str = Field(min_length=1, max_length=256)
    dependency_manager: str = Field(min_length=1, max_length=256)
    template: str = Field(min_length=1, max_length=256)
    built_in_features: list[Annotated[str, BeforeValidator(non_empty_feature)]] = Field(min_length=0)
mutants_x__get_usage_event_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__get_usage_event_register__mutmut)
def _get_usage_event_register(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=PostgresUsageEventRepository(session=session),
        uuid_generator=Uuid7Generator(),
    )


def x__get_usage_event_register__mutmut_orig(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=PostgresUsageEventRepository(session=session),
        uuid_generator=Uuid7Generator(),
    )


def x__get_usage_event_register__mutmut_1(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=None,
        uuid_generator=Uuid7Generator(),
    )


def x__get_usage_event_register__mutmut_2(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=PostgresUsageEventRepository(session=session),
        uuid_generator=None,
    )


def x__get_usage_event_register__mutmut_3(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        uuid_generator=Uuid7Generator(),
    )


def x__get_usage_event_register__mutmut_4(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=PostgresUsageEventRepository(session=session),
        )


def x__get_usage_event_register__mutmut_5(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=PostgresUsageEventRepository(session=None),
        uuid_generator=Uuid7Generator(),
    )

mutants_x__get_usage_event_register__mutmut['_mutmut_orig'] = x__get_usage_event_register__mutmut_orig # type: ignore # mutmut generated
mutants_x__get_usage_event_register__mutmut['x__get_usage_event_register__mutmut_1'] = x__get_usage_event_register__mutmut_1 # type: ignore # mutmut generated
mutants_x__get_usage_event_register__mutmut['x__get_usage_event_register__mutmut_2'] = x__get_usage_event_register__mutmut_2 # type: ignore # mutmut generated
mutants_x__get_usage_event_register__mutmut['x__get_usage_event_register__mutmut_3'] = x__get_usage_event_register__mutmut_3 # type: ignore # mutmut generated
mutants_x__get_usage_event_register__mutmut['x__get_usage_event_register__mutmut_4'] = x__get_usage_event_register__mutmut_4 # type: ignore # mutmut generated
mutants_x__get_usage_event_register__mutmut['x__get_usage_event_register__mutmut_5'] = x__get_usage_event_register__mutmut_5 # type: ignore # mutmut generated


@usage_events_router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def register_event(
    payload: UsageEventCreateRequest,
    usage_event_register: Annotated[UsageEventRegister, Depends(_get_usage_event_register)],
) -> None:
    usage_event_register.execute(**payload.model_dump())
