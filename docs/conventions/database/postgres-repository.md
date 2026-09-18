# PostgreSQL Repository Pattern

## Convention

Implement the repository port (defined as an ABC in the feature package) as a concrete adapter class. The adapter receives an SQLAlchemy `Session` and maps between the domain entity (TypedDict) and the ORM model.

### Responsibilities

- **Receives** domain entities from the use case layer.
- **Maps** domain entities to ORM models (not the other way around — this is a write-focused pattern).
- **Delegates** persistence to the SQLAlchemy session.
- **Does NOT** contain business logic — it is a pure data-mapping layer.

### File layout

```
src/
  usage_events/
    usage_event.py               # Domain entity (TypedDict)
    usage_event_repository.py    # Repository ABC + Postgres implementation
    database.py                  # SQLAlchemy ORM model
```

### Structure

**ORM model** (`database.py`):

```python
from datetime import UTC, datetime

from sqlalchemy import JSON, Column, DateTime, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UsageEventTable(Base):
    __tablename__ = "usage_events"

    id = Column(String(36), primary_key=True)
    user_id = Column(String(256), nullable=False)
    ipy_version = Column(String(256), nullable=False)
    python_version = Column(String(256), nullable=False)
    operating_system = Column(String(256), nullable=False)
    command = Column(String(256), nullable=False)
    dependency_manager = Column(String(256), nullable=False)
    template = Column(String(256), nullable=False)
    built_in_features = Column(JSON, nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
```

**Repository adapter** (`usage_event_repository.py`):

```python
from abc import ABC, abstractmethod
from typing import override

from sqlalchemy.orm import Session

from usage_events.usage_event_model import UsageEventModel
from usage_events.usage_event import UsageEvent


class UsageEventRepository(ABC):
    @abstractmethod
    def save(self, event: UsageEvent) -> None:
        raise NotImplementedError


class PostgresUsageEventRepository(UsageEventRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    @override
    def save(self, event: UsageEvent) -> None:
        table_row = self._to_table(event)
        self._session.add(table_row)
        self._session.commit()

    @staticmethod
    def _to_table(event: UsageEvent) -> UsageEventModel:
        return UsageEventModel(
            id=event["id"],
            user_id=event["user_id"],
            ipy_version=event["ipy_version"],
            operating_system=event["operating_system"],
            distinct_id=event["distinct_id"],
            command=event["command"],
            python_version=event["python_version"],
            dependency_manager=event["dependency_manager"],
            template=event["template"],
            built_in_features=event["built_in_features"],
        )

    @staticmethod
    def _from_table(row: UsageEventModel) -> UsageEvent:
        return UsageEvent(
            id=row.id,
            user_id=row.user_id,
            ipy_version=row.ipy_version,
            # ... other fields
        )
```

### Key rules

- The ORM model lives in `database.py`, **not** in the domain entity file. The domain entity is a plain TypedDict with no SQLAlchemy dependency.
- The repository adapter maps **domain → ORM** on writes. For reads, map **ORM → domain**.
- Extra database-only fields (e.g., `created_at`, `updated_at`) are acceptable in the ORM model. They are not part of the domain entity.
- The adapter does NOT validate business rules — validation happens in the delivery layer (Pydantic) and the application layer (use case).
- Session is injected via constructor, not created inside the repository.

## Benefits

- **Domain purity** — domain entities have zero database dependencies. They are plain TypedDicts.
- **Testability** — the repository ABC can be mocked or replaced with an in-memory implementation for unit tests.
- **Separation of concerns** — ORM model, domain entity, and repository adapter each have a single, clear responsibility.

## Real world examples

- `src/usage_events/database.py` — `UsageEventTable` (ORM model with `Base`)
- `src/usage_events/usage_event_repository.py` — `PostgresUsageEventRepository` (adapter implementation)
- `test/usage_events/in_memory_usage_event_repository.py` — `InMemoryUsageEventRepository` (test double)

## Related agreements

- `docs/conventions/architecture/architecture.md` — flat feature structure
- `docs/conventions/database/data-mapper.md` — ORM model and data mapping pattern
- `docs/conventions/database/alembic-setup.md` — migrations for these ORM models
- `docs/conventions/architecture/uuid-v7.md` — UUID v7 generation for entity IDs
