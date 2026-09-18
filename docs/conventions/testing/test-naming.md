# Test Naming

## Convention

All test functions follow the pattern `test_should_<behavior>` where `<behavior>` describes what the test verifies in plain English.

```python
class TestRegisterUsageEventRouter:
    def test_should_return_204_when_payload_is_valid(self) -> None: ...
    def test_should_return_422_when_required_field_is_missing(self) -> None: ...
    def test_should_return_422_when_user_id_is_invalid_uuid(self) -> None: ...
```

## Rules

- Start every test name with `test_should_`.
- After `test_should_`, describe the expected outcome and the condition that triggers it.
- Use `_when_` to separate the outcome from the condition when both are needed.
- Keep names readable as English phrases: "test should return 204 when payload is valid".
- Avoid repeating the test class name in the function name.

## Benefits

- Test names read like executable specifications.
- Failure messages are self-explanatory: "FAILED test_should_return_422_when_user_id_is_invalid_uuid".
- No need for docstrings or comments — the name says it all.

## Real world examples

- `test_should_return_204_when_payload_is_valid`
- `test_should_return_422_when_field_is_empty_string`
- `test_should_register_usage_event`

## Related agreements

- `docs/conventions/testing/tdd_outside_in.md` — TDD workflow that produces these tests
