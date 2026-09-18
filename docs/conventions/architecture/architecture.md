# Code Structure

## Convention

The codebase follows a **flat feature structure** organized by feature. Each feature is a single Python package with all responsibilities at one level, making the project root scream what the application does (`usage_events/`, `invoices/`) rather than what framework it uses.

There is no layer sub-directory hierarchy. Instead, each file in the package has a clear functional role.

### Feature structure

```
src/
  usage_events/                     # ← feature name (plural noun, snake_case)
    __init__.py                     #   package marker
    routers.py                      #   FastAPI routes + Pydantic request models
    usage_event_register.py         #   use case (application orchestration)
    usage_event.py                  #   domain entity (TypedDict or simple class)
    usage_event_repository.py       #   repository ABC + Postgres implementation
    database.py                     #   SQLAlchemy ORM model
    uuid_generator.py               #   UUID generator ABC + implementation
    validators.py                   #   standalone validation functions
  common/                           # shared across features (added when proven)
    errors/
      base_error.py
      domain_error.py
    http/
      error_response.py
      success_response.py
```

### File responsibilities

| File                        | Responsibility                                                                                                                                                                           |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `routers.py`                | FastAPI routes, Pydantic request models, dependency wiring. Parses HTTP requests, validates input via Pydantic, delegates to the use case. Does NOT contain business logic.              |
| `<name>.py` (use case)      | Application orchestration. Single entry point (`execute`). Imports domain entities, applies business rules, calls port interfaces to persist or retrieve data. Named `<Object><Action>`. |
| `<name>.py` (domain entity) | TypedDict or simple class representing the core domain concept. No framework dependencies.                                                                                               |
| `validators.py`             | Standalone validation functions (e.g., semver check, UUID validation). Used by Pydantic's `BeforeValidator`.                                                                             |
| `database.py`               | SQLAlchemy ORM model(s). `DeclarativeBase` subclass + table definitions.                                                                                                                 |
| `uuid_generator.py`         | ABC port interface + concrete implementation.                                                                                                                                            |

### Dependency flow

```
routers.py ──→ usage_event_register.py ──→ usage_event_repository.py
                   │                               │
                   │                        database.py
                   │
            uuid_generator.py
```

- `routers.py` imports and instantiates the use case directly, passing any required adapters.
- Use cases import domain entities and ABC port interfaces. They receive concrete adapters via constructor injection.
- ABC port interfaces and their implementations may live in the same file (when small) or separate files (when complex).
- `database.py` is imported only by the repository implementation, not by the domain entity or use case.

### No shared folder until proven (YAGNI)

A `common/` module only exists when a pattern is used across three or more features. The first feature keeps everything local. Shared error types and HTTP response helpers are acceptable as they emerge from handling cross-cutting concerns.

### ABC explicit inheritance (port interfaces)

Port interfaces use `abc.ABC` with `@abstractmethod` to define the contract. Concrete implementations explicitly inherit from the ABC.

```python
# src/usage_events/usage_event_repository.py
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
            # ... other fields
        )
```

This explicit inheritance provides:

1. **IDE discoverability** — "go to implementations" works in all major IDEs.
2. **Runtime contract enforcement** — Python prevents instantiation of classes that don't implement all abstract methods.
3. **Clear intent** — the inheritance relationship is visible at a glance.

#### When NOT to create a port interface (YAGNI)

Not every external dependency needs a port interface. During the Register Usage Event feature, a `Clock` ABC was introduced early and later removed because:

- The `created_at` timestamp was set via the ORM model column default, not in domain logic.
- No test demanded control over time — the use case never read or manipulated timestamps.
- The abstraction added code without any tests exercising it.

**Rule of thumb**: Do not create a port interface until a test demands it. If the domain logic does not need to control a dependency (time, random numbers, etc.), the concrete call is fine. Abstract when you have a concrete test case that requires swapping the implementation.

### Naming conventions

| Concept | File naming | Class/Function naming |
|---------|-------------|----------------------|
| Routes | `routers.py` per feature | `usage_events_router` (APIRouter instance) |
| Use case | `<object>_<action>.py` | `UsageEventRegister` (`<Object><Action>`) |
| Domain entity | `<entity>.py` | `UsageEvent` (TypedDict) |
| Repository | `<entity>_repository.py` | `UsageEventRepository` (ABC), `PostgresUsageEventRepository` |
| Validation | `validators.py` | `validate_strict_semver`, `non_empty_feature` |
| ORM model | `database.py` | `UsageEventTable` |
| UUID generator | `uuid_generator.py` | `UuidGenerator` (ABC), `Uuid7Generator` |

## Benefits

- **Flat navigation** — every file for a feature is at one level; no drilling into sub-directories.
- **Clear file roles** — each filename tells you what it does without needing to understand the folder it's in.
- **Low ceremony** — no need to create layered sub-packages for every feature; start flat and refactor only when the file grows too large.
- **Screaming architecture** — the package list reads like a feature list, not a framework list.
- **Testable** — ABC port interfaces allow easy adapter swapping in tests.
- **YAGNI-compliant** — no shared abstractions until the codebase proves they are needed.

## Examples

### Good: Flat feature structure

```
src/usage_events/
  routers.py
  usage_event_register.py
  usage_event.py
  usage_event_repository.py
  database.py
  uuid_generator.py
  validators.py
```

### Bad: Layer-organized sub-directories

```
src/usage_events/delivery/router.py
src/usage_events/application/usage_event_register.py
src/usage_events/domain/usage_event.py
src/usage_events/infra/models.py
src/usage_events/infra/postgres_usage_event_repository.py
```

Sub-directory layers add navigation overhead without clear benefit when each feature has few files. Flat structure keeps all files visible at once.

### Good: Use case with constructor injection

```python
# src/usage_events/usage_event_register.py
class UsageEventRegister:
    def __init__(self, repository: UsageEventRepository, uuid_generator: UuidGenerator) -> None:
        self._repository = repository
        self._uuid_generator = uuid_generator

    def execute(
        self,
        ipy_version: str,
        python_version: str,
        operating_system: str,
        user_id: str,
        command: str,
        dependency_manager: str,
        template: str,
        built_in_features: list[str],
    ) -> None:
        usage_event = UsageEvent(
            id=self._uuid_generator.generate(),
            user_id=user_id,
            # ... other fields
        )
        self._repository.save(usage_event)
```

### Bad: Use case instantiating adapters directly

```python
class UsageEventRegister:
    def execute(self, ...) -> None:
        # Cannot test without a real database
        repo = PostgresUsageEventRepository(session)
        usage_event = UsageEvent(id=uuid7(), ...)
        repo.save(usage_event)
```

### Good: Port interface with explicit ABC inheritance

```python
class UsageEventRepository(ABC):
    @abstractmethod
    def save(self, event: UsageEvent) -> None: ...


class InMemoryUsageEventRepository(UsageEventRepository):
    def save(self, event: UsageEvent) -> None:
        self._events.append(event)
```

### Bad: Structural subtyping with Protocol

```python
class UsageEventRepository(Protocol):
    def save(self, event: UsageEvent) -> None: ...

# Does NOT inherit — structural subtyping hides the relationship
class PostgresUsageEventRepository:
    def save(self, event: UsageEvent) -> None: ...
```

Structural subtyping with `Protocol` hides the relationship between interface and implementation. "Go to implementations" in most IDEs does not work. Use `abc.ABC` with explicit inheritance instead.

## Real world examples

- `src/usage_events/` — flat feature structure with all files at one level
- `src/common/` — shared error types and HTTP response helpers

## Related agreements

- `docs/conventions/convention_guidelines.md` — document structure standard
- `docs/conventions/workflow/leader_workflow.md` — the development pipeline this code structure supports
- `docs/conventions/architecture/uuid-v7.md` — UUID v7 generation for entity identifiers
- `docs/conventions/database/postgres-repository.md` — PostgreSQL adapter pattern
- `docs/conventions/database/data-mapper.md` — ORM model and data mapping pattern
- `docs/conventions/database/alembic-setup.md` — Alembic configuration for ORM models
- `docs/conventions/testing/doublex-mocking.md` — mocking port interfaces in tests
- `docs/conventions/testing/tdd_outside_in.md` — outside-in TDD workflow
- `docs/conventions/testing/test-patterns.md` — test naming, object mothers, mocking patterns
