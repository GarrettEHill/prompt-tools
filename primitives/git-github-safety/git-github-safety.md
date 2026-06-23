# Git/GitHub Safety Baseline

Apply these rules in every coordinator and worker run unless a pattern explicitly defines a narrower exception.

## Always

- Start from clean current `main` unless remediating an existing PR branch.
- Run `git status` and respect unrelated local user changes.
- Use non-destructive git operations only.
- Merge through GitHub after validation passes.
- Sync `main` from origin after each merged PR.
- Refresh live state between sweep iterations.
- Verify branch protection and required checks before merging.

## Never

- `git push --force` to shared branches, especially `main`.
- Hard reset, rebase, or clean in ways that destroy unpushed or unshared user work.
- Skip hooks (`--no-verify`, `--no-gpg-sign`) unless the user or project policy explicitly requests it.
- Commit secrets, credentials, or tokens.
- Change production deployment settings as a side effect of unrelated work.
- Amend commits that were not created in the current run or that have been pushed.

## Existing PR exception

When remediating an open PR:

- work on the PR branch or an explicitly linked branch
- do not open a duplicate PR for the same item
- shared-branch safety rules still apply to `main` and other protected branches

## User-change conflict rule

Stop and report if the selected work item conflicts with unrelated local changes. Do not overwrite user work.

## Stop and ask

Stop the current item or sweep when:

- `gh auth status` fails
- unrelated uncommitted changes would be affected
- merge requires force-push
- branch protection blocks the intended merge path
- continuing would require secrets or production changes not in scope
