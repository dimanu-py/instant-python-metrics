from datetime import UTC, datetime

from sqlalchemy import JSON, UUID, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from common.persistence.orm_base import OrmBase
from usage_events.usage_event import UsageEvent


class UsageEventModel(OrmBase):
    __tablename__ = "usage_events"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(256), nullable=False)
    ipy_version: Mapped[str] = mapped_column(String(256), nullable=False)
    python_version: Mapped[str] = mapped_column(String(256), nullable=False)
    operating_system: Mapped[str] = mapped_column(String(256), nullable=False)
    command: Mapped[str] = mapped_column(String(256), nullable=False)
    dependency_manager: Mapped[str] = mapped_column(String(256), nullable=False)
    template: Mapped[str] = mapped_column(String(256), nullable=False)
    built_in_features: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(UTC))

    @classmethod
    def from_domain(cls, event: UsageEvent) -> "UsageEventModel":
        return cls(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            python_version=event["python_version"],
            operating_system=event["operating_system"],
            command=event["command"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    def to_domain(self) -> UsageEvent:
        return UsageEvent(
            id=self.id,
            user_id=self.user_id,
            ipy_version=self.ipy_version,
            python_version=self.python_version,
            operating_system=self.operating_system,
            command=self.command,
            dependency_manager=self.dependency_manager,
            template=self.template,
            built_in_features=self.built_in_features,
        )
