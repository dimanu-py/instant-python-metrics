# Code Structure

## Convention

The codebase follows a screaming architecture organized by feature. Each feature contains all its layers internally, 
making the project root scream what the application does (invoices, users, reports) rather than 
what framework it uses.

### Feature structure

Every feature follows this internal layout:

```
src/
  invoices/                        # ← feature name (plural noun)
    delivery/                        #   FastAPI routers
      __init__.py
      router.py
    application/                     #   orchestration actors
      __init__.py
      create_invoice.py
      list_invoices.py
    domain/                          #   aggregates, entities, value objects, ports
      __init__.py
      invoice.py
      invoice_repository.py          #   port interface
      value_objects.py
    infra/                           #   port implementations
      __init__.py
      postgres_invoice_repository.py
  users/
    delivery/
    application/
    domain/
    infra/
```

### Layer responsibilities

**Delivery (`delivery/`)** — FastAPI routers. Handles HTTP concerns: parsing requests, returning responses, status codes. Does NOT contain business logic. Delegates immediately to an application use case.

**Application (`application/`)** — Orchestrators. Each use case has a single responsibility and a single entry point (`execute`). It imports domain entities, applies business rules, creates aggregates, and calls port interfaces to persist or retrieve data.

**Domain (`domain/`)** — The innermost layer. Contains aggregates, entities, value objects, and port interfaces. It imports NOTHING from outer layers (delivery, application, infra). External collaborators are abstracted through port interfaces living directly in this folder.

**Infra (`infra/`)** — Concrete implementations of port interfaces defined in the domain layer. One adapter class per port interface.

### Layer communication rules

```
delivery/ ──→ application/ ──→ domain/
                             │
                        infra/  (implements ports from domain/)
```

- `delivery/` imports and instantiates use cases directly, passing any required infra adapters.
- `application/` imports domain entities, value objects, and port interfaces. It also imports concrete adapters from `infra/` when the router does not provide them.
- `domain/` has zero imports from `delivery/`, `application/`, or `infra/`.
- `infra/` imports domain port interfaces to implement them.

No shared folder exists until a pattern is used across three or more features (YAGNI).

### Naming conventions

| Layer       | File naming                      | Class naming                     |
|-------------|----------------------------------|----------------------------------|
| delivery    | `router.py` per feature          | standard FastAPI router function |
| application | `invoice_creator.py`             | `InvoiceCreator`                 |
| domain      | `invoice.py`, `invoice_id.py`    | `Invoice` (aggregate)            |
| infra       | `postgres_invoice_repository.py` | `PostgresInvoiceRepository`      |

Port interfaces in `domain/` use `abc.ABC` and are named after the concept, not the implementation (e.g., `InvoiceRepository`, not `PostgresInvoiceRepository`).

## Benefits

- **Screaming architecture** — the folder tree reads like a feature list, not a framework list.
- **Strong isolation** — domain has no framework dependencies; swapping the delivery mechanism or database requires changing only one layer.
- **Discoverable** — every file for a feature lives under one tree; no jumping between layer directories.
- **Testable** — port interfaces in domain allow easy adapter swapping in tests.
- **YAGNI-compliant** — no shared abstractions until the codebase proves they are needed.

## Examples

### Good: Feature with a single use case

```
src/invoices/delivery/router.py              # GET /invoices, POST /invoices
src/invoices/application/invoice_creator.py
src/invoices/domain/invoice.py               # Invoice aggregate
src/invoices/domain/invoice_repository.py    # InvoiceRepository port
src/invoices/infra/postgres_invoice_repository.py
```

Router creates the adapter and use case, then calls execute:

```python
@router.post("/invoices", status_code=201)
def create_invoice(payload: CreateInvoiceRequest) -> InvoiceResponse:
    repo = PostgresInvoiceRepository(db.session)
    uc = CreateInvoiceUseCase(repo)
    result = uc.execute(payload)
    return InvoiceResponse.from_domain(result)
```

### Bad: Layer-organized structure

```
src/delivery/invoices.py
src/application/invoice_creation.py
src/domain/invoice.py
src/infra/postgres_invoice_repository.py
```

Scattered files make it hard to find all pieces of a feature. Changing a feature requires touching files in four separate top-level directories.

### Good: Port interface in domain

```python
# src/invoices/domain/invoice_repository.py
from typing import Protocol

class InvoiceRepository(Protocol):
    def save(self, invoice: Invoice) -> None: ...
```

### Bad: Port coupled to implementation

```python
# src/invoices/application/create_invoice.py
from src.invoices.infra.postgres_invoice_repository import PostgresInvoiceRepository
```

Use case depends directly on a concrete adapter, making it impossible to test without a database.

## Real world examples

- `src/` — the codebase follows this structure

## Related agreements

- `docs/conventions/convention-guidelines.md` — document structure standard
- `docs/conventions/leader_workflow.md` — the development pipeline this code structure supports
