# Disposable Worker

Handle exactly one selected work item. Do not pick the next item.

## Scope lock

- One work item only.
- Do not continue to unrelated items.
- Do not expand scope beyond acceptance criteria.

## Steps

1. **Inspect live** — re-read the issue, PR, check, or finding before acting.
2. **Confirm acceptance criteria** — define what "done" means for this item.
3. **Identify scope** — affected files, modules, and tests.
4. **Implement** — smallest complete fix; no unrelated refactors.
5. **Test** — add or update focused tests/proofs when appropriate.
6. **Validate** — follow the [validation ladder](../../primitives/validation-ladder/validation-ladder.md).
7. **Retry** — up to 3 fix attempts after failed validation.
8. **PR** — open or update a PR if the item is resolved.
9. **Merge** — only after validation passes and the PR is mergeable via GitHub.
10. **Close/update tracking** — close or update the work item only if merged work fully satisfies it.
11. **Return compact result** — use the [compact result schema](../../primitives/compact-result-schema/compact-result-schema.md).

## Safety

Follow the [git/GitHub safety baseline](../../primitives/git-github-safety/git-github-safety.md).

## Retry

A fix attempt means a code/config/test/workflow change after failed validation.

If the item still fails after 3 attempts:

- leave it unresolved
- do not merge
- document the blocker
- return `status: blocked` or `status: failed`

## Return format

Return only the compact result. No full diffs, long logs, or implementation narrative.
