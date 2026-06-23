# CCM Handoff

Phase 8: feed prioritized audit issues into the Continuous Completion Model for remediation.

## Pipeline

```text
divide-and-conquer-audit  →  issues + priority queue  →  continuous-completion-model
```

Audit identifies and documents. CCM fixes, validates, merges, and closes.

## Handoff block

Paste after audit completes. Fill from audit outputs.

```text
## CCM Handoff: Audit remediation

Repository/project:
- <owner/repo>

Goal:
- Remediate all open audit-finding issues in priority order until complete or blocked.

Work queue discovery:
- Open issues with label `audit-finding`
- Priority order:
  1. #201 — AUDIT-001 — <title>
  2. #198 — AUDIT-004 — <title>
  3. ...
- Also include existing Sonar issues if not duplicated by audit issues

Selection order:
1. critical severity
2. high severity
3. medium severity
4. low severity
5. within tier: follow remediation_queue rank

A work item is concrete when:
- one audit-finding issue or one Sonar issue per worker

Validation requirements:
- per-issue acceptance criteria in issue body
- repo-standard lint/test/build
- re-run audit check or scanner where applicable

Completion criteria:
- acceptance criteria met
- PR merged via GitHub
- audit-finding issue closed with brief resolution note

Special safety rules:
- do not close audit issues without merged fix or documented false-positive
- reference AUDIT-XXX id in PR body
- for Sonar-sourced issues, wait for quality gate if available

Final report must include:
- audit issues closed vs remaining
- findings marked false-positive with justification
```

## Full remediation prompt composition

```text
live-state-refresh
+ continuous-completion-model
+ disposable-worker
+ git-github-safety
+ validation-ladder
+ compact-result-schema
+ <CCM handoff block above>
+ final-report
```

## Closing the loop

Optional: after CCM sweep, re-run targeted audit domains to verify findings are resolved. Do not re-audit everything — only domains whose issues were closed.
