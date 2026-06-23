# Audit Finding Schema

## Single finding

```yaml
id: AUDIT-001              # assigned at aggregation; auditors use temp local ids
persona: ci-cd             # persona that produced the finding
domain: ci-cd              # audit domain tag
title: string
severity: critical | high | medium | low | informational
location: string           # file, module, workflow, package
evidence: string           # concise; link or excerpt
recommendation: string
already_tracked: null | number   # GitHub issue if exists
sonar_ref: null | string         # Sonar rule/issue if applicable
suggested_labels: [string]
suggested_issue_title: string
```

## Finding registry entry (post-aggregation)

```yaml
finding_registry:
  - id: AUDIT-001
    domain: dependency-supply-chain
    title: "Transitive dependency has known CVE"
    severity: high
    location: "Cargo.lock → crate-x"
    evidence: "cargo audit: RUSTSEC-2024-XXXX"
    recommendation: "Upgrade to >= 1.2.3"
    already_tracked: null
    issue_created: 201        # filled in issue-generation phase
```

## Severity definitions (default)

| Level | Meaning |
|-------|---------|
| critical | exploitable vulnerability, secret exposure, or prod outage risk |
| high | significant security/reliability gap with clear impact |
| medium | real issue with moderate impact or fix cost |
| low | minor hygiene, tech debt, non-urgent doc drift |
| informational | note only; issue creation optional per adapter |

## Deduplication keys

Treat as duplicate when:

- same `location` + same root cause
- same CVE or Sonar rule + same component
- existing open issue describes the same remediable problem
