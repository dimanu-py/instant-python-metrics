# Outside-In TDD

## Convention

Every feature is built using Outside-In (London School) TDD. An acceptance test drives the outermost layer, 
and each inner layer is driven by the tests of the layer above it.

### Test pyramid

```
            ╱  acceptance  ╲            happy paths + critical errors — TestClient
           ╱  delivery unit ╲           all scenarios, use case mocked — doublex
          ╱  application unit ╲         business logic, ports mocked — doublex
         ╱  infra integration  ╲        real adapters (DB, IO) — pytest
```

| Type              | Layer tested          | Target                             | Mocking            | Tools                            |
|-------------------|-----------------------|------------------------------------|--------------------|----------------------------------|
| Acceptance        | delivery (full stack) | happy paths + critical errors      | real dependencies  | FastAPI TestClient, pytest       |
| Delivery unit     | delivery              | all scenarios (edge cases, errors) | use case mocked    | pytest, doublex or unittest.mock |
| Application unit  | application           | business rules, orchestration      | infra ports mocked | pytest, doublex or unittest.mock |
| Infra integration | infra                 | adapter correctness                | real DB/adapter    | pytest                           |

### TDD cycle per feature

```
1. Write acceptance test → Red
2. Implement delivery + stub application layer → Green
3. Write delivery unit tests (mock use case) → Red
4. Harden delivery code → Green
5. Write application unit tests → Red
6. Implement application layer (stub domain/infra) → Green
7. Continue for each inner layer until all are real
8. Write infra integration tests
```

Each step follows strict TDD: Red → Green → Refactor before moving to the next.

### Test markers

Tag every test file with a `@pytest.mark` marker indicating the layer under test:

| Marker               | Layer            | File location                           |
|----------------------|------------------|-----------------------------------------|
| `@pytest.mark.acceptance` | Delivery (full stack) | `test/<feature>/test_routers.py` (acceptance class) |
| `@pytest.mark.unit`  | All unit tests   | `test/<feature>/test_*.py` (non-acceptance classes) |

Class-level markers keep test files clean:

```python
@pytest.mark.acceptance
class TestRegisterUsageEventAcceptance:
    """Acceptance tests for POST /api/v1/events."""

    def test_should_return_204_when_payload_is_valid(self, client: TestClient) -> None:
        ...
```

```python
@pytest.mark.unit
class TestRegisterUsageEventRouter:
    """Unit tests for POST /api/v1/events router."""

    def test_should_return_422_when_required_field_is_missing(self, client: TestClient) -> None:
        ...
```

### Scenario references in test names

Link every test back to its Gherkin scenario using an `@sN` tag in the docstring. This creates traceability between the `.feature` file and the test suite:

```python
def test_should_return_204_when_payload_is_valid(self, client: TestClient) -> None:
    """@s1: Register a valid usage event with all fields."""
    ...
```

```python
def test_should_return_422_when_required_field_is_missing(self, client: TestClient) -> None:
    """@s2: Missing a required field returns 422."""
    ...
```

The `@sN` tags correspond to the scenario order in `docs/features/<feature>.feature`.

### Testing the delivery layer

Delivery tests use FastAPI `TestClient` against the ASGI app. Two categories:

**Acceptance tests** — one file per feature, covering the happy path and critical system errors. These test 
the real stack end-to-end. They are few and focus on proving the feature works.

```python
# tests/usage_events/test_routers.py
from fastapi.testclient import TestClient

def test_should_return_204_when_payload_is_valid(client: TestClient) -> None:
    response = client.post("/api/v1/events/", json=valid_payload)
    assert response.status_code == 204
```

**Delivery unit tests** — cover every scenario the acceptance tests do not exercise: validation errors, malformed requests, edge cases, and error responses. The use case collaborator is mocked with doublex so the test stays in the delivery layer.

```python
# tests/usage_events/test_routers.py
from doublex import ANY_ARG, Mock
from doublex_expects import have_been_called_with
from expects import expect, equal

def test_should_return_503_when_database_unavailable(client: TestClient) -> None:
    from usage_events.routers import _get_usage_event_register
    from usage_events.usage_event_register import UsageEventRegister

    register_mock = Mock(UsageEventRegister)
    expect_call(register_mock).execute(ANY_ARG).raises(RuntimeError("Database connection failed"))

    app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
    try:
        response = client.post("/api/v1/events/", json=valid_payload)
        expect(response.status_code).to(equal(503))
    finally:
        app.dependency_overrides.clear()
```

### Testing the application layer

Application tests exercise use cases in isolation. Infra port dependencies are mocked with doublex. These tests cover business rules, orchestration logic, and error handling.

```python
# tests/usage_events/test_usage_event_register.py
from expects import expect, have_length

def test_should_register_usage_event() -> None:
    usage_event = UsageEventMother.dummy()
    usage_event_repository = InMemoryUsageEventRepository()
    register = UsageEventRegister(
        repository=usage_event_repository,
        uuid_generator=FakeUuidGenerator(uuid_value=usage_event["id"]),
    )

    register.execute(**{key: value for key, value in usage_event.items() if key != "id"})

    expect(usage_event_repository).to(have_length(1))
```

### Testing the infra layer

Infra integration tests run against real dependencies (PostgreSQL, external services). They verify adapter contracts match what the domain port promises.

```python
# tests/usage_events/test_postgres_usage_event_repository.py
def test_saves_and_retrieves_invoice(db_session: Session) -> None:
    repo = PostgresUsageEventRepository(db_session)
    event = UsageEventMother.dummy()
    repo.save(event)
    # ... verify via retrieval
```

### Test directory structure

```
tests/
  usage_events/
    test_routers.py                   # acceptance + unit tests for delivery layer
    test_usage_event_register.py      # unit tests for use case
    usage_event_mother.py             # test data factories
    in_memory_usage_event_repository.py  # test double for repository
    fake_uuid_generator.py            # test double for UUID generator
    conftest.py                       # shared fixtures
```

File naming: `test_<module>.py`, matching the module under test in `src/`.

### Object mothers

Test data factories live in `test/<feature>/`. They are used by tests only — never imported in production code.

```
test/
  usage_events/
    usage_event_mother.py             # UsageEventMother + UsageEventMotherForPayload
```

Mothers use static factory methods with sensible defaults and descriptive names:

```python
# test/usage_events/usage_event_mother.py
class UsageEventMother:
    @staticmethod
    def dummy() -> UsageEvent:
        return UsageEvent(
            id="06a2e698-4377-7f43-8000-0a4f8c034fd4",
            ipy_version="1.2.3",
            python_version="3.11",
            operating_system="Linux",
            user_id="550e8400-e29b-41d4-a716-446655440000",
            command="init",
            dependency_manager="uv",
            template="standard",
            built_in_features=["github_actions", "makefile"],
        )


class UsageEventMotherForPayload:
    _BASE_PAYLOAD = {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        ...
    }

    @classmethod
    def dummy(cls) -> dict:
        return dict(cls._BASE_PAYLOAD)

    @classmethod
    def with_missing_field(cls, field_name: str) -> dict:
        return {key: value for key, value in cls._BASE_PAYLOAD.items() if key != field_name}
```

## Benefits

- **Safety net from the outside** — the acceptance test proves the feature works end-to-end before any layer is fully implemented.
- **Contract-first development** — delivery unit tests encode the HTTP contract (status codes, response shapes) before the use case exists.
- **Isolated, fast unit tests** — each layer is tested in isolation with mocked neighbours, keeping the suite fast.
- **Real adapter coverage** — infra integration tests catch database and IO issues that unit tests miss.
- **One Red-Green-Refactor per layer** — prevents building abstractions before they are driven by a test.

## Examples

### Good: Outside-In flow for register usage event

1. Write acceptance test: `POST /api/v1/events/ → 204` → Red (no router)
2. Implement `routers.py` → stubs `UsageEventRegister` → Green
3. Write delivery unit test: missing field returns 422 → Red
4. Add validation to router → Green → Refactor
5. Write application test: use case calls repo.save → Red
6. Implement `UsageEventRegister` → Green
7. Write infra integration test: save and retrieve → Red
8. Implement `PostgresUsageEventRepository` → Green

### Bad: Starting from the domain layer

Write `UsageEvent` TypedDict and `UsageEventRepository` ABC first, then build the use case, then add the router. No acceptance test exists until everything is wired. The domain might be over-engineered because no outer-layer test drove its shape.

### Bad: Mixing test layers

A delivery unit test that also asserts database queries. Slow, coupled, and duplicates both delivery unit and infra integration concerns.

## Real world examples

- `test/usage_events/test_routers.py` — acceptance + unit tests for the delivery layer
- `test/usage_events/test_usage_event_register.py` — application layer unit tests
- `test/usage_events/usage_event_mother.py` — object mothers for test data

## Related agreements

- `docs/conventions/architecture/architecture.md` — the code structure these tests exercise
- `docs/conventions/testing/test-naming.md` — `test_should_<behavior>` naming
- `docs/conventions/testing/object-mother.md` — Object Mother pattern for test data
- `docs/conventions/testing/test-isolation.md` — acceptance vs unit, mocking use cases, test doubles
- `docs/conventions/convention_guidelines.md` — document structure standard
