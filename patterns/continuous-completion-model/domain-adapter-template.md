# Domain Adapter Template

Append this after the Continuous Completion Model.

```text
## Domain Adapter: <task name>

Repository/project:
- <owner/repo or project path>

Goal:
- <what should be completed>

Work queue discovery:
- <how to find items>
- Examples:
  - open Dependabot PRs
  - SonarQube findings posted on GitHub
  - child issues under umbrella issue #123
  - failing GitHub Actions jobs
  - issues with missing labels

Selection order:
1. <highest priority item type>
2. <next priority>
3. <fallback priority>

A work item is concrete when:
- <conditions that make it small enough for one worker>

If an item is too broad:
- create/link child items with acceptance criteria
- select the smallest unblocked child
- do not close the parent until all children and acceptance criteria are complete

Validation requirements:
- <commands/checks required before merge/close>
- Examples:
  - cargo fmt --check
  - cargo test --workspace --locked
  - cargo clippy --workspace --all-targets --all-features -- -D warnings
  - docker compose config
  - actionlint
  - shellcheck
  - npm test
  - Sonar quality gate
  - GitHub checks

Completion criteria:
- <what proves the item is done>
- <what allows the PR to merge>
- <what allows the issue/finding to close>

Special safety rules:
- <project-specific rules>
- Do not change secrets, credentials, production deploy settings, or unrelated infrastructure.
- Do not make broad unrelated refactors.
- Do not suppress findings unless they are objectively false-positive and justified.

Final report must include:
- <domain-specific details>
```

## Example: SonarQube Cleanup

```text
## Domain Adapter: SonarQube/SonarCloud Cleanup

Repository/project:
- GarrettEHill/Xyberus

Goal:
- Review, fix, validate, and close all actionable SonarQube/SonarCloud issues posted on the project.

Work queue discovery:
- Search open GitHub issues for sonar, sonarqube, sonarcloud, code-quality, quality gate, vulnerability, security hotspot, bug, code smell, duplication, and coverage.
- Check PR comments, GitHub checks, Actions logs, and local scanner configuration.
- If Sonar API access is unavailable, use GitHub-posted Sonar issues/checks/annotations as the source of truth.

Selection order:
1. Vulnerabilities and true security hotspots
2. Bugs/reliability findings
3. Critical/blocker severity findings
4. Major maintainability findings
5. Duplication findings with a safe extraction path
6. Minor/code-style findings
7. Coverage-only findings

Validation requirements:
- Run focused tests for the affected module.
- Run repo-standard lint/static checks.
- Run Sonar scanner or wait for Sonar/GitHub quality gate if available.
- Do not merge based only on inspection.

Completion criteria:
- Finding is fixed, proven false-positive with narrow justification, or blocked with documented reason.
- PR passes required validation and GitHub/Sonar checks where available.
- Related GitHub issue is closed only after merged work fully resolves it.
```
