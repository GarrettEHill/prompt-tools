# Prompts

Copy-paste prompts for Cursor agent sessions.

## Audit pipeline

1. **[`run-repository-audit.md`](run-repository-audit.md)** — run on target repo: discover, audit, report, file issues, prioritize
2. **[`run-audit-remediation.md`](run-audit-remediation.md)** — run on same repo after audit: fix issues via CCM

## Usage

1. Open the **target repository** in Cursor (not prompt-tools).
2. Open Composer/Agent and paste the full contents of `run-repository-audit.md`.
3. Fill in the **Configuration** section at the top.
4. After audit completes, paste `run-audit-remediation.md` with the CCM handoff block.

## Prompt-tools access

The agent needs persona/pattern content from this repo. Either:

- `@` mention a local clone of `GarrettEHill/prompt-tools`, or
- let the agent fetch from `https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/...`

## Related

- [`patterns/divide-and-conquer-audit`](../patterns/divide-and-conquer-audit/)
- [`auditors/`](../auditors/)
