# Data Mapper Pattern (ORM ↔ Domain)

## Convention

Separate the domain entity (a plain `TypedDict` or dataclass) from the SQLAlchemy ORM model (a `DeclarativeBase` subclass). The repository adapter contains explicit `_to_table()` / `_from_table()` conversion methods that map between the two representations.

### File layout

```
src/usage_events/
  usage_event.py        # Domain entity (TypedDict) — no ORM dependency
  usage_event_repository.py  # Repository ABC + Postgres implementation with _to_table/_from_table
  database.py           # SQLAlchemy ORM model (UsageEventTable)
```

### Domain entity as TypedDict

Domain entities are lightweight `TypedDict` definitions with no framework dependencies:

```python
# src/usage_events/usage_event.py
from typing import TypedDict


class UsageEvent(TypedDict):
    id: str
    user_id: str
    ipy_version: str
    python_version: str
    operating_system: str
    command: str
    dependency_manager: str
    template: str
    built_in_features: list[str]
```

The domain entity contains only business-relevant fields. Database-only fields (e.g., `created_at`, `updated_at`) belong exclusively on the ORM model.

### ORM model

The ORM model inherits from a `DeclarativeBase` subclass and defines table columns:

```python
# src/usage_events/usage_event_model.py
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

Key details:

- `created_at` uses a **callable default** (`lambda: datetime.now(UTC)`), evaluated at insert time, not at class definition time.
- `Built_in_features` uses `JSON` column type for list storage.
- The `Base` class is defined in `database.py` alongside the models for discoverability.

### Repository conversion methods

The repository adapter maps between domain and ORM representations:

```python
# src/usage_events/usage_event_repository.py
class PostgresUsageEventRepository(UsageEventRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, event: UsageEvent) -> None:
        table_row = self._to_table(event)
        self._session.add(table_row)
        self._session.commit()

    @staticmethod
    def _to_table(event: UsageEvent) -> UsageEventTable:
        return UsageEventTable(
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

    @staticmethod
    def _from_table(row: UsageEventTable) -> UsageEvent:
        return UsageEvent(
            id=row.id,
            user_id=row.user_id,
            # ... other fields
        )
```

### Key rules

- **Domain entity has zero SQLAlchemy dependency** — it is a plain `TypedDict` with no ORM imports.
- **ORM model has zero business logic** — it only defines columns and table metadata.
- **Conversion methods are static** — they do not depend on instance state (session, connection).
- **`_to_table()` maps domain → ORM** (for writes); **`_from_table()` maps ORM → domain** (for reads).
- **Database-only fields** (e.g., `created_at`) are added in the ORM model only. They are never part of the domain entity.
- **Session is injected** via the constructor, not created inside the repository.

## Benefits

- **Domain purity** — domain entities have zero database dependencies. They are plain `TypedDict` objects.
- **Testability** — repositories can be mocked or replaced with in-memory implementations for unit tests.
- **Clear boundary** — the `_to_table()` / `_from_table()` methods make the mapping explicit and visible.
- **ORM flexibility** — changing ORM libraries or migrating to a different database technology only affects `database.py` and the repository adapter.

## Examples

### Good: TypedDict domain entity

```python
class UsageEvent(TypedDict):
    id: str
    user_id: str
    ipy_version: str
    built_in_features: list[str]
```

### Bad: Domain entity inheriting from ORM Base

```python
class UsageEvent(Base):
    # Domain now has an SQLAlchemy dependency
    # Cannot instantiate without a session/engine
    ...
```

The domain entity should not be an ORM model. This couples business logic to the persistence framework.

### Good: Callable default for created_at

```python
created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
```

### Bad: Eager default for created_at

```python
created_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
```

This evaluates `datetime.now(UTC)` once at class definition time, so all rows share the same timestamp.

## Real world examples

- `src/usage_events/usage_event.py` — `UsageEvent` TypedDict domain entity
- `src/usage_events/database.py` — `UsageEventTable` ORM model
- `src/usage_events/usage_event_repository.py` — `PostgresUsageEventRepository` with `_to_table()` / `_from_table()`

## Related agreements

- `docs/conventions/database/postgres-repository.md` — PostgreSQL repository adapter pattern
- `docs/conventions/database/alembic-setup.md` — Alembic configuration for ORM models
- `docs/conventions/architecture/architecture.md` — flat feature structure
- `docs/conventions/convention_guidelines.md` — document structure standard
