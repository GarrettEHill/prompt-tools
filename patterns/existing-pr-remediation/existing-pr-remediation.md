# Existing PR Remediation

Handle exactly one existing PR. Do not open a duplicate PR for the same item.

## PR inspection

- author (Dependabot, human, bot)
- base branch and mergeability
- conflicts
- required checks and current status
- review state and requested changes

## Remediation paths

- update dependency PR safely
- fix failing check on existing branch
- resolve merge conflicts minimally
- address review comments within scope
- close/supersede PR if obsolete

## Validation and merge

- follow the [validation ladder](../../primitives/validation-ladder/validation-ladder.md)
- re-run required checks
- do not merge with unrelated additions
- merge via GitHub when green

## When not to reuse the PR

- scope has drifted beyond the original item
- branch history is irreparable without force-push
- wrong base branch or abandoned branch
- duplicate PR already supersedes this one

## Return

Compact result with PR URL, action taken, checks, and merge status.

## Safety

Follow the [git/GitHub safety baseline](../../primitives/git-github-safety/git-github-safety.md), including the existing-PR exception.
