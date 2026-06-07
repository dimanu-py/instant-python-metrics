"""In-memory implementation of UsageEventRepository for development."""

from usage_events.domain.usage_event import UsageEvent


class MemoryUsageEventRepository:
    """In-memory repository for usage events (non-persistent)."""

    def __init__(self) -> None:
        self._events: list[UsageEvent] = []

    def save(self, event: UsageEvent) -> None:
        self._events.append(event)
