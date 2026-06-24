# Operate Safety

Mandatory rules for Operate family workflows.

## Always

- Read-only on production unless user explicitly approves deploy/smoke actions.
- Document environment and credentials scope before any live check.
- Prefer staging/sandbox endpoints when available.
- Never delete resources, rotate secrets, or change infra without explicit approval.
- Output recommendations only; user executes changes.

## Never

- Run destructive commands against production.
- Expose credentials in reports.
- Assume metrics/billing APIs are available without checking auth.
