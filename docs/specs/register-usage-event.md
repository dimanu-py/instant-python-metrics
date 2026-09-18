# Register Usage Event

## Purpose

Register a usage event sent by the CLI tool, validate it against business rules, persist it to PostgreSQL, and confirm with a success response.

## Behavior

A client sends a POST request to `/api/v1/events` with a JSON body containing eight required fields. The system validates the payload in two stages: first, Pydantic v2 parses the request body and performs type checks and basic format validations; second, domain-level validation ensures `ipy_version` follows strict semver (`X.Y.Z` with no pre-release or build metadata) and `python_version` follows relaxed semver (`X.Y` or `X.Y.Z`).

If all validations pass, the event is stored in the `usage_events` table with a server-generated UUID v7 identifier and a server-generated `created_at` timestamp. The response is **204 No Content** — the client is fire-and-forget and does not consume the response body.

If any validation fails, the response is **422 Unprocessable Entity** with the standard Pydantic error detail array. FastAPI's built-in JSON parsing error also produces 422, never 400.

Extra fields in the request body are silently ignored. An empty `built_in_features` array is accepted.

## Contract

### Inputs

- **Method**: `POST`
- **Path**: `/api/v1/events`
- **Content-Type**: `application/json`

**Request body** (all 8 fields required):

| Field                | Type            | Constraints                                                       |
|----------------------|-----------------|-------------------------------------------------------------------|
| `ipy_version`        | string          | Non-empty, strict semver `X.Y.Z`, max 256 characters              |
| `python_version`     | string          | Non-empty, relaxed semver `X.Y` or `X.Y.Z`, max 256 characters    |
| `operating_system`   | string          | Non-empty, max 256 characters                                     |
| `user_id`            | string          | UUID v4 format, max 256 characters                                |
| `command`            | string          | Non-empty, max 256 characters                                     |
| `dependency_manager` | string          | Non-empty, max 256 characters                                     |
| `template`           | string          | Non-empty, max 256 characters                                     |
| `built_in_features`  | array of strings| May be empty; no empty strings inside; each string max 256 chars  |

Extra fields in the JSON body: silently ignored (Pydantic `model_config = {"extra": "ignore"}`).

### Outputs

#### 204 No Content

- **Status**: 204 No Content
- **Body**: empty
- **Rationale**: The CLI client sends events fire-and-forget. It does not read the response. Returning a body would add bytes to the wire with zero value.

#### 422 Unprocessable Entity

- **Body**:
  ```json
  {
    "detail": [
      {
        "loc": ["body", "ipy_version"],
        "msg": "String should match pattern '^\\d+\\.\\d+\\.\\d+$'",
        "type": "string_pattern_mismatch"
      }
    ]
  }
  ```

Standard FastAPI/Pydantic v2 error format. Multiple validation errors are reported in a single array when present.

## Edge Cases

1. **Missing required field** — Any of the 8 required fields omitted from the body → 422 with one error entry per missing field.
2. **Empty string field** — Any required string field is `""` → 422.
3. **Invalid strict semver (`ipy_version`)** — Value does not match `X.Y.Z` (e.g., `"1"`, `"1.2"`, `"1.2.3.4"`, `"1.02.3"`, `"1.2.3-alpha"`, `"1.2.3+build"`) → 422.
4. **Invalid relaxed semver (`python_version`)** — Value does not match `X.Y` or `X.Y.Z` (e.g., `"3"`, `"3.10.0.1"`, `"three"`) → 422.
5. **Invalid UUID v4 (`user_id`)** — Value is not a valid UUID (e.g., `"not-a-uuid"`) → 422.
6. **Non-array `built_in_features`** — Value is not a JSON array (e.g., string, object, number, null) → 422.
7. **Empty strings inside `built_in_features`** — Array contains one or more empty strings → 422.
8. **Empty `built_in_features` array** — Array is `[]` → 201 (accepted).
9. **Extra unknown fields** — Body contains fields not in the schema → 201 (silently ignored).
10. **Malformed JSON body** — Body is not valid JSON (e.g., trailing comma, unquoted `null`, single quotes) → 422 via FastAPI's built-in `RequestValidationError`.
11. **All fields empty string** — All 8 fields provided as empty strings → 422 with error entries for all 8 fields.
12. **Mix of valid and invalid** — Some fields valid, some invalid → 422 with error entries only for the invalid fields.
13. **String exceeds 256 characters** — Any string field (including individual strings inside `built_in_features`) exceeds 256 characters → 422.

## Decisions

### Sync API with FastAPI
- **Decision**: Use FastAPI with synchronous endpoints, synchronous SQLAlchemy, and psycopg2.
- **Rationale**: The CLI tool sends events fire-and-forget. There is no concurrent client benefit from async. Sync code is simpler to write, test, and debug.
- **Alternative rejected**: Async FastAPI with async SQLAlchemy and asyncpg. Adds complexity (event loop management, async test fixtures) with zero benefit for this use case.

### Flat feature structure with shared modules
- **Decision**: Organize code as a flat `usage_events/` feature folder. Shared infrastructure lives in `common/` (error types, HTTP response helpers).
- **Rationale**: The feature is a single use case — sub-layers add navigation overhead for no benefit. Flat structure keeps related files close. Shared patterns in `common/` are reusable across future features without premature abstraction.
- **Alternative rejected**: Screaming architecture with delivery/application/domain/infra sub-layers per feature. Over-engineered for a single-endpoint feature.

### ABC with explicit inheritance for port interfaces
- **Decision**: Port interfaces use `abc.ABC` with `@abstractmethod`. Adapters inherit explicitly from the interface.
- **Rationale**: Makes implementations discoverable (IDE "go to implementations" works). Clear contract enforcement at runtime. Explicit inheritance makes the relationship between interface and adapter obvious.
- **Alternative rejected**: `typing.Protocol` with structural subtyping. Hides the relationship between interface and implementation; "go to implementations" in most IDEs does not work.

### UUID v7 for event entity IDs (injected port)
- **Decision**: Event IDs are UUID v7, generated via an injected port interface (`UuidGenerator` ABC). The default implementation uses `uuid_extensions.uuid7()`.
- **Rationale**: UUID v7 is time-sortable, improving B-tree index performance in PostgreSQL. An injected port makes tests deterministic (can inject a fake that returns fixed UUIDs). Aligns with `docs/conventions/architecture/uuid-v7.md`.
- **Alternative rejected**: UUID v4 (`uuid.uuid4()`) causes index fragmentation. Auto-increment integers require coordination and leak business information (event count).

### `created_at` as ORM default (no Clock port)
- **Decision**: The `created_at` timestamp is set via a `default=lambda: datetime.now(UTC)` on the SQLAlchemy column. No injected Clock interface is used.
- **Rationale**: The domain logic never needs to read or control the timestamp — it is purely an infrastructure concern (audit trail). Adding a port interface would be YAGNI. The ORM column default is simpler and sufficient.
- **Alternative rejected**: Injected `Clock` port interface (previously implemented and removed during TDD when no test demanded it).

### Pydantic v2 with BeforeValidator for request parsing
- **Decision**: Use Pydantic v2 models in the router for request parsing. Domain validators (semver, UUID) are injected via `BeforeValidator`. Validators raise `ValueError` for Pydantic compatibility.
- **Rationale**: FastAPI ships with Pydantic v2. `BeforeValidator` allows running custom domain validation functions before Pydantic's built-in validation. Raising `ValueError` produces clean 422 responses with field-level error locations.
- **Alternative rejected**: `Field` validators that raise `DomainError` — Pydantic's `BeforeValidator` only catches `ValueError`/`TypeError`/`AssertionError`, not custom exception types.

### Domain validation as standalone functions
- **Decision**: Semver and UUID validation are standalone functions in `validators.py` (not methods on a class or value objects).
- **Rationale**: Functions are simpler to test and reuse. They are injected into Pydantic via `BeforeValidator`. No state, no class hierarchy.
- **Alternative rejected**: Value object classes (e.g., `IpyVersion(value)`). Adds ceremony for single-format validation. Would make sense if versions had behavior beyond validation.

### Extra fields silently ignored
- **Decision**: Pydantic `model_config = {"extra": "ignore"}` discards unknown fields.
- **Rationale**: The CLI client may add future fields before the server supports them. Forward compatibility. The CLI does not read the response, so it does not need to know whether extra fields were accepted.
- **Alternative rejected**: `"extra": "forbid"` would reject requests with unknown fields, breaking forward compatibility. `"extra": "allow"` would expose extra fields in the response but we do not echo the body.

### All validation errors return 422, never 400
- **Decision**: All validation failures, including malformed JSON, semver errors, and domain validation errors, produce 422 Unprocessable Entity.
- **Rationale**: FastAPI's default behavior for Pydantic validation errors and JSON parse errors is 422. Consistency: one error status code for all client-side validation failures.
- **Alternative rejected**: Using 400 for malformed JSON and 422 for schema violations. Inconsistent; the client must handle two error codes for the same class of errors.

### One table `usage_events` with JSONB for `built_in_features`
- **Decision**: Single table with one column per field. `built_in_features` uses `JSONB` (PostgreSQL). All other fields are `VARCHAR(256) NOT NULL`.
- **Rationale**: Simplest schema that satisfies the requirement. JSONB allows querying array contents with PostgreSQL operators if needed later.
- **Alternative rejected**: Normalized `usage_event_features` join table for `built_in_features`. Adds complexity (joins, cascade deletes, additional ORM model) for a feature that currently only stores and retrieves events. Deferred until Grafana panel requirements prove the need.

### 204 No Content response (fire-and-forget client)
- **Decision**: Successful registration returns **204 No Content** with an empty body.
- **Rationale**: The CLI client sends events fire-and-forget and ignores the response. Returning a body adds wire overhead with zero value. 204 is the HTTP standard for "operation succeeded, no content to return."
- **Alternative rejected**: 201 Created with `{"id": "..."}`. Standard REST but wasteful for a client that discards the response. Was tried in an earlier version and simplified.

### Max length 256 characters for all VARCHAR fields
- **Decision**: All string columns use `VARCHAR(256)`. Validated in Pydantic and enforced in the database schema.
- **Rationale**: 256 characters is generous for all fields (CLI tool name, version strings, OS name, command name). Round number.
- **Alternative rejected**: No length limit. Risk of unbounded storage growth from a misbehaving CLI. `TEXT` column type is semantically wrong for short strings.

### SQLAlchemy data mapper pattern
- **Decision**: `PostgresUsageEventRepository` uses a data mapper: a `UsageEventTable` ORM class maps columns, and the repository has `_to_table()` / `_from_table()` methods to convert between domain dict and ORM model.
- **Rationale**: Separates the domain representation (`TypedDict`) from the persistence representation (ORM model). The repository owns the conversion, keeping both layers decoupled. The session is injected via constructor, making the repository testable with a fake session.
- **Alternative rejected**: Active Record pattern where the domain entity inherits from the ORM base. Couples domain to SQLAlchemy; violates separation of concerns.

### Use case naming: `<Object><Action>`
- **Decision**: Use cases are named `<noun><verb>` (e.g., `UsageEventRegister`, not `RegisterUsageEvent`).
- **Rationale**: Groups related use cases alphabetically in IDE autocomplete — `EventRegister`, `EventCancel`, `EventList` all appear under "Event". More natural in conversation ("the EventRegister use case").
- **Alternative rejected**: Verb-first naming (`RegisterUsageEvent`). Scatters related use cases across the alphabet.

### Test naming: `test_should_<behavior>`
- **Decision**: All test names follow the pattern `test_should_<expected_behavior>` (e.g., `test_should_return_204_when_payload_is_valid`).
- **Rationale**: Test names read as complete sentences, making failures immediately understandable. Consistent format across the entire test suite.
- **Alternative rejected**: `test_<scenario>_<expected>` (e.g., `test_valid_payload_returns_204`). Less readable when reading failure output.

### Acceptance tests only check status code
- **Decision**: Acceptance tests verify only `response.status_code`. They do NOT inspect response body, headers, or stored data.
- **Rationale**: Acceptance tests validate the system is wired correctly end-to-end. Fine-grained contract validation belongs in unit tests (router tests with mocked use case), where failures produce precise diagnostics.
- **Alternative rejected**: Full contract validation in acceptance tests (body, headers, database state). Creates brittle tests that fail on unrelated changes. Forces a real database in the test suite.

### Router unit tests mock the use case
- **Decision**: Router unit tests mock the `UsageEventRegister` use case using doublex and override the FastAPI dependency via `app.dependency_overrides`. They validate the HTTP contract (status code, body, headers) and verify the use case was called with correct arguments.
- **Rationale**: Isolates the router layer from the use case. Tests are fast (no DB, no real UUID generation). Each failure points to exactly which layer is broken.
- **Alternative rejected**: Testing the router through the full stack (real use case, real DB). Slower, more setup, failures are harder to diagnose.

### Test data: Object Mother pattern
- **Decision**: Test payloads are created via static factory methods on `UsageEventMotherForPayload` (e.g., `UsageEventMotherForPayload.dummy()`, `UsageEventMotherForPayload.with_missing_field("ipy_version")`).
- **Rationale**: Descriptive names give meaning to test data. A test using `UsageEventMotherForPayload.dummy()` says "I don't care what the values are, I just need a valid payload." `with_missing_field("ipy_version")` says "this is a payload that intentionally lacks ipy_version."
- **Alternative rejected**: Inline dictionaries in every test. Duplicates field names, hides intent, breaks when fields change.

### InMemoryUsageEventRepository in tests only
- **Decision**: `InMemoryUsageEventRepository` lives exclusively in `test/`. Production uses `PostgresUsageEventRepository` with a real SQLAlchemy session.
- **Rationale**: The in-memory repo is a test double, not a production implementation. Keeping it in `test/` signals that it is not a valid production adapter.
- **Alternative rejected**: Having both `InMemoryUsageEventRepository` and `PostgresUsageEventRepository` in `src/`. Misleading — the in-memory version has no production use case.
- **Decision**: If `built_in_features` is not an array, error location is `["body", "built_in_features"]`. If an element inside the array is empty, error location is `["body", "built_in_features", 0]` (index of the empty string).
- **Rationale**: Standard Pydantic behavior for nested validators. The client can identify which specific item failed.
- **Alternative rejected**: A single top-level error for "built_in_features contains invalid values". Imprecise; client cannot fix the offending item without trial and error.

## Open Questions

None. All decisions are settled.

## Related Features

See [register-usage-event.feature](../features/register-usage-event.feature)
