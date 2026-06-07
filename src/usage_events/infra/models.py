"""SQLAlchemy ORM model for usage events."""

import uuid
from datetime import UTC, datetime

from sqlalchemy import JSON, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid_extensions import uuid7


class Base(DeclarativeBase):
    pass


class UsageEventModel(Base):
    __tablename__ = "usage_events"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid7())
    ipy_version: Mapped[str] = mapped_column(String(255))
    operating_system: Mapped[str] = mapped_column(String(255))
    distinct_id: Mapped[str] = mapped_column(String(255))
    command: Mapped[str] = mapped_column(String(255))
    python_version: Mapped[str] = mapped_column(String(255))
    dependency_manager: Mapped[str] = mapped_column(String(255))
    template: Mapped[str] = mapped_column(String(255))
    built_in_features: Mapped[list[str]] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )
