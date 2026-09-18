# No Comments

## Convention

Code must be self-documenting through expressive naming. Comments are not allowed in source code or test files.

## Rationale

- Comments drift out of sync with code; names do not.
- Well-named code already communicates intent.
- Tests serve as executable documentation.

## What to do instead of commenting

| Instead of a comment... | ...use a better name |
|--------------------------|----------------------|
| `# Validate that the version is semver` | `def validate_strict_semver(...)` |
| `# Clean up the dependency override` | `finally: app.dependency_overrides.clear()` |
| `# Arrange` | (nothing — the code already shows setup) |
| `# Act` | (nothing — the action call already shows what's happening) |
| `# Assert` | (nothing — `expect(...)` already reads as assertion) |

## Exceptions

None. If code is unclear, rename until it is clear.

## Related agreements

- `docs/conventions/testing/test-naming.md` — test names replace test docstrings
