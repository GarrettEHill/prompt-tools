# Remediation load manifest

Loaded by [`run-audit-remediation.md`](../run-audit-remediation.md).

## Bootstrap (load once)

```text
patterns/continuous-completion-model/continuous-completion-model.md
patterns/disposable-worker/disposable-worker.md
patterns/live-state-refresh/live-state-refresh.md
patterns/final-report/final-report-template.md
primitives/git-github-safety/git-github-safety.md
primitives/validation-ladder/validation-ladder.md
primitives/compact-result-schema/compact-result-schema.md
patterns/divide-and-conquer-audit/ccm-handoff.md
```

## Per iteration

Load: `patterns/live-state-refresh/preflight-checklist.md` (refresh)  
Then: `patterns/disposable-worker/disposable-worker.md` + issue acceptance criteria from GitHub.

## Stop

Load: `patterns/final-report/final-report-template.md`  
Load: `primitives/stop-blocker-decision-tree/stop-blocker-decision-tree.md`
