from typing import override

from usage_events.usage_event import UsageEvent
from usage_events.usage_event_repository import UsageEventRepository


class InMemoryUsageEventRepository(UsageEventRepository):
    def __init__(self) -> None:
        self._events: list[UsageEvent] = []

    @override
    def save(self, event: UsageEvent) -> None:
        self._events.append(event)

    def __len__(self) -> int:
        return len(self._events)
