# Umbrella Issue Composer

Proactive planning: compose umbrella epics with decomposed child issues.

Related: [`umbrella-issue-completion`](../../adapters/umbrella-issue-completion/domain-adapter.md) (execution).

## Loop

1. Load goal and acceptance criteria from user
2. Decompose via [`work-item-decomposition`](../work-item-decomposition/work-item-decomposition.md)
3. Draft umbrella body + child stubs per [`child-issue-template.md`](child-issue-template.md)
4. Optional: `gh issue create` batch with labels (user approves)

## Output

Umbrella issue body + child issue stubs each with acceptance criteria.
