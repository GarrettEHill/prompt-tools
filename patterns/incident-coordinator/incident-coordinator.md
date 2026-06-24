# Incident Coordinator

Structured incident response. **Document mitigations only** — no production changes without explicit user approval.

## Loop

1. Refresh live state
2. Establish timeline ([`incident-timeline-template.md`](incident-timeline-template.md))
3. Collect evidence: logs, metrics, deploy events, recent changes
4. Assess severity/impact
5. Propose mitigations vs fixes (mitigations = immediate; fixes = follow-up)
6. Feed postmortem generator when stable

## Output

[`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md) with `type: incident`.

## Safety

No production changes, rollbacks, or secret rotation without explicit user approval.
