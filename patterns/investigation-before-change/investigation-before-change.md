# Investigation Before Change

Operate in read-only mode. No commits, branches, or PRs during investigation.

## Steps

1. **Reproduce or inspect** — failure, finding, or issue live.
2. **Collect evidence** — logs, annotations, comments, related commits, config.
3. **Identify scope** — affected modules and recent changes.
4. **Form hypothesis** — likely root cause category.
5. **Classify outcome** — see [`classification-outcomes.md`](classification-outcomes.md).
6. **Return compact investigation report** — use `status: investigate` in the compact result schema.

## Investigation report fields

- item id/title
- observed behavior
- evidence reviewed
- likely cause
- recommended next action
- suggested acceptance criteria if implementable
- blockers/follow-ups

## Safety

- no code changes
- no branch creation
- no PR open/merge
- no issue close unless proving duplicate/invalid with evidence

## Handoff

- ready to implement → disposable worker
- false positive → false-positive adjudication
- too broad → work-item decomposition
- blocked → coordinator with blocker note
