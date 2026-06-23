# Prompt Tools

Reusable prompts and workflow patterns for Cursor, Codex-style agents, and GitHub-connected automation.

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

## Adapters

Task-specific plug-ins for the Continuous Completion Model.

- [`adapters/dependabot-pr-sweep`](adapters/dependabot-pr-sweep/)
- [`adapters/failing-ci-remediation`](adapters/failing-ci-remediation/)
- [`adapters/umbrella-issue-completion`](adapters/umbrella-issue-completion/)
- [`adapters/issue-label-normalization`](adapters/issue-label-normalization/)
- [`adapters/docs-backlog-cleanup`](adapters/docs-backlog-cleanup/)
- [`adapters/code-quality-lint-sweep`](adapters/code-quality-lint-sweep/)
- [`adapters/full-repository-audit`](adapters/full-repository-audit/) — comprehensive audit beyond SonarQube

## Auditors

Composable persona prompts that flavor `disposable-auditor`. **24 personas** in **8 classes** — assign 1–3 personas per run.

- [`auditors/`](auditors/) — catalog, composition, [`persona-classes`](auditors/persona-classes.md)
- Classes: `ingest`, `security`, `infrastructure`, `architecture`, `quality`, `contracts`, `safety-critical`, `compliance`

```text
disposable-auditor + [ci-cd, secrets-hygiene] → infrastructure/security workflow run
```

## Primitives

Shared rules and schemas used by multiple patterns.

- [`primitives/git-github-safety`](primitives/git-github-safety/) — non-negotiable git/GitHub rules
- [`primitives/validation-ladder`](primitives/validation-ladder/) — focused → repo-wide validation escalation
- [`primitives/compact-result-schema`](primitives/compact-result-schema/) — worker-to-coordinator return format
- [`primitives/stop-blocker-decision-tree`](primitives/stop-blocker-decision-tree/) — skip item vs stop sweep
- [`primitives/false-positive-adjudication`](primitives/false-positive-adjudication/) — fix vs suppress decisions
- [`primitives/audit-finding-schema`](primitives/audit-finding-schema/) — audit finding and auditor result format

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
| Class index | `auditors/classes/` | `security`, `infrastructure` |
| Adapter | `adapters/` | Dependabot sweep, full-repo audit |
| Primitive | `primitives/` | safety rules, validation ladder, result schema |
