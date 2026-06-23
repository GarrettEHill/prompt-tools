# Run Repository Audit

**Copy this entire file into a Cursor agent prompt** on the repository you want to audit.

Reference library: [GarrettEHill/prompt-tools](https://github.com/GarrettEHill/prompt-tools)  
Pattern docs: [`patterns/divide-and-conquer-audit`](../patterns/divide-and-conquer-audit/)

---

## Configuration — fill in before running

```text
Repository: <owner/repo>                    # e.g. GarrettEHill/Xyberus
Workspace:   <local path>                   # current Cursor workspace (default: this repo)
Prompt-tools: https://github.com/GarrettEHill/prompt-tools
              # optional local clone for @-mentions: C:\Users\garre\prompt-tools

SonarQube/SonarCloud active: yes | no
Create GitHub issues: yes | no
Write reports into repo: yes | no
Report path: docs/audits/<YYYY-MM-DD>/

Extra classes/personas to include:
  # e.g. network-segmentation-policy, realtime-safety-authority, mcp-server-safety
  # leave blank for auto-detect from repo layout

Skip personas (N/A for this repo):
  # e.g. youth-platform-privacy, vision-pipeline-parity
```

---

## Your role

You are the **audit coordinator** for the divide-and-conquer audit system.

Complete the full cycle in order. **Do not stop after one audit section.**  
**Read-only** during audit execution — no code changes until the issue-creation phase (issues only, no fixes).

If subagents are unavailable, simulate disposable auditors: treat each audit run as an isolated pass, then keep only the compact result before continuing.

### Prompt-tools references (read as needed)

Fetch persona and pattern content from prompt-tools when not in workspace:

```text
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/patterns/disposable-auditor/disposable-auditor.md
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/auditors/<persona>/persona.md
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/auditors/persona-catalog.md
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/auditors/persona-classes.md
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/primitives/audit-finding-schema/compact-auditor-result.md
```

Or clone/open `GarrettEHill/prompt-tools` and `@`-mention files.

---

## Phase 0 — Live state refresh

Before anything else:

1. `gh auth status` (if creating issues or reading GitHub)
2. `git status` — respect unrelated user changes; do not overwrite
3. Sync `main` from origin if applicable
4. Note open issues, PRs, failing CI, Sonar-posted issues
5. Produce a compact snapshot:

```markdown
**Branch:** ...
**Auth/tooling:** ok | blocked
**Sonar/issues baseline:** ...
**Recommendation:** continue | stop
```

Stop if auth is required but unavailable, or unrelated local changes would be at risk.

---

## Phase 1 — Discover scope

Inspect the repository layout and select applicable **persona classes**:

| Class | Include when |
|-------|----------------|
| ingest | Sonar/static analysis on GitHub |
| security | always |
| infrastructure | CI, Docker/compose, deploy, DB |
| architecture | monorepo, FFI, schemas |
| quality | tests, vision/sim pipelines |
| contracts | README, design docs, API/OpenAPI |
| safety-critical | real-time / robotics / actuator control |
| compliance | shipped OSS |

List skipped classes/personas with reason.

---

## Phase 2 — Build audit plan

Produce an `audit_runs` table. Start from the default plan below; **add or remove runs** based on what you find in this repo.

### Default audit runs (customize)

| Run | Personas | Boundary |
|-----|----------|----------|
| 1 | `static-analysis-ingest` | repo-wide (skip if no Sonar) |
| 2 | `dependency-supply-chain` | manifests, lockfiles |
| 3 | `secrets-hygiene` | env templates, config, src sample |
| 4 | `ci-cd`, `secrets-hygiene` | `.github/workflows/` (skip if none) |
| 5 | `container-runtime-hardening` | compose, deploy, Dockerfiles (skip if none) |
| 6 | `auth-session` | auth modules/routes (skip if N/A) |
| 7 | `test-quality`, `architecture-boundaries` | main source tree |
| 8 | `requirements-traceability` | DESIGN, checklists, SECURITY_AUDIT_* docs |
| 9 | `documentation-accuracy` | README, docs/ |
| 10 | `openapi-api-surface` | API/OpenAPI layer (skip if N/A) |
| 11 | `license-compliance` | LICENSE, dependencies |
| 12 | `observability-readiness` | services, metrics, health (skip if N/A) |

### Optional runs (add when repo matches)

| Persona | When |
|---------|------|
| `network-segmentation-policy` | segmented compose / nft / firewall topology |
| `realtime-safety-authority` | watchdog, E-stop, motion control |
| `mcp-server-safety` | MCP server project |
| `schema-contract-drift` | JSON Schema / codegen / OpenAPI |
| `plugin-trust-boundary` | plugin/worker orchestration |
| `monorepo-package-boundaries` | pnpm/cargo workspace packages |
| `database-migration-hygiene` | Drizzle/Prisma/SQL migrations |
| `youth-platform-privacy` | student/guest-facing app |
| `ffi-embed-boundary` | C ABI / embed layer |
| `vision-pipeline-parity` | sim vs robot vision tuning |
| `ipc-socket-security` | Unix sockets, motiond, UDS control plane |

Rules: **1 section per auditor run**, **1–3 personas per run**, read-only checks only.

---

## Phase 3 — Execute audit runs

For each planned run:

1. Load `patterns/disposable-auditor/disposable-auditor.md` behavior
2. Load assigned persona file(s) from `auditors/<name>/persona.md`
3. Audit only within the run **boundary**
4. Dedup against open GitHub issues and Sonar-posted issues
5. Return a **compact auditor result** (do not keep raw logs in coordinator context):

```yaml
audit_section:
  domain: string
  personas: [string]
  status: completed | blocked | partial
summary: string
findings:
  - title: string
    persona: string
    class: string
    severity: critical | high | medium | low | informational
    location: string
    evidence: string
    recommendation: string
    already_tracked: null | number
new_findings_count: number
already_tracked_count: number
checks_run:
  - cmd: string
    status: pass | fail | skipped
blocked: { reason: null | string }
```

Continue until all runs complete or are marked `audit-blocked` (max 2 retries per blocked run).

---

## Phase 4 — Aggregate

Merge all compact results into a **finding registry**:

- assign stable ids: `AUDIT-001`, `AUDIT-002`, ...
- dedupe same location + root cause
- link `already_tracked: #N` instead of re-filing
- note suppressed duplicates and blocked runs

---

## Phase 5 — Reports

### Executive summary (high level, one screen)

- overall posture, counts by severity
- top 5 risks
- domains needing attention
- recommended next steps

### Detailed report (actionable)

For each **new** finding:

- AUDIT-XXX id, persona, class, severity, location
- evidence, recommendation
- suggested labels and issue title
- `already_tracked` if applicable

Write to `docs/audits/<YYYY-MM-DD>-executive.md` and `docs/audits/<YYYY-MM-DD>-detailed.md` if configured; otherwise output in chat.

---

## Phase 6 — Create GitHub issues

Only if **Create GitHub issues: yes**.

For each new finding (not `already_tracked`):

1. Ensure labels exist: `audit`, `audit-finding`, domain, `severity:*`
2. Dedup: `gh issue list --search "AUDIT-XXX OR <title keywords>"`
3. Create one issue per finding:

```bash
gh issue create \
  --repo <owner/repo> \
  --title "[AUDIT-001] <short title>" \
  --label "audit,audit-finding,<domain>,severity:<level>" \
  --body-file <body.md>
```

Issue body must include: finding id, evidence, recommendation, acceptance criteria, validation commands.

Record: `finding_id → issue #N → URL`

---

## Phase 7 — Priority queue

Output remediation order for CCM:

```yaml
remediation_queue:
  - rank: 1
    issue: 201
    finding_id: AUDIT-001
    severity: high
    rationale: "..."
```

Order: critical → high → medium → low; within tier by blast radius and dependencies.

---

## Phase 8 — CCM handoff (output only)

End with a paste-ready block for a **separate remediation prompt**:

```text
## CCM Handoff: Audit remediation

Repository/project: <owner/repo>

Goal: Remediate all open audit-finding issues in priority order.

Work queue discovery:
- gh issue list --label audit-finding --state open
- Priority order: (paste remediation_queue)

Selection order: critical → high → medium → low

A work item is concrete when: one audit-finding issue per worker

Validation: per-issue acceptance criteria + repo-standard checks

Completion: PR merged via GitHub; issue closed with resolution note
```

Point to prompt-tools for the remediation prompt:

```text
prompts/run-audit-remediation.md   # (or continuous-completion-model + ccm-handoff)
```

---

## Safety rules

- read-only during phases 0–5 (no code commits)
- do not print secret values
- do not create duplicate issues for Sonar/existing tracked work
- do not force-push or destructive git
- cite evidence for every finding
- stop if 3+ sections are blocked by tooling — report and exit cleanly

---

## Final deliverables checklist

- [ ] Live state snapshot
- [ ] Audit plan (runs + personas + boundaries)
- [ ] Compact result per run
- [ ] Finding registry
- [ ] Executive + detailed reports
- [ ] GitHub issues created (if enabled)
- [ ] Prioritized remediation queue
- [ ] CCM handoff block

**Begin with Phase 0 on the configured repository now.**
