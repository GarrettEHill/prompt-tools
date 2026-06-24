# Ship checklist manifest

Loaded by [`bootstrap-ship-checklist.md`](../bootstrap-ship-checklist.md).

## Bootstrap (load once)

```text
patterns/ship-checklist/ship-checklist.md
patterns/ship-checklist/gate-template.md
patterns/live-state-refresh/live-state-refresh.md
primitives/ship-gate-schema/ship-gate-schema.md
primitives/git-github-safety/git-github-safety.md
```

## Run

1. Live refresh
2. Evaluate gates per ship-checklist
3. Fill gate-template and emit ship-gate-schema

Read-only — no version bumps or deploys.
