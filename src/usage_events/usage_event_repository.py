from abc import ABC, abstractmethod
from typing import override

from sqlalchemy.orm import Session

from usage_events.usage_event import UsageEvent
from usage_events.usage_event_model import UsageEventModel


class UsageEventRepository(ABC):
    @abstractmethod
    def save(self, event: UsageEvent) -> None:
        raise NotImplementedError


class PostgresUsageEventRepository(UsageEventRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    @override
    def save(self, event: UsageEvent) -> None:
        table_row = UsageEventModel.from_domain(event)
        self._session.add(table_row)
        self._session.commit()
