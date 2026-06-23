# Compact Auditor Result

Return to the audit coordinator after each section. One screenful max.

## Schema

```yaml
audit_section:
  domain: string
  status: completed | blocked | partial
summary: string
findings:
  - title: string
    severity: critical | high | medium | low | informational
    location: string
    evidence: string
    recommendation: string
    already_tracked: null | number
already_tracked_count: number
new_findings_count: number
checks_run:
  - cmd: string
    status: pass | fail | skipped
blocked:
  reason: null | string
follow_up: null | string
```

## Markdown form

```markdown
**Section:** dependency-supply-chain
**Status:** completed
**Summary:** 2 new high findings; 3 already tracked in #10, #11, #12.
**New findings:** 2 | **Already tracked:** 3
**Checks:** cargo audit (fail), cargo metadata (pass)
```

## Rules

- No raw scanner logs.
- List finding summaries; full detail goes in aggregation.
- Always report `already_tracked` vs `new` counts for Sonar overlap visibility.
