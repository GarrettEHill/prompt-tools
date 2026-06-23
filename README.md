# Prompt Tools

Reusable prompts and workflow patterns for Cursor, Codex-style agents, and GitHub-connected automation.

## Patterns

Orchestration loops and workflow units.

- [`patterns/continuous-completion-model`](patterns/continuous-completion-model/) — coordinator + disposable worker loop for item-by-item sweeps
- [`patterns/disposable-worker`](patterns/disposable-worker/) — handle one work item in isolation
- [`patterns/work-item-decomposition`](patterns/work-item-decomposition/) — split broad goals into worker-sized items
- [`patterns/live-state-refresh`](patterns/live-state-refresh/) — preflight checklist before acting
- [`patterns/investigation-before-change`](patterns/investigation-before-change/) — read-only pass for ambiguous items
- [`patterns/existing-pr-remediation`](patterns/existing-pr-remediation/) — fix open PRs without duplicates
- [`patterns/final-report`](patterns/final-report/) — standardized end-of-sweep report

## Adapters

Task-specific plug-ins for the Continuous Completion Model.

- [`adapters/dependabot-pr-sweep`](adapters/dependabot-pr-sweep/)
- [`adapters/failing-ci-remediation`](adapters/failing-ci-remediation/)
- [`adapters/umbrella-issue-completion`](adapters/umbrella-issue-completion/)
- [`adapters/issue-label-normalization`](adapters/issue-label-normalization/)
- [`adapters/docs-backlog-cleanup`](adapters/docs-backlog-cleanup/)
- [`adapters/code-quality-lint-sweep`](adapters/code-quality-lint-sweep/)

## Primitives

Shared rules and schemas used by multiple patterns.

- [`primitives/git-github-safety`](primitives/git-github-safety/) — non-negotiable git/GitHub rules
- [`primitives/validation-ladder`](primitives/validation-ladder/) — focused → repo-wide validation escalation
- [`primitives/compact-result-schema`](primitives/compact-result-schema/) — worker-to-coordinator return format
- [`primitives/stop-blocker-decision-tree`](primitives/stop-blocker-decision-tree/) — skip item vs stop sweep
- [`primitives/false-positive-adjudication`](primitives/false-positive-adjudication/) — fix vs suppress decisions

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
| Pattern | `patterns/` | coordinator loop, worker unit, investigation flow |
| Adapter | `adapters/` | Dependabot sweep, Sonar cleanup |
| Primitive | `primitives/` | safety rules, validation ladder, result schema |
