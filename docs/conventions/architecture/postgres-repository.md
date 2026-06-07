# PostgreSQL Repository Pattern

## Convention

Implement the repository port (defined in the domain layer) as a concrete adapter class in the `infra/` folder. The adapter receives an SQLAlchemy `Session` and maps between the domain entity and the ORM model.

### Responsibilities

- **Receives** domain entities from the use case layer.
- **Maps** domain entities to ORM models (not the other way around — this is a write-focused pattern).
- **Delegates** persistence to the SQLAlchemy session.
- **Does NOT** contain business logic — it is a pure data-mapping layer.

### File layout

```
src/
  usage_events/
    domain/
      usage_event.py               # Domain entity (dataclass)
      usage_event_repository.py    # Repository port (Protocol)
    infra/
      models.py                    # SQLAlchemy ORM model
      postgres_usage_event_repository.py  # Port implementation
```

### Structure

**ORM model** (`models.py`):

```python
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

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=lambda: uuid7(),
    )
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
```

**Repository adapter** (`postgres_usage_event_repository.py`):

```python
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
```

### Key rules

- The ORM model lives in `infra/models.py`, **not** in the domain layer. The domain entity is a plain dataclass with no SQLAlchemy dependency.
- The repository adapter maps **domain → ORM** on writes. For reads, map **ORM → domain**.
- Extra database-only fields (e.g., `created_at`, `updated_at`) are acceptable in the ORM model. They are not part of the domain entity.
- The adapter does NOT validate business rules — validation happens in the delivery layer (Pydantic) and the application layer (use case).

## Benefits

- **Domain purity** — domain entities have zero database dependencies. They are plain dataclasses.
- **Testability** — the repository port (Protocol) can be mocked or replaced with an in-memory implementation for unit tests.
- **Separation of concerns** — ORM model, domain entity, and repository adapter each have a single, clear responsibility.

## Real world examples

- `src/usage_events/infra/models.py` — `UsageEventModel` (ORM model with `Base`)
- `src/usage_events/infra/postgres_usage_event_repository.py` — `PostgresUsageEventRepository` (adapter implementation)
- `src/usage_events/infra/memory_usage_event_repository.py` — `MemoryUsageEventRepository` (in-memory adapter for dev/test)

## Related agreements

- `docs/conventions/architecture/architecture.md` — screaming architecture layer structure
- `docs/conventions/architecture/alembic-setup.md` — migrations for these ORM models
- `docs/conventions/architecture/uuid-v7.md` — UUID v7 generation for entity IDs
