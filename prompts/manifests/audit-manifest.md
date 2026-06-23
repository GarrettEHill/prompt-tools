# Audit load manifest

Loaded by [`run-repository-audit.md`](../run-repository-audit.md).  
Resolve each path from `PROMPT_TOOLS_BASE` (local clone or GitHub raw).

## Bootstrap (load once at start)

```text
patterns/divide-and-conquer-audit/divide-and-conquer-audit.md
patterns/live-state-refresh/live-state-refresh.md
adapters/full-repository-audit/domain-adapter.md
adapters/full-repository-audit/audit-domains.md
auditors/persona-classes.md
auditors/persona-catalog.md
auditors/persona-composition.md
primitives/audit-finding-schema/audit-finding-schema.md
primitives/audit-finding-schema/compact-auditor-result.md
```

## Per phase

### Phase 0 — preflight

Load: `patterns/live-state-refresh/preflight-checklist.md`  
Inspect target repo: `git status`, `gh auth status`, open issues/PRs.

### Phase 1 — scope

Load: `patterns/divide-and-conquer-audit/audit-scope-discovery.md`  
Inspect target repo layout; pick classes/personas from `persona-catalog.md` project shortcuts.

### Phase 2 — plan

Load: `patterns/divide-and-conquer-audit/audit-plan-template.md`  
Start from `adapters/full-repository-audit/audit-domains.md`; customize `audit_runs` from repo inspection.

### Phase 3 — execute (per run)

Always load: `patterns/disposable-auditor/disposable-auditor.md`  
Per run, load: `auditors/<persona>/persona.md` for each assigned persona (1–3).  
Class indexes if needed: `auditors/classes/<class>.md`

### Phase 4 — aggregate

Load: `patterns/divide-and-conquer-audit/aggregation-and-reporting.md`

### Phase 5 — reports

Use templates in `aggregation-and-reporting.md`.  
Optional: `patterns/final-report/final-report-template.md` for remediation handoff shape.

### Phase 6 — issues

Load: `patterns/divide-and-conquer-audit/issue-generation.md`  
Skip if config `create_issues: no`.

### Phase 7 — prioritize

Load: `patterns/divide-and-conquer-audit/priority-queue-output.md`

### Phase 8 — handoff

Load: `patterns/divide-and-conquer-audit/ccm-handoff.md`  
Output filled handoff + point to `prompts/run-audit-remediation.md`.

## Optional personas (load when plan includes them)

```text
auditors/network-segmentation-policy/persona.md
auditors/realtime-safety-authority/persona.md
auditors/mcp-server-safety/persona.md
auditors/schema-contract-drift/persona.md
auditors/plugin-trust-boundary/persona.md
auditors/monorepo-package-boundaries/persona.md
auditors/database-migration-hygiene/persona.md
auditors/youth-platform-privacy/persona.md
auditors/ffi-embed-boundary/persona.md
auditors/vision-pipeline-parity/persona.md
auditors/ipc-socket-security/persona.md
```

## Default personas (load per run as planned)

```text
auditors/static-analysis-ingest/persona.md
auditors/dependency-supply-chain/persona.md
auditors/secrets-hygiene/persona.md
auditors/ci-cd/persona.md
auditors/container-runtime-hardening/persona.md
auditors/auth-session/persona.md
auditors/test-quality/persona.md
auditors/architecture-boundaries/persona.md
auditors/requirements-traceability/persona.md
auditors/documentation-accuracy/persona.md
auditors/openapi-api-surface/persona.md
auditors/license-compliance/persona.md
auditors/observability-readiness/persona.md
```
