## Domain Adapter: Umbrella Issue Completion

Repository/project:
- `<owner/repo>`

Goal:
- Complete all child work under a parent/umbrella issue and close the parent only when fully satisfied.

Work queue discovery:
- parent umbrella issue body/checklist
- linked child issues, sub-issues, and task lists
- open PRs referencing parent/children
- missing children for unchecked umbrella criteria

Selection order:
1. unblocked children that unlock other children
2. highest severity/acceptance-critical children
3. children with existing partial PRs
4. net-new children after decomposition

A work item is concrete when:
- one child issue or one clearly scoped acceptance criterion
- if no children exist, decomposition is required before implementation

If an item is too broad:
- create child issues with acceptance criteria
- select the smallest unblocked child
- do not close the parent until all children are complete

Validation requirements:
- child-specific tests/checks
- umbrella-level validation before parent close (integration/e2e if defined)

Completion criteria:
- child closed only when acceptance criteria met and work merged/proven
- parent closed only when all children and umbrella criteria are satisfied
- parent updated with compact progress notes after each child

Special safety rules:
- do not close parent for partial completion
- do not bundle unrelated children into one PR
- link PRs to child issues; reference parent in PR body

Final report must include:
- children completed vs remaining
- parent status
- newly created child issues
- blockers on critical path
