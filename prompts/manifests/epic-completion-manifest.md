# Epic completion load manifest

Loaded by [`bootstrap-complete-epic.md`](../bootstrap-complete-epic.md).

## Bootstrap (load once)

```text
patterns/continuous-completion-model/continuous-completion-model.md
patterns/disposable-worker/disposable-worker.md
patterns/work-item-decomposition/work-item-decomposition.md
patterns/live-state-refresh/live-state-refresh.md
patterns/final-report/final-report-template.md
patterns/investigation-before-change/investigation-before-change.md
primitives/git-github-safety/git-github-safety.md
primitives/validation-ladder/validation-ladder.md
primitives/compact-result-schema/compact-result-schema.md
primitives/stop-blocker-decision-tree/stop-blocker-decision-tree.md
adapters/umbrella-issue-completion/domain-adapter.md
adapters/umbrella-issue-completion/notes.md
```

## Per iteration

Load: `patterns/live-state-refresh/preflight-checklist.md` (refresh)  
Then: `patterns/disposable-worker/disposable-worker.md` + live child issue / acceptance criteria from GitHub.

## Stop

Load: `patterns/final-report/final-report-template.md`  
Load: `primitives/stop-blocker-decision-tree/stop-blocker-decision-tree.md`
