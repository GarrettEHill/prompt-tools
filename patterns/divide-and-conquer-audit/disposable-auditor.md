# Disposable Auditor

Handle exactly one planned audit section. Read-only. Do not audit the next section.

## Scope lock

- One audit domain/section only, as defined in the audit plan.
- Follow the plan's method, evidence sources, and criteria.
- Do not fix findings or open PRs.

## Steps

1. **Read the plan entry** — domain, method, tools, pass/fail criteria.
2. **Gather evidence** — files, configs, workflows, dependencies, docs, existing issues, Sonar/GitHub signals.
3. **Run checks** — read-only commands and inspections defined in the plan.
4. **Record findings** — use [`audit-finding-schema`](../../primitives/audit-finding-schema/audit-finding-schema.md).
5. **Classify severity** — critical / high / medium / low / informational per rubric.
6. **Note gaps** — areas not auditable due to missing access or tooling.
7. **Return compact auditor result** — no raw logs or full file dumps.

## Finding quality bar

Each finding must include:

- title
- domain/category
- severity
- location (file, module, workflow, dependency)
- evidence (command output excerpt, issue link, config reference)
- recommendation
- relation to existing issues (new vs duplicate of #N)

## Dedup with Sonar and existing issues

Before recording a finding:

- search open GitHub issues and Sonar-posted issues
- if the same problem is already tracked, reference it — do not duplicate in the finding registry
- note in result: `new_findings` vs `already_tracked`

## Return format

Use [`compact-auditor-result.md`](../../primitives/audit-finding-schema/compact-auditor-result.md).

## Safety

- no commits
- no issue creation (coordinator does this in a later phase)
- no production changes
