"""Repository port for usage events."""

from typing import Protocol

from usage_events.domain.usage_event import UsageEvent


class UsageEventRepository(Protocol):
    """Port interface for persisting usage events."""

    def save(self, event: UsageEvent) -> None: ...
