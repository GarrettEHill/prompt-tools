# Audit Domain Adapter Template

Append after [`divide-and-conquer-audit.md`](divide-and-conquer-audit.md).

```text
## Audit Domain Adapter: <project or audit name>

Repository/project:
- <owner/repo or path>

Audit goal:
- <e.g. full repository health audit before v2 release>

Scope discovery overrides:
- include domains: <list>
- exclude domains: <list with reason>
- Sonar mode: ingest-existing | supplement | full-audit

Tooling available:
- <sonar, cargo audit, gh api, etc.>

Evidence restrictions:
- <no prod access, no secret values in output, etc.>

Severity overrides:
- <project-specific critical/high definitions>

Label mapping:
- audit → <label>
- audit-finding → <label>
- domain labels: <security, ci-cd, ...>
- severity labels: <severity:critical, ...>

Issue creation:
- target repo: <owner/repo>
- assignees: <optional>
- milestone: <optional>

CCM repo for remediation:
- <owner/repo — usually same>

Report output paths:
- executive: <path or chat>
- detailed: <path or chat>
```

## Example: full repository audit

See [`adapters/full-repository-audit`](../../adapters/full-repository-audit/).
