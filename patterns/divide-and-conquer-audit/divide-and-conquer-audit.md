# Divide and Conquer Audit

Operate as an audit coordinator with disposable auditors.

The goal is to complete a full audit cycle: discover scope → plan → audit each section → aggregate → report → file issues → prioritize → hand off to remediation. Do not stop after one audit section.

## Coordinator Responsibilities

The main agent is only the audit coordinator.

It must:

1. Refresh live project state before starting.
2. **Discover audit scope** — identify domains/sections that need auditing (see [`audit-scope-discovery.md`](audit-scope-discovery.md)).
3. **Build an audit plan** — for each domain, define method, evidence sources, and pass/fail criteria (see [`audit-plan-template.md`](audit-plan-template.md)).
4. Select exactly one audit domain/section at a time.
5. Spawn a fresh disposable auditor for that one section.
6. Give the auditor only minimal context:

   - repository/project
   - selected audit domain and plan entry
   - evidence sources and tools available
   - finding severity rubric
   - read-only safety rules

7. After the auditor finishes, discard the auditor context.
8. Keep only a compact auditor result (see [`primitives/audit-finding-schema`](../../primitives/audit-finding-schema/)).
9. Refresh live state between sections if needed.
10. Continue until all planned audit sections are complete or blocked.

### After all audits complete

11. **Aggregate** findings into a single registry (see [`aggregation-and-reporting.md`](aggregation-and-reporting.md)).
12. **Generate reports** — executive summary + detailed report.
13. **Create GitHub issues** from the detailed report with labels (see [`issue-generation.md`](issue-generation.md)).
14. **Define priority order** for remediation (see [`priority-queue-output.md`](priority-queue-output.md)).
15. **Hand off** to Continuous Completion Model (see [`ccm-handoff.md`](ccm-handoff.md)).

Do not allow the coordinator context to accumulate full logs, raw tool output, or repeated analysis from prior auditors. Keep compact results only until aggregation.

If real subagents are unavailable, simulate by treating each audit section as an isolated task and summarizing only the compact result before continuing.

## Auditor Responsibilities

Each auditor handles exactly one planned audit section. See [`disposable-auditor.md`](disposable-auditor.md).

Auditors are **read-only** unless the domain adapter explicitly allows issue creation in a later phase. During audit execution:

- inspect live evidence
- run read-only checks and scanners
- record findings with severity, location, and evidence
- do not fix code
- do not open PRs
- return compact auditor result

## Continuous Loop (audit execution)

Repeat for each planned audit section:

1. Refresh live state if cross-section drift matters.
2. Select next unaudited or incomplete section.
3. Spawn fresh auditor with plan entry for that section.
4. Auditor inspects, checks, records findings.
5. Coordinator stores compact result.
6. Discard auditor context.
7. Continue.

## Stop Rules

Stop the audit cycle only when:

- all planned sections are audited
- remaining sections are blocked (missing access, tooling, credentials)
- baseline environment is unavailable
- continuing requires production access or secrets not available
- audit retry limits are hit for a section

A blocked section is recorded and the coordinator continues to the next independent section when safe.

## Retry Rules

Each audit section gets at most 2 re-run attempts if tooling fails or evidence is incomplete.

If still blocked, record the section as `audit-blocked` and continue.

## Safety Rules

Always:

- read-only during audit execution phases
- respect existing user changes
- avoid modifying code, config, or issues during audit (issue creation is a separate phase after aggregation)
- cite evidence for every finding
- deduplicate findings that Sonar or other tools already track — reference existing issues when appropriate

Never:

- assume prior chat state is current
- invent findings without evidence
- create duplicate GitHub issues for the same underlying problem
- suppress or omit critical findings to shorten the report

## Final Deliverables

When the full audit cycle completes:

1. Executive report (high level)
2. Detailed report (actionable findings)
3. Labeled GitHub issues (one finding or tight group per issue)
4. Prioritized remediation queue for CCM
5. CCM handoff block ready to paste
