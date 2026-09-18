# Test Isolation

## Convention

Tests are organized into two levels of isolation: acceptance tests and unit tests. Each level tests a different layer of the application with different mocking strategies.

### Acceptance tests

Acceptance tests verify the full stack (router + use case + repository) without mocking anything. They only assert on HTTP status codes — no response body inspection, no internal state checks.

```python
@pytest.mark.acceptance
class TestRegisterUsageEventAcceptance:
    def test_should_return_204_when_payload_is_valid(self, client: TestClient) -> None:
        payload = UsageEventMotherForPayload.dummy()
        response = client.post("/api/v1/events/", json=payload)
        expect(response.status_code).to(equal(204))
```

### Router unit tests

Router unit tests isolate the router layer by mocking the use case using **doublex**. Each test:
1. Creates a `Mock(UsageEventRegister)`.
2. Sets up expected calls with `expect_call(mock).execute(**payload)`.
3. Overrides the use case dependency via `app.dependency_overrides`.
4. Sends the HTTP request.
5. Asserts the status code.
6. Verifies the mock was called correctly with `expect(mock.execute).to(have_been_called_with(...))`.
7. Cleans up with `app.dependency_overrides.clear()` in a `finally` block.

```python
@pytest.mark.unit
class TestRegisterUsageEventRouter:
    def test_should_return_204_when_payload_is_valid(self, client: TestClient) -> None:
        register_mock = Mock(UsageEventRegister)
        payload = UsageEventMotherForPayload.dummy()
        expect_call(register_mock).execute(**payload)
        app.dependency_overrides[_get_usage_event_register] = lambda: register_mock
        try:
            response = client.post("/api/v1/events/", json=payload)
            expect(response.status_code).to(equal(204))
            expect(register_mock.execute).to(have_been_called_with(**payload))
        finally:
            app.dependency_overrides.clear()
```

### Use case unit tests

Use case unit tests use **in-memory test doubles** instead of mocks. The `InMemoryUsageEventRepository` and `FakeUuidGenerator` are concrete classes that inherit from the ABC port interfaces. Tests exercise the use case directly without HTTP.

```python
class TestUsageEventRegister:
    def test_should_register_usage_event(self) -> None:
        usage_event = UsageEventMother.dummy()
        repository = InMemoryUsageEventRepository()
        register = UsageEventRegister(
            repository=repository,
            uuid_generator=FakeUuidGenerator(uuid_value=usage_event["id"]),
        )
        register.execute(**{k: v for k, v in usage_event.items() if k != "id"})
        expect(repository).to(have_length(1))
```

### Where test doubles live

In-memory repositories and fake implementations live **in `test/` only**, never in `src/`. This signals clearly that they are not production adapters.

```
test/usage_events/
    in_memory_usage_event_repository.py   # test double, inherits from ABC
    fake_uuid_generator.py                # test double, inherits from ABC
```

## Rules

- **Acceptance tests**: Use `@pytest.mark.acceptance`. Only assert on status codes. No mocking.
- **Router unit tests**: Use `@pytest.mark.unit`. Mock use case with doublex (`Mock`, `expect_call`, `have_been_called_with`). Use `dependency_overrides` with try/finally cleanup.
- **Use case unit tests**: Use `@pytest.mark.unit`. Use in-memory test doubles. No doublex mocking of the use case itself.
- **Test fixtures**: FastAPI `TestClient` is a `conftest.py` fixture at the test package level.
- **System module mocking**: Use `@patch` from `unittest.mock` only for Python system modules (`readline`, `atexit`, `subprocess`, `sys`, `os`). Use doublex for all application code.

## Benefits

- Each test level focuses on one layer.
- Router tests fail only when the router contract changes, not when the use case has a bug.
- Use case tests verify business logic without HTTP overhead.
- Acceptance tests catch integration issues without testing everything at that level.
- Clean dependency override cleanup prevents test pollution.

## Real world examples

- `test/usage_events/test_routers.py` — both `TestRegisterUsageEventAcceptance` and `TestRegisterUsageEventRouter`
- `test/usage_events/test_usage_event_register.py` — `TestUsageEventRegister` with in-memory doubles
- `test/usage_events/in_memory_usage_event_repository.py` — test double in `test/`
- `test/usage_events/conftest.py` — `TestClient` fixture

## Related agreements

- `docs/conventions/testing/tdd_outside_in.md` — TDD workflow that produces these test levels
- `docs/conventions/testing/object-mother.md` — Object Mothers for test data
- `docs/conventions/architecture/architecture.md` — ABC port interfaces that enable test doubles
