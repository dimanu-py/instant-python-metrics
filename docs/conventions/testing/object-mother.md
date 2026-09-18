# Object Mother

## Convention

Test data is created via Object Mother classes — static factories that return pre-configured test objects with sensible defaults, plus named variants for specific scenarios.

A feature may have multiple Object Mothers when the data shapes differ (e.g., domain entity vs. HTTP payload).

```python
class UsageEventMother:
    """Domain entity factory."""
    @staticmethod
    def dummy() -> UsageEvent:
        return UsageEvent(
            id="06a2e698-4377-7f43-8000-0a4f8c034fd4",
            ipy_version="1.2.3",
            python_version="3.11",
            ...
        )


class UsageEventMotherForPayload:
    """HTTP payload factory."""
    _BASE_PAYLOAD = {
        "ipy_version": "1.2.3",
        "python_version": "3.11",
        ...
    }

    @classmethod
    def dummy(cls) -> dict:
        return dict(cls._BASE_PAYLOAD)

    @classmethod
    def without_built_in_features_selected(cls) -> dict:
        return {**cls._BASE_PAYLOAD, "built_in_features": []}

    @classmethod
    def with_missing_field(cls, field_name: str) -> dict:
        return {k: v for k, v in cls._BASE_PAYLOAD.items() if k != field_name}
```

## Rules

- Name the mother `<Entity>Mother` for domain entities, `<Entity>MotherForPayload` for HTTP payloads.
- Provide a `dummy()` classmethod or staticmethod that returns the default valid instance.
- Name variants `without_<variant>()`, `with_<variant>()` for divergent cases.
- Keep `_BASE_PAYLOAD` as a class-level dict for payload mothers; return copies so callers can mutate.
- Place the Object Mother file in the test package at the same level as the tests that use it.

## Benefits

- Test setup is a single line: `UsageEventMotherForPayload.dummy()`.
- Named variants document the different data shapes under test.
- Changes to the domain entity only require updating the mother, not every test.

## Real world examples

- `test/usage_events/usage_event_mother.py` — `UsageEventMother` (domain) and `UsageEventMotherForPayload` (HTTP payload)
- `UsageEventMother.dummy()` used in use case unit tests
- `UsageEventMotherForPayload.dummy()` used in acceptance and router tests
- `UsageEventMotherForPayload.with_missing_field("ipy_version")` used in validation tests

## Related agreements

- `docs/conventions/testing/test-naming.md` — tests that use Object Mothers
