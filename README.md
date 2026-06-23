# Prompt Tools

Reusable prompts and workflow patterns for Cursor, Codex-style agents, and GitHub-connected automation.

## Contents

- [`patterns/continuous-completion-model`](patterns/continuous-completion-model/) — reusable coordinator + disposable worker/subagent loop for prompts that should keep working item-by-item until complete.

## Intended use

Copy the continuous completion model into the top of a task-specific prompt, then add a short domain adapter describing:

- how to discover the work queue
- how to order the queue
- what validation is required
- what counts as complete
- when to stop

This keeps long-running prompts consistent without rewriting the whole control loop each time.
