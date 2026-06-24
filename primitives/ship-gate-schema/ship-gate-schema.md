# Ship Gate Schema

Release-readiness gate output. Used by ship-checklist and release-coordinator.

## Schema

```yaml
release:
  version: string | null          # target semver, e.g. 1.2.0
  repo: string
  base_ref: string                # branch or tag being released from
  candidate_sha: string | null
verdict: ship | no-ship | blocked
summary: string                   # one-line go/no-go
gates:
  - id: string                    # stable gate id, e.g. ci-green
    name: string
    status: pass | fail | blocked | skipped
    evidence: string              # command output, URL, or issue refs
    blocker: string | null
required_gates_failed: [string]
optional_gates_failed: [string]
blockers:
  - type: issue | check | audit-finding | migration | docs | manual
    ref: string                   # #123, workflow/job, AUDIT-001
    reason: string
handoff:
  ccm_queue: [string]             # issue ids to route to remediation
  recommended_action: string | null
checks_run:
  - cmd: string
    status: pass | fail | skipped
```

## Markdown form

```markdown
**Release:** v1.2.0 from main @ abc1234
**Verdict:** no-ship
**Summary:** Required CI failing; 2 open audit-finding issues.

| Gate | Status | Evidence |
|------|--------|----------|
| ci-green | fail | preflight job failed |
| audit-clear | fail | #819, #820 open |
| changelog | pass | CHANGELOG.md updated |

**Blockers:** #819, preflight failure
**Handoff:** remediate audit-finding queue via CCM
```

## Rules

- `verdict: ship` only when all **required** gates are `pass`.
- `blocked` means cannot determine (auth, missing tooling, ambiguous policy).
- Coordinator keeps only this payload between release-worker iterations.
- Do not mark `ship` with skipped required gates unless project policy explicitly allows.
