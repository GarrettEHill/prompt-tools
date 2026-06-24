# Ship rollback manifest

Loaded by [`bootstrap-ship-rollback.md`](../bootstrap-ship-rollback.md).

## Bootstrap (load once)

```text
patterns/rollback-plan/rollback-plan.md
patterns/rollback-plan/rollback-template.md
patterns/live-state-refresh/live-state-refresh.md
primitives/git-github-safety/git-github-safety.md
```

## Run

1. Live refresh
2. Inspect release diff, migrations, deploy manifests
3. Fill rollback-template

Read-only — no rollback execution.
