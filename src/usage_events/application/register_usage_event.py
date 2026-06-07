"""Use case for registering a usage event."""

from typing import cast
from uuid import UUID

from usage_events.domain.usage_event import UsageEvent
from usage_events.domain.usage_event_repository import UsageEventRepository


class RegisterUsageEventUseCase:
    def __init__(self, repository: UsageEventRepository) -> None:
        self._repository = repository

    def execute(
        self,
        ipy_version: str,
        operating_system: str,
        distinct_id: str,
        command: str,
        python_version: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> UUID:
        """Register a usage event and return its ID."""
        event = UsageEvent(
            ipy_version=ipy_version,
            operating_system=operating_system,
            distinct_id=distinct_id,
            command=command,
            python_version=python_version,
            dependency_manager=dependency_manager,
            template=template,
            built_in_features=built_in_features,
        )
        self._repository.save(event)
        return cast(UUID, event.event_id)
