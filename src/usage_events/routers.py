from typing import Annotated

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette import status

from usage_events.session import get_db
from usage_events.usage_event_create_request import UsageEventCreateRequest
from usage_events.usage_event_register import UsageEventRegister
from usage_events.usage_event_repository import PostgresUsageEventRepository
from usage_events.uuid_generator import Uuid7Generator

usage_events_router = APIRouter(prefix="/api/v1/events", tags=["Usage Events"])


def _get_usage_event_register(session: Annotated[Session, Depends(get_db)]) -> UsageEventRegister:
    return UsageEventRegister(
        repository=PostgresUsageEventRepository(session=session),
        uuid_generator=Uuid7Generator(),
    )


@usage_events_router.post("/", status_code=status.HTTP_204_NO_CONTENT)
def register_event(
    payload: UsageEventCreateRequest,
    usage_event_register: Annotated[UsageEventRegister, Depends(_get_usage_event_register)],
) -> None:
    usage_event_register.execute(**payload.model_dump())
