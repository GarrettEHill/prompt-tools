## Audit Domain Adapter: Full Repository Audit

Repository/project:
- `<owner/repo>`

Audit goal:
- Identify security, reliability, maintainability, and operational gaps across the repository; file prioritized GitHub issues for remediation via CCM.

Scope discovery overrides:
- include: dependency-supply-chain, secrets-hygiene, ci-cd, test-quality, documentation-accuracy, architecture-boundaries, error-handling-observability, configuration-drift
- include: static-analysis in **ingest-existing** mode when SonarQube/SonarCloud is active
- exclude: performance-hotspots unless adapter extended — skip with reason if not applicable
- exclude: license-compliance if no scanner available — mark audit-blocked

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
