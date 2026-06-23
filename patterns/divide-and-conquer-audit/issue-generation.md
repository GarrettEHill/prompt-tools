# Issue Generation

Phase 6: create GitHub issues from the detailed report.

Run this phase **after** aggregation and reporting. One issue per finding or tight finding group.

## Rules

- Create issues only for **new** findings (`already_tracked` → skip or comment on existing issue).
- One issue = one remediable unit of work (align with [`work-item-decomposition`](../work-item-decomposition/)).
- Every issue must have labels, acceptance criteria, and a link back to the audit report finding id.
- Do not create issues for `informational` findings unless the domain adapter says to.

## Issue body template

```markdown
## Summary
<finding title>

## Audit reference
- **Finding ID:** AUDIT-001
- **Domain:** ci-cd
- **Severity:** high
- **Report:** <link or path to detailed report>

## Evidence
<concise evidence>

## Recommendation
<what should change>

## Acceptance criteria
- [ ] <measurable outcome>
- [ ] validation: <commands/checks>

## Context
- **Location:** `path/to/file`
- **Related issues:** #N (if any)
```

## Label strategy

Use consistent labels for CCM queue discovery.

| Label | Purpose |
|-------|---------|
| `audit` | all audit-generated issues |
| `audit-finding` | specific remediable finding |
| `<domain>` | e.g. `security`, `ci-cd`, `dependencies`, `docs` |
| `severity:critical` / `high` / `medium` / `low` | priority input |
| `source:sonar` | ingested from Sonar (optional) |

Create labels if missing:

```bash
gh label create audit --description "From divide-and-conquer audit" --color "5319E7"
gh label create audit-finding --description "Remediable audit finding" --color "BFD4F2"
```

## Create issues

```bash
gh issue create \
  --title "[AUDIT-001] Scope GITHUB_TOKEN permissions in deploy workflow" \
  --label "audit,audit-finding,ci-cd,severity:high" \
  --body-file issue-body.md
```

Record created issues:

```yaml
issues_created:
  - finding_id: AUDIT-001
    issue: 201
    url: https://github.com/org/repo/issues/201
```

## Dedup guard

Before creating:

```bash
gh issue list --state open --search "AUDIT-001 OR <key phrase>"
```

If duplicate exists, link finding to existing issue instead.

## Do not

- create umbrella issues without child criteria
- bundle unrelated findings into one issue
- create issues for findings already tracked unless adding new evidence
