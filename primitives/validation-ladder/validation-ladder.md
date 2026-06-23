# Validation Ladder

Escalate validation from focused proof to repo-wide gates. Do not merge until the project-required level is satisfied.

## Levels

### Level 1 — Targeted proof

Run the command closest to the changed code:

- single test file or test name
- focused lint on changed files
- module-scoped check

### Level 2 — Affected module/package

Run the suite or scripts for the affected module, package, or service.

### Level 3 — Repo standard

Run project-required commands, for example:

- full workspace test
- workspace lint/format check
- build or typecheck
- `docker compose config`
- `actionlint` / `shellcheck`

### Level 4 — External gate

Wait for or verify external gates:

- GitHub required checks
- Sonar quality gate
- deploy preview / integration environment checks

## Rules

- Do not skip levels unless the project policy or domain adapter explicitly allows it.
- Do not merge after level 1 only when policy requires level 3 or higher.
- Record every command run and its outcome in the compact worker result.
- If level 3 fails globally and the change is unrelated, classify as a baseline blocker and stop the sweep.
- Prefer local reproduction before waiting on CI when feasible.

## Merge prerequisites

Merge only when:

- required ladder levels pass
- PR is mergeable
- branch protection is satisfied
- no unrelated failures were introduced
