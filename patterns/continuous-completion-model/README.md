# Continuous Completion Model

This pattern is for Cursor prompts where you want the agent to keep working through a queue of tasks without manual intervention.

It is useful for workflows like:

- open Dependabot PR sweeps — [`adapters/dependabot-pr-sweep`](../../adapters/dependabot-pr-sweep/)
- SonarQube/SonarCloud cleanup — see [`domain-adapter-template.md`](domain-adapter-template.md)
- GitHub issue umbrella completion — [`adapters/umbrella-issue-completion`](../../adapters/umbrella-issue-completion/)
- failing CI job remediation — [`adapters/failing-ci-remediation`](../../adapters/failing-ci-remediation/)
- issue label normalization — [`adapters/issue-label-normalization`](../../adapters/issue-label-normalization/)
- documentation backlog cleanup — [`adapters/docs-backlog-cleanup`](../../adapters/docs-backlog-cleanup/)
- repeated code quality fixes — [`adapters/code-quality-lint-sweep`](../../adapters/code-quality-lint-sweep/)

## Files

- [`continuous-completion-model.md`](continuous-completion-model.md) — the reusable control loop.
- [`domain-adapter-template.md`](domain-adapter-template.md) — the small task-specific section to append after the control loop.

## Related patterns

- [`disposable-worker`](../disposable-worker/) — extracted worker unit
- [`work-item-decomposition`](../work-item-decomposition/) — split broad items before queueing
- [`live-state-refresh`](../live-state-refresh/) — preflight and between-iteration refresh
- [`investigation-before-change`](../investigation-before-change/) — read-only pass for ambiguous items
- [`existing-pr-remediation`](../existing-pr-remediation/) — PR-native remediation
- [`final-report`](../final-report/) — end-of-sweep report template

## Upstream: audit handoff

Audit-generated issues feed this pattern via [`divide-and-conquer-audit/ccm-handoff`](../divide-and-conquer-audit/ccm-handoff.md).

## Related primitives

- [`git-github-safety`](../../primitives/git-github-safety/)
- [`validation-ladder`](../../primitives/validation-ladder/)
- [`compact-result-schema`](../../primitives/compact-result-schema/)
- [`stop-blocker-decision-tree`](../../primitives/stop-blocker-decision-tree/)
- [`false-positive-adjudication`](../../primitives/false-positive-adjudication/)

## How to use

1. Paste `continuous-completion-model.md` at the top of your Cursor prompt.
2. Fill out the domain adapter or use a ready-made adapter from `adapters/`.
3. Add any project-specific safety rules.
4. Run from a clean repo state.

The main idea is:

> The main agent coordinates. Each concrete work item is handled by a fresh disposable worker/subagent. After each item, only a compact result is kept, live state is refreshed, and the next item is selected.
