"""PostgreSQL implementation of UsageEventRepository."""

from sqlalchemy.orm import Session

from usage_events.domain.usage_event import UsageEvent
from usage_events.infra.models import UsageEventModel


class PostgresUsageEventRepository:
    """PostgreSQL-backed usage event repository."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, event: UsageEvent) -> None:
        model = UsageEventModel(
            id=event.event_id,
            ipy_version=event.ipy_version,
            operating_system=event.operating_system,
            distinct_id=event.distinct_id,
            command=event.command,
            python_version=event.python_version,
            dependency_manager=event.dependency_manager,
            template=event.template,
            built_in_features=event.built_in_features,
        )
        self._session.add(model)
        self._session.commit()
