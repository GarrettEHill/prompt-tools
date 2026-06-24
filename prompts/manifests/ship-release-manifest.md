# Ship release manifest

Loaded by [`bootstrap-ship-release.md`](../bootstrap-ship-release.md).

## Bootstrap (load once)

```text
patterns/release-coordinator/release-coordinator.md
patterns/release-coordinator/release-worker.md
patterns/release-coordinator/release-checklist.md
patterns/ship-checklist/ship-checklist.md
patterns/ship-checklist/gate-template.md
patterns/rollback-plan/rollback-plan.md
patterns/rollback-plan/rollback-template.md
patterns/continuous-completion-model/continuous-completion-model.md
patterns/disposable-worker/disposable-worker.md
patterns/live-state-refresh/live-state-refresh.md
patterns/final-report/final-report-template.md
adapters/semver-release/domain-adapter.md
primitives/ship-gate-schema/ship-gate-schema.md
primitives/git-github-safety/git-github-safety.md
primitives/validation-ladder/validation-ladder.md
primitives/compact-result-schema/compact-result-schema.md
primitives/stop-blocker-decision-tree/stop-blocker-decision-tree.md
```

## Per slice iteration

Load: `patterns/live-state-refresh/preflight-checklist.md` (refresh)  
Then: `patterns/release-coordinator/release-worker.md` + slice acceptance criteria.

## Stop

Load: `patterns/final-report/final-report-template.md`  
Load: `primitives/stop-blocker-decision-tree/stop-blocker-decision-tree.md`

If ship gate fails, hand off blockers via `prompts/bootstrap-remediate.md`.
