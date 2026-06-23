# Divide and Conquer Audit

Coordinator-driven audit system that discovers scope, plans per-section audits, runs disposable auditors, aggregates findings, reports, files GitHub issues, and outputs a prioritized queue for the Continuous Completion Model.

## When to use

- periodic repository health audits beyond SonarQube alone
- pre-release security/reliability/readiness reviews
- bootstrapping a remediation backlog from scratch
- feeding structured issues into [`continuous-completion-model`](../continuous-completion-model/)

SonarQube covers static analysis well. This pattern covers **what else to audit**, **how to audit each area**, and **how to turn findings into prioritized GitHub issues** for remediation.

## Phases

| Phase | Doc | Output |
|-------|-----|--------|
| 0. Preflight | [`live-state-refresh`](../live-state-refresh/) | continue/stop |
| 1. Discover scope | [`audit-scope-discovery.md`](audit-scope-discovery.md) | audit domain list |
| 2. Plan audits | [`audit-plan-template.md`](audit-plan-template.md) | per-domain audit plan |
| 3. Execute audits | [`disposable-auditor.md`](disposable-auditor.md) | compact auditor results |
| 4. Aggregate | [`aggregation-and-reporting.md`](aggregation-and-reporting.md) | finding registry |
| 5. Report | [`aggregation-and-reporting.md`](aggregation-and-reporting.md) | executive + detailed reports |
| 6. File issues | [`issue-generation.md`](issue-generation.md) | labeled GitHub issues |
| 7. Prioritize | [`priority-queue-output.md`](priority-queue-output.md) | ordered remediation queue |
| 8. Hand off | [`ccm-handoff.md`](ccm-handoff.md) | CCM-ready prompt |

## Files

- [`divide-and-conquer-audit.md`](divide-and-conquer-audit.md) — main coordinator control loop
- [`disposable-auditor.md`](disposable-auditor.md) — one audit section per worker
- [`audit-scope-discovery.md`](audit-scope-discovery.md) — identify what needs auditing
- [`audit-plan-template.md`](audit-plan-template.md) — define how each section is audited
- [`aggregation-and-reporting.md`](aggregation-and-reporting.md) — merge findings and write reports
- [`issue-generation.md`](issue-generation.md) — create GitHub issues with labels
- [`priority-queue-output.md`](priority-queue-output.md) — remediation priority order
- [`ccm-handoff.md`](ccm-handoff.md) — feed prioritized issues into CCM
- [`domain-adapter-template.md`](domain-adapter-template.md) — project-specific fill-in

## Related

- Remediation: [`patterns/continuous-completion-model`](../continuous-completion-model/)
- Finding schema: [`primitives/audit-finding-schema`](../../primitives/audit-finding-schema/)
- Example adapter: [`adapters/full-repository-audit`](../../adapters/full-repository-audit/)

## How to compose

```text
live-state-refresh
+ divide-and-conquer-audit
+ disposable-auditor
+ audit-finding-schema
+ <audit domain adapter>
+ issue-generation
+ priority-queue-output
→ ccm-handoff → continuous-completion-model
```
