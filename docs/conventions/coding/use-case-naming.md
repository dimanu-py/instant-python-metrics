# Use Case Naming

## Convention

Use case classes follow the `<Object><Action>` naming pattern. The file is named `<object>_<action>.py`.

```
File: usage_event_register.py
Class: UsageEventRegister
Method: execute
```

## Rules

- Class name = `<Object><Action>` (PascalCase).
- File name = `<object>_<action>.py` (snake_case).
- The only public method is `execute(...)`.
- The constructor receives all dependencies via parameter injection.

## Benefits

- Names read as natural commands: "Usage Event Register", "Invoice Send".
- File names are predictable: given a concept, you know where to look.
- Consistent naming reduces guesswork across features.

## Real world examples

- `src/usage_events/usage_event_register.py` → `UsageEventRegister`
- Method signature: `def execute(self, ...) -> None`

## Related agreements

- `docs/conventions/architecture/architecture.md` — flat feature structure where use case files live
