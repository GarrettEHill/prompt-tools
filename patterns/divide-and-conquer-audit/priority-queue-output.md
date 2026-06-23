# Priority Queue Output

Phase 7: define remediation order for the Continuous Completion Model.

After all audit issues are filed, produce an ordered queue the CCM coordinator can consume.

## Priority rules

Order issues by:

1. **Severity** — critical → high → medium → low
2. **Exploitability / blast radius** — production path, auth, secrets, CI deploy
3. **Dependency unlock** — items that unblock other remediations
4. **Effort** — small safe fixes before large migrations when severity is equal
5. **Already partially started** — existing PRs or branches first

## Sonar and audit issue merge

When both Sonar-posted issues and new audit issues exist:

- dedupe by location + root cause
- prefer the issue with more context
- one queue entry per unique remediable problem

## Output: remediation queue

```yaml
remediation_queue:
  - rank: 1
    issue: 201
    finding_id: AUDIT-001
    title: "Scope GITHUB_TOKEN permissions in deploy workflow"
    severity: high
    domain: ci-cd
    rationale: "Deploy workflow; excessive permissions; high blast radius"
  - rank: 2
    issue: 198
    finding_id: AUDIT-004
    title: "cargo audit: CVE in transitive dep X"
    severity: high
    domain: dependency-supply-chain
    rationale: "Known CVE on production dependency path"
```

## Markdown form (for CCM handoff)

```markdown
## Remediation queue (priority order)

1. #201 — AUDIT-001 — Scope GITHUB_TOKEN permissions (high, ci-cd)
2. #198 — AUDIT-004 — CVE in transitive dep X (high, dependencies)
3. #205 — AUDIT-007 — README install command outdated (medium, docs)
```

## CCM discovery hook

The queue becomes the CCM **work queue discovery** input:

```text
Work queue discovery:
- Open issues labeled audit-finding, ordered by remediation_queue
- gh issue list --label audit-finding --state open
- Apply rank order from audit output; do not re-prioritize without cause
```

See [`ccm-handoff.md`](ccm-handoff.md).
