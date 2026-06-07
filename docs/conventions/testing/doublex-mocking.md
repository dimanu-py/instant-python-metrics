# doublex Mocking Patterns

## Convention

Use `doublex` for all mocking in unit and application-layer tests. The `doublex.Mock` class creates test doubles from Protocol types, and `expect_call` sets up expectations and stubs.

Follow these patterns when mocking repository ports and other dependencies:

### Basic pattern: Mock and expect_call

```python
from doublex import Mock, expect_call

repository = Mock(UsageEventRepository)
expect_call(repository).save(ANY_ARG)
```

This creates a mock that expects `save()` to be called once with any argument. If `save()` is not called, the test fails automatically when the mock is garbage-collected.

### Pattern: Simulating errors with raises

```python
from doublex import ANY_ARG, Mock, expect_call

repository = Mock(UsageEventRepository)
expect_call(repository).save(ANY_ARG).raises(RuntimeError("Database connection failed"))
```

This creates a mock that raises an exception when `save()` is called, allowing tests to verify error-handling paths.

### Pattern: Accessing captured arguments

```python
from doublex import ANY_ARG, Mock, expect_call

repository = Mock(UsageEventRepository)
expect_call(repository).save(ANY_ARG)

use_case.execute(...)

saved_event = repository.save.calls[0].args[0]
expect(saved_event.ipy_version).to(equal("1.2.3"))
```

Access `repository.<method>.calls` to inspect captured call arguments. Each call has `.args` (positional) and `.kwargs` (keyword) attributes.

### Pattern: Type-safe mock creation

```python
from typing import Any

repository: Any = Mock(UsageEventRepository)
```

Declare the mock as `Any` to avoid mypy errors about type incompatibility between the mock and the Protocol.

## Benefits

- **Isolated tests** — mocks replace real infrastructure, keeping tests fast and deterministic.
- **Self-verifying** — `expect_call` verifies the expected call happened; no need for explicit `verify()` calls.
- **Readable** — expectations are set up before the action, following Arrange-Act-Assert.
- **Consistent across the codebase** — one mocking library, one pattern, no surprises.

## Examples

### Good: Mocking a repository port in application unit tests

```python
from typing import Any

from doublex import ANY_ARG, Mock, expect_call

def test_saves_event_with_all_fields() -> None:
    repository: Any = Mock(UsageEventRepository)
    expect_call(repository).save(ANY_ARG)
    use_case = RegisterUsageEventUseCase(repository)

    event_id = use_case.execute(
        ipy_version="1.2.3",
        operating_system="linux",
        distinct_id="a1b2c3d4-e5f6-4789-abcd-ef1234567890",
        command="generate",
        python_version="3.13.1",
        dependency_manager="uv",
        template="standard_project",
        built_in_features=["github_actions"],
    )

    expect(event_id).to_not(be_none)
    saved_event = repository.save.calls[0].args[0]
    expect(saved_event).to(have_properties(
        ipy_version="1.2.3",
        command="generate",
    ))
```

### Good: Simulating a database error in delivery tests

```python
from doublex import ANY_ARG, Mock, expect_call

def test_database_unavailable_returns_503(client: TestClient) -> None:
    repository = Mock(UsageEventRepository)
    expect_call(repository).save(ANY_ARG).raises(RuntimeError("Database connection failed"))

    client.app.dependency_overrides[_get_repository] = lambda: repository

    response = client.post("/api/v1/events", json=valid_payload)

    expect(response.status_code).to(equal(503))

    client.app.dependency_overrides.clear()
```

### Bad: Mocking without expectation (no verification)

```python
def test_saves_event() -> None:
    repository = MagicMock()  # No expect_call — no verification
    use_case = RegisterUsageEventUseCase(repository)
    use_case.execute(...)
    # Did save() actually get called? The test doesn't verify.
```

### Bad: Using unittest.mock for application code

```python
from unittest.mock import Mock  # Wrong — use doublex for app code

repository = Mock(UsageEventRepository)
```

### Good: Mocking with expect_call for repositories
```python
from doublex import Mock, expect_call
from doublex_expects import have_been_called_with
from expects import expect

def test_use_case_calls_save() -> None:
    repository = Mock(UsageEventRepository)
    expect_call(repository).save(ANY_ARG)
    use_case = RegisterUsageEventUseCase(repository)

    use_case.execute(...)

    expect(repository.save).to(have_been_called_with(...))
```

## Real world examples

- `test/usage_events/application/test_register_usage_event.py` — `Mock(UsageEventRepository)` with `expect_call(repository).save(ANY_ARG)`
- `test/usage_events/delivery/test_router.py` — `expect_call(repository).save(ANY_ARG).raises(...)` for 503 test

## Related agreements

- `docs/conventions/testing/tdd-outside-in.md` — test pyramid and mock placement
- `docs/conventions/architecture/architecture.md` — repository port interface (what gets mocked)
