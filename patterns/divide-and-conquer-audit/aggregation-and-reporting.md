# Aggregation and Reporting

Phases 4–5: merge auditor results, deduplicate, and produce executive + detailed reports.

## Aggregation

After all audit sections complete (or are marked blocked):

1. Collect all compact auditor results.
2. Merge into a **finding registry** — single list of unique findings.
3. Deduplicate:
   - same file + same root cause → one finding
   - finding already tracked as GitHub issue #N → `already_tracked: #N`
   - Sonar finding with existing issue → link, do not duplicate
4. Normalize severity across domains.
5. Record blocked audit sections separately.

### Finding registry schema

See [`audit-finding-schema.md`](../../primitives/audit-finding-schema/audit-finding-schema.md).

```yaml
finding_registry:
  - id: AUDIT-001          # stable id for issue creation
    domain: ci-cd
    title: "Workflow uses excessive GITHUB_TOKEN permissions"
    severity: high
    location: .github/workflows/deploy.yml
    evidence: "permissions: write-all at line 12"
    recommendation: "Scope to contents:read and least-privilege writes"
  already_tracked:
    - issue: 42
      reason: "Sonar hotspot already filed"
  audit_blocked:
    - domain: license-compliance
      reason: "No license scanner available"
```

## Executive report (high level)

Audience: maintainers needing a quick health picture.

```markdown
# Audit Executive Summary

**Repository:** <owner/repo>
**Audit date:** <date>
**Domains audited:** <count> | **Blocked:** <count>

## Overall posture
<2-4 sentences>

## By severity
| Severity | New | Already tracked | Total |
|----------|-----|-----------------|-------|
| critical | | | |
| high     | | | |
| medium   | | | |
| low      | | | |

## Top risks (max 5)
1. ...
2. ...

## Domains needing attention
- ...

## Recommended next steps
1. Remediate critical/high via CCM
2. ...
```

Keep to one screen. No per-finding detail.

## Detailed report (actionable)

Audience: issue creation and remediation workers.

```markdown
# Audit Detailed Report

**Repository:** <owner/repo>
**Finding registry version:** 1

## Findings

### AUDIT-001 — <title>
- **Domain:** ci-cd
- **Severity:** high
- **Location:** `.github/workflows/deploy.yml`
- **Evidence:** ...
- **Recommendation:** ...
- **Already tracked:** no | #42
- **Suggested labels:** audit, security, ci-cd, priority:high
- **Suggested issue title:** ...

### AUDIT-002 — ...

## Blocked audit sections
- ...

## Duplicates suppressed
- AUDIT-00X merged into AUDIT-00Y because ...
```

Every new finding must have enough detail to become a GitHub issue without re-auditing.

## Output location

Write reports to a durable location if the project uses audit artifacts, e.g.:

- `docs/audits/YYYY-MM-DD-executive.md`
- `docs/audits/YYYY-MM-DD-detailed.md`

Or return in chat if no repo write is desired before issue creation.
