## Domain Adapter: Dependabot PR Sweep

Repository/project:
- `<owner/repo>`

Goal:
- Review, validate, and merge or remediate all actionable open Dependabot PRs.

Work queue discovery:
- `gh pr list --author app/dependabot --state open`
- filter by mergeability, failing checks, draft status, and labels
- identify obsolete or superseded dependency PRs

Selection order:
1. security updates
2. patch/minor updates with green or fixable checks
3. major updates with focused failures
4. conflict-only PRs after simpler ones are merged

A work item is concrete when:
- one Dependabot PR per worker unless policy defines safe grouping by dependency + target

If an item is too broad:
- do not batch unrelated dependency families
- select the smallest mergeable PR first
- leave major bumps blocked with documented migration needs

Validation requirements:
- repo-standard test/lint/build commands
- required GitHub checks
- lockfile/manifest consistency checks where applicable

Completion criteria:
- PR merged after validation, or
- closed with documented reason (superseded, breaking, blocked), or
- left open with blocker note

Special safety rules:
- no unrelated refactors on Dependabot branches
- prefer updating the existing PR branch over opening a new PR
- do not change secrets or deploy config unless the dependency update requires it

Final report must include:
- merged Dependabot PR count
- blocked major bumps
- superseded/closed PRs
- repeated CI failure patterns
