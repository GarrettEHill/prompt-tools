# Prompt Tools

Reusable prompts and workflow patterns for Cursor, Codex-style agents, and GitHub-connected automation.

## Primary use case — audit any repo from Cursor

**You do not add prompt-tools to the project you are auditing.** Open that repo in Cursor, paste a short snippet, and the agent fetches the **latest instructions from `main`** at run time.

Save this and reuse it — only change `repo` and flags:

```text
Run a divide-and-conquer repo audit (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-audit.md

Target: this workspace
repo: <owner/repo>
sonar: yes
create_issues: yes
reports: chat-only
```

| | |
|---|---|
| **You paste** | ~6 lines (snippet above) |
| **Agent fetches** | `bootstrap-*.md` → manifest → patterns, personas, schemas |
| **Target repo** | unchanged — no files copied in |
| **Updates** | push to `main` here → next run uses new behavior automatically |

After audit issues exist, remediate with:

```text
Remediate audit findings (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-remediate.md

Target: this workspace
repo: <owner/repo>
```

### Complete an issue epic (CCM sweep)

Paste this on **any repo** with a parent/umbrella GitHub issue. The coordinator works through child issues **one at a time** with fresh disposable workers until the epic is done or blocked:

```text
Complete issue epic (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-complete-epic.md

Target: this workspace
repo: <owner/repo>
epic: <issue-number>
```

More snippets: [`prompts/SNIPPET.md`](prompts/SNIPPET.md) — audit, remediate, epic, map, review PR, ship

### Other remote workflows

| Workflow | Bootstrap URL |
|----------|----------------|
| Complete epic | `prompts/bootstrap-complete-epic.md` |
| Map repo | `prompts/bootstrap-map-archaeology.md` |
| Onboarding brief | `prompts/bootstrap-map-onboarding.md` |
| Review PR | `prompts/bootstrap-review-pr.md` |
| Ship release | `prompts/bootstrap-ship-release.md` |
| Ship checklist | `prompts/bootstrap-ship-checklist.md` |
| Rollback plan | `prompts/bootstrap-ship-rollback.md` |

Full library roadmap: [#64](https://github.com/GarrettEHill/prompt-tools/issues/64) · [`docs/WORKFLOW_ROADMAP.md`](docs/WORKFLOW_ROADMAP.md)

### What the audit run does

1. Discovers scope and builds an audit plan (personas by class)
2. Runs read-only disposable auditors section by section
3. Aggregates findings → executive + detailed reports
4. Creates labeled GitHub issues (optional)
5. Outputs a prioritized queue + handoff for remediation (CCM)

SonarQube is ingested where present; this system covers CI, deps, secrets, infra, contracts, and more.

### What the epic run does

1. Loads the parent issue and discovers child issues, checklists, and linked tasks
2. Decomposes any broad umbrella criteria into worker-sized child issues
3. Runs the CCM coordinator loop — one fresh disposable worker per item
4. Opens PRs, validates, merges, and closes children as each completes
5. Updates the parent with progress notes; closes the epic only when fully satisfied
6. Stops with a final report when complete, blocked, or stop rules trigger

## Quick start

1. Open the **target repo** in Cursor.
2. Paste a snippet from above (or [`prompts/SNIPPET.md`](prompts/SNIPPET.md)) — audit, remediate, or epic completion.
3. Let the agent run — it pulls everything else from this repo on GitHub.
4. For audit → remediate flows, paste the remediate snippet after issues exist.

## Patterns

Orchestration loops and workflow units.

- [`patterns/continuous-completion-model`](patterns/continuous-completion-model/) — coordinator + disposable worker loop for item-by-item sweeps
- [`patterns/disposable-worker`](patterns/disposable-worker/) — handle one work item in isolation
- [`patterns/disposable-auditor`](patterns/disposable-auditor/) — read-only audit shell; flavor with personas
- [`patterns/work-item-decomposition`](patterns/work-item-decomposition/) — split broad goals into worker-sized items
- [`patterns/live-state-refresh`](patterns/live-state-refresh/) — preflight checklist before acting
- [`patterns/investigation-before-change`](patterns/investigation-before-change/) — read-only pass for ambiguous items
- [`patterns/existing-pr-remediation`](patterns/existing-pr-remediation/) — fix open PRs without duplicates
- [`patterns/final-report`](patterns/final-report/) — standardized end-of-sweep report
- [`patterns/divide-and-conquer-audit`](patterns/divide-and-conquer-audit/) — discover, plan, audit, report, file issues, prioritize for CCM
- [`patterns/repo-archaeology`](patterns/repo-archaeology/) — read-only repo map before audit or change
- [`patterns/onboarding-brief`](patterns/onboarding-brief/) — onboarding brief generator
- [`patterns/decision-archaeology`](patterns/decision-archaeology/) — decision register
- [`patterns/blast-radius`](patterns/blast-radius/) — change impact map
- [`patterns/pr-review`](patterns/pr-review/) — composable PR review personas
- [`patterns/release-coordinator`](patterns/release-coordinator/) — version-cut coordinator + release slices
- [`patterns/ship-checklist`](patterns/ship-checklist/) — release gate evaluation
- [`patterns/rollback-plan`](patterns/rollback-plan/) — read-only rollback plan generator

## Adapters

Task-specific plug-ins for the Continuous Completion Model.

- [`adapters/dependabot-pr-sweep`](adapters/dependabot-pr-sweep/)
- [`adapters/failing-ci-remediation`](adapters/failing-ci-remediation/)
- [`adapters/umbrella-issue-completion`](adapters/umbrella-issue-completion/)
- [`adapters/issue-label-normalization`](adapters/issue-label-normalization/)
- [`adapters/docs-backlog-cleanup`](adapters/docs-backlog-cleanup/)
- [`adapters/code-quality-lint-sweep`](adapters/code-quality-lint-sweep/)
- [`adapters/full-repository-audit`](adapters/full-repository-audit/) — comprehensive audit beyond SonarQube
- [`adapters/semver-release`](adapters/semver-release/) — release readiness and version-cut assembly

## Auditors

Composable persona prompts that flavor `disposable-auditor`. **24 personas** in **8 classes** — assign 1–3 personas per run.

- [`auditors/`](auditors/) — catalog, composition, [`persona-classes`](auditors/persona-classes.md)
- Classes: `ingest`, `security`, `infrastructure`, `architecture`, `quality`, `contracts`, `safety-critical`, `compliance`

```text
disposable-auditor + [ci-cd, secrets-hygiene] → infrastructure/security workflow run
```

## Mappers & reviewers

- [`mappers/`](mappers/) — map workflow specialists (api-surface, data-flow, deploy-topology)
- [`reviewers/`](reviewers/) — PR review personas (security, api-compat, tests, design, deps)

## Primitives

Shared rules and schemas used by multiple patterns.

- [`primitives/git-github-safety`](primitives/git-github-safety/) — non-negotiable git/GitHub rules
- [`primitives/validation-ladder`](primitives/validation-ladder/) — focused → repo-wide validation escalation
- [`primitives/compact-result-schema`](primitives/compact-result-schema/) — worker-to-coordinator return format
- [`primitives/stop-blocker-decision-tree`](primitives/stop-blocker-decision-tree/) — skip item vs stop sweep
- [`primitives/false-positive-adjudication`](primitives/false-positive-adjudication/) — fix vs suppress decisions
- [`primitives/audit-finding-schema`](primitives/audit-finding-schema/) — audit finding and auditor result format
- [`primitives/map-result-schema`](primitives/map-result-schema/) — map workflow output
- [`primitives/decision-record-schema`](primitives/decision-record-schema/) — decision register
- [`primitives/review-result-schema`](primitives/review-result-schema/) — PR review output
- [`primitives/ship-gate-schema`](primitives/ship-gate-schema/) — release go/no-go gate output

## Audit → remediate pipeline

```text
live-state-refresh
+ divide-and-conquer-audit
+ disposable-auditor
+ auditors/<persona> (+ optional personas)
+ audit-finding-schema
+ full-repository-audit (or custom adapter)
  → executive + detailed reports
  → GitHub issues with labels
  → priority queue
+ ccm-handoff
+ continuous-completion-model
+ disposable-worker
  → fix, validate, merge, close
```

SonarQube covers static analysis well. The audit pattern identifies **what else to inspect**, plans **how** each section is audited, aggregates results, files issues, and outputs a prioritized queue for remediation.

## How to compose

```text
live-state-refresh
+ continuous-completion-model
+ disposable-worker
+ git-github-safety
+ validation-ladder
+ compact-result-schema
+ <domain adapter>
+ final-report
```

1. Paste [`continuous-completion-model.md`](patterns/continuous-completion-model/continuous-completion-model.md) at the top of your prompt.
2. Add primitives and patterns as needed.
3. Append a domain adapter (or fill out [`domain-adapter-template.md`](patterns/continuous-completion-model/domain-adapter-template.md)).
4. Run from a clean repo state.

## Intended use

Copy the continuous completion model into the top of a task-specific prompt, then add a short domain adapter describing:

- how to discover the work queue
- how to order the queue
- what validation is required
- what counts as complete
- when to stop

This keeps long-running prompts consistent without rewriting the whole control loop each time.

## Where new prompts belong

| Type | Put it here | Example |
|------|-------------|---------|
| Pattern | `patterns/` | coordinator loop, worker unit, auditor shell |
| Persona | `auditors/<name>/` | `ci-cd`, `mcp-server-safety` |
| Mapper | `mappers/<name>/` | `api-surface-mapper` |
| Reviewer | `reviewers/<name>/` | `security-reviewer` |
| Class index | `auditors/classes/` | `security`, `infrastructure` |
| Adapter | `adapters/` | Dependabot sweep, full-repo audit |
| Operational prompt | `prompts/` | [`SNIPPET.md`](prompts/SNIPPET.md), `bootstrap-audit.md` |
| Primitive | `primitives/` | safety rules, validation ladder, result schema |
