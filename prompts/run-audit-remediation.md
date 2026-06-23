# Run Audit Remediation

**Use after** [`run-repository-audit.md`](run-repository-audit.md) has filed issues.

Paste into Cursor on the same repository to remediate `audit-finding` issues using the Continuous Completion Model.

Reference: [GarrettEHill/prompt-tools](https://github.com/GarrettEHill/prompt-tools)

---

## Configuration

```text
Repository: <owner/repo>
Paste CCM handoff block from audit output below.
```

## CCM Handoff

```text
(paste remediation_queue and handoff block from audit run)
```

---

## Your role

You are the **remediation coordinator** (Continuous Completion Model).

Process audit issues **one at a time** until the queue is complete, blocked, or stop rules fire. Do not stop after one issue.

Load from prompt-tools:

```text
patterns/continuous-completion-model/continuous-completion-model.md
patterns/disposable-worker/disposable-worker.md
patterns/live-state-refresh/live-state-refresh.md
patterns/final-report/final-report-template.md
primitives/git-github-safety/git-github-safety.md
primitives/validation-ladder/validation-ladder.md
primitives/compact-result-schema/compact-result-schema.md
```

## Per issue

1. Refresh live state
2. Select next issue from remediation queue
3. Implement smallest complete fix
4. Validate (validation ladder)
5. Open PR referencing `AUDIT-XXX`
6. Merge via GitHub when green
7. Close issue with brief resolution note
8. Keep compact coordinator note; continue

## Safety

- respect git-github-safety baseline
- do not close audit issues without merged fix or documented false-positive
- max 3 fix attempts per issue; 3 failed items → stop sweep and final report

**Begin with live state refresh and the first queued audit-finding issue.**
