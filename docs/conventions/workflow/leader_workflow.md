# Leader Workflow

## Convention

The development process follows a strict pipeline with a single human approval gate. Features are tracked 
as Linear issues in the "Instant Python Metrics" project (team: Dimanupy). Each issue carries one of two labels:
`sdd` (requires Spec-Driven Development) or `not-sdd` (skips the spec conversation).

### State machine (Linear issue statuses)

```
Backlog ──→ Todo ──→ In Progress ──→ Release ──(manual)──→ Done
```

The `Release → Done` transition is manual — the user moves it when they confirm the release.

### Pipeline per label

**For `sdd` features (full SDD):**
```
Backlog
    → [spec_partner]  conversation + Gherkin distillation → .md spec and .feature files
    → ⏸ HUMAN APPROVES the scenarios
    → Todo (leader sets when spec is ready)
    → In Progress (leader sets after human approval)
    → [tdd_craftsman]  Red → Green → Refactor cycle (one test at a time)
    → [judge]          review + mutation testing → sets status to Release on approval
    → [convention_keeper]  capture learnings → update convention docs
    → (user manually moves from Release to Done)
```

**For `not-sdd` features (skip spec):**
```
Backlog
    → Todo (leader marks as ready, no spec needed)
    → In Progress
    → [tdd_craftsman]  Red → Green → Refactor cycle
    → [judge]          review + mutation testing → sets status to Release on approval
    → [convention_keeper]  capture learnings → update convention docs
    → (user manually moves from Release to Done)
```

One feature at a time. For `sdd` features: one human approval gate on the Gherkin scenarios,
before writing production code.

### Phase details

1. **spec_partner** (sdd only): the spec is born from conversation, not dictation. The agent debates edge cases, 
output contracts, and discarded alternatives with the human. The result is a reasoned `.md` spec file 
documenting decisions and their rationale. The same agent then distills the spec into executable Gherkin 
scenarios in a `.feature` file.
2. **Human approval gate** (sdd only): the `.feature` scenarios are the executable contract. The human must read and 
approve them before any production code is written. Approving late (after code exists) is expensive; approving 
the Gherkin is cheap and is the point of maximum leverage. The leader **stops** here and waits.
3. **tdd_craftsman**: one test at a time following the Three Laws of TDD: Red (write a failing test), Green (minimum code to pass), 
Refactor (clean up in green). No code is written that no test asks for.
4. **judge**: reviews all code and tests, then runs mutation testing. The review step is the whole 
game: agents draft, judgment prunes. Mutation testing validates that the test suite actually 
catches defects. Only when both review and mutation succeed does the judge set the issue status to `Release`.
5. **convention_keeper**: reviews the completed feature's artifacts (spec, progress logs, judge verdict), identifies new patterns or practices worth standardising, and creates or updates convention docs in `docs/conventions/`. Always asks the human to approve new convention files before finalising.

### Artifact map

| File                           | Created by    | Content                                         |
|--------------------------------|---------------|-------------------------------------------------|
| `docs/specs/<name>.md`         | spec_partner  | Spec conversation: purpose, contract, decisions |
| `docs/features/<name>.feature` | spec_partner  | Gherkin scenarios (the signed contract)         |
| `src/`, `test/`                | tdd_craftsman | Production code and tests, carved by TDD        |
| `progress/tdd_<name>.md`       | tdd_craftsman | Cycle log + scenario-to-test map                |
| `progress/judge_<name>.md`     | judge         | Review verdict + mutation score                 |
| `docs/conventions/`            | convention_keeper | New or updated convention docs              |

Issue status is managed in Linear (not a local file). The craftsman_leader and judge use
`linear_save_issue` to transition statuses. The user manually moves `Release → Done`.

### Anti-broken-telephone rule

Subagents write results to files (listed above) and return only the file reference, never 
the content through chat. This prevents information loss and keeps the audit trail on disk.

## Benefits

- **Single human gate** keeps approval cost low and leverage high — catch contract flaws before code exists.
- **Spec conversation** surfaces hidden edge cases that written requirements miss.
- **TDD strictness** ensures every line of code is justified by a failing test.
- **Mutation testing** proves the test suite catches real defects, not just that the code runs.
- **One feature at a time** prevents context switching and partial work.
- **File-based handoffs** prevent information loss across agent handovers.

## Examples

### Good: Following the full pipeline (sdd)

A feature enters with status `Backlog` and label `sdd` in Linear. The leader launches `spec_partner`, which debates with the human, 
writes `docs/specs/new-feature.md`, then generates `docs/features/new-feature.feature`. The leader
stops and asks the human to approve.
The human reads the scenarios, approves them.
The leader updates the Linear issue to `In Progress`, launches `tdd_craftsman`.
Once tests pass, `judge` reviews and runs mutation. All green → judge sets Linear status to `Release`, then `convention_keeper` captures learnings and updates conventions. The user moves the issue to `Done` when ready.

### Good: Following the pipeline (not-sdd)

A feature enters with status `Backlog` and label `not-sdd`. The leader marks it `Todo`, then `In Progress`, and launches `tdd_craftsman` directly (no spec conversation). The rest is the same: TDD → judge → Release → conventions → manual Done.

### Bad: Skipping the spec conversation (sdd feature)

A leader launches `tdd_craftsman` directly on a `Backlog` feature with label `sdd` because the requirements seem clear. The coder writes tests that pass but miss the actual business behavior. No `.feature` file exists. The `judge` rejects for missing spec coverage, and everything rolls back.

### Bad: Setting an sdd feature to Release without judge approval

The leader sets an issue to `Release` without launching the `judge`. The user expects `Release` to mean "reviewed and mutation-tested". When they move it to `Done`, they get untested code.

### Bad: Two features in flight

The leader starts spec for feature A, then launches TDD for feature B while waiting for human approval on A. The coder on B is blocked by ambiguous scenarios, and the human now has two unapproved `.feature` files to review. The pipeline ensures one feature at a time for a reason.

## Real world examples

- `docs/specs/` — contains `.md` spec files produced by this pipeline
- `docs/features/` — contains `.feature` files produced by this pipeline
- `.agents/agents/craftsman_leader.md` — the orchestrator agent that implements this workflow
- `.agents/agents/spec_partner.md` — spec conversation agent
- `.agents/agents/tdd_craftsman.md` — TDD execution agent
- `.agents/agents/judge.md` — review and mutation agent
- `.agents/agents/convention_keeper.md` — convention documentation agent

## Related agreements

- `docs/conventions/convention-guidelines.md` — document structure standard