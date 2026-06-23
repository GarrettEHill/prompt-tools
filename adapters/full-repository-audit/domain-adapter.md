## Audit Domain Adapter: Full Repository Audit

Repository/project:
- `<owner/repo>`

Audit goal:
- Identify security, reliability, maintainability, and operational gaps across the repository; file prioritized GitHub issues for remediation via CCM.

Scope discovery overrides:
- use persona run plan from `audit-domains.md`
- Sonar via `static-analysis-ingest` persona only (ingest-existing)

Persona assignment:
- select by **class** and/or persona name — see `auditors/persona-classes.md`
- default run plan in `audit-domains.md`; expand for Xyberus, robotics, MCP, monorepo per `persona-catalog.md` project shortcuts

Tooling available:
- SonarQube/SonarCloud via GitHub issues and checks
- `gh` CLI for issues, PRs, workflows, Dependabot
- language-native tools: `cargo audit`, `npm audit`, `osv-scanner`, `actionlint`, `shellcheck`, `gitleaks` (read-only)
- repo test/lint commands (read-only)

Evidence restrictions:
- do not print secret values
- no production environment access unless explicitly granted
- do not modify code during audit phases

Severity overrides:
- critical: exploitable CVE on prod path, exposed secret, deploy workflow with excessive permissions
- high: missing auth check, failing required CI on main, known CVE without fix
- medium: doc/command drift, missing tests on critical path, outdated non-CVE deps
- low: style-level hygiene not caught by Sonar

Label mapping:
- `audit`, `audit-finding`
- domain: `security`, `dependencies`, `ci-cd`, `testing`, `documentation`, `architecture`
- severity: `severity:critical`, `severity:high`, `severity:medium`, `severity:low`
- `source:sonar` for ingested Sonar findings

Issue creation:
- target repo: same as audit target
- one issue per AUDIT-XXX finding unless tightly coupled

CCM repo for remediation:
- same as audit target

Report output paths:
- `docs/audits/YYYY-MM-DD-executive.md`
- `docs/audits/YYYY-MM-DD-detailed.md`
- or chat output if docs path not used

Remediation queue:
- output `priority-queue-output.md` block after issue creation
- paste into `ccm-handoff.md` for next prompt
