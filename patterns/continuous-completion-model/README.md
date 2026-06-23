# Continuous Completion Model

This pattern is for Cursor prompts where you want the agent to keep working through a queue of tasks without manual intervention.

It is useful for workflows like:

- open Dependabot PR sweeps
- SonarQube/SonarCloud cleanup
- GitHub issue umbrella completion
- failing CI job remediation
- issue label normalization
- documentation backlog cleanup
- repeated code quality fixes

## Files

- [`continuous-completion-model.md`](continuous-completion-model.md) — the reusable control loop.
- [`domain-adapter-template.md`](domain-adapter-template.md) — the small task-specific section to append after the control loop.

## How to use

1. Paste `continuous-completion-model.md` at the top of your Cursor prompt.
2. Fill out the domain adapter.
3. Add any project-specific safety rules.
4. Run from a clean repo state.

The main idea is:

> The main agent coordinates. Each concrete work item is handled by a fresh disposable worker/subagent. After each item, only a compact result is kept, live state is refreshed, and the next item is selected.
