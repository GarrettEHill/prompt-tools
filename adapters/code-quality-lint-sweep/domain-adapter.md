## Domain Adapter: Code Quality / Lint Sweep

Repository/project:
- `<owner/repo>`

Goal:
- Resolve actionable linter and static-analysis findings in priority order.

Work queue discovery:
- linter CLI output (eslint, clippy, ruff, shellcheck, actionlint, etc.)
- pre-commit/CI annotations
- GitHub issues labeled lint/code-quality
- optional diff-scoped lint on changed modules

Selection order:
1. errors blocking CI
2. correctness/security-adjacent lint findings
3. high-volume simple fixes grouped by rule
4. cosmetic/style findings

A work item is concrete when:
- one rule + one module/directory per worker, or
- one CI-blocking lint error per worker

If an item is too broad:
- split by rule and directory
- route disputed findings to false-positive adjudication

Validation requirements:
- run the specific linter that produced the finding
- run repo-standard tests for affected module
- full workspace lint/test if project policy requires

Completion criteria:
- finding resolved with behavior preserved
- suppression only with narrow justification
- CI lint step green for affected scope

Special safety rules:
- no broad autoformat-only sweeps unless explicitly in scope
- no rule suppression to bypass failures without justification
- preserve project lint config conventions

Final report must include:
- rules/modules fixed
- suppressions with justification
- unresolved/blocking findings
