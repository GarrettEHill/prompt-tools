#!/usr/bin/env python3
"""Generate remaining workflow family files for epic #64."""
from pathlib import Path

ROOT = Path(__file__).parent.parent

def write(rel: str, content: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {rel}")


def bootstrap(name: str, family: str, title: str, config: str, pattern: str, extra: str = "") -> str:
    return f"""# Remote {family} bootstrap — {title}

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
{config}
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{{PROMPT_TOOLS_BASE}}prompts/manifests/{name}-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. {extra}

**Begin:** load manifest, refresh live state, then run coordinator.
"""


def manifest(name: str, files: list[str], optional: list[str] | None = None) -> str:
    lines = ["# " + name.replace("-", " ").title() + " manifest", "", "Bootstrap:"]
    for f in files:
        lines.append(f"- {f}")
    if optional:
        lines.extend(["", "Optional:"])
        for f in optional:
            lines.append(f"- {f}")
    return "\n".join(lines) + "\n"


def readme(title: str, coordinator: str, bootstrap_path: str, files: list[tuple[str, str]]) -> str:
    file_lines = "\n".join(f"- [`{f[0]}`]({f[0]}) — {f[1]}" for f in files)
    return f"""# {title}

## Files

{file_lines}

## Remote

[`{bootstrap_path}`](../../{bootstrap_path})

## Handoff

See coordinator stop rules and compact result schema.
"""


def main() -> None:
    # --- Shared primitives ---
    write("primitives/investigation-result-schema/investigation-result-schema.md", """# Investigation Result Schema

Compact output for regression hunt, flake hunter, and incident workflows.

```yaml
investigation:
  type: regression | flake | incident
  repo: string
  symptom: string
  status: root-cause-found | mitigated | blocked | inconclusive
summary: string
timeline:
  - at: string
    event: string
    evidence: string
hypothesis:
  - statement: string
    confidence: high | medium | low
    evidence: string
root_cause: string | null
regression_window:
  good_ref: string | null
  bad_ref: string | null
  suspect_commits: [string]
classification: flake | env | deterministic-bug | null
impact:
  severity: sev1 | sev2 | sev3 | sev4
  scope: string
mitigations:
  - action: string
    type: mitigation | fix
    status: proposed | applied | blocked
blockers: [string]
checks_run: [{cmd, status}]
next_steps: [string]
```
""")

    write("primitives/investigation-result-schema/README.md", """# Investigation Result Schema

Shared compact output for Investigate family workflows.

- [`investigation-result-schema.md`](investigation-result-schema.md)
""")

    write("primitives/decision-record-schema/decision-record.md", """# Decision Record Schema

Output for Decide family workflows. **No merge by default.**

```yaml
decision:
  title: string
  status: proposed | accepted | rejected | deferred
  date: string
context: string
options:
  - name: string
    pros: [string]
    cons: [string]
    risks: [string]
recommendation: string
non_goals: [string]
evidence: [string]
follow_up:
  issues: [string]
  spikes: [string]
no_commit: true
```
""")

    write("primitives/decision-record-schema/README.md", """# Decision Record Schema

- [`decision-record.md`](decision-record.md)
""")

    write("primitives/license-policy-template/license-policy-template.md", """# License Policy Template

Configure before running license-policy-gate.

```yaml
policy:
  allowed:
    - MIT
    - Apache-2.0
    - BSD-2-Clause
    - BSD-3-Clause
    - ISC
  denied:
    - GPL-3.0
    - AGPL-3.0
    - SSPL-1.0
  review_required:
    - LGPL-2.1
    - LGPL-3.0
    - MPL-2.0
  unknown_action: block | review
exceptions: []
```

Human review required for `review_required` and unknown licenses.
""")

    write("primitives/license-policy-template/README.md", """# License Policy Template

- [`license-policy-template.md`](license-policy-template.md)
""")

    write("primitives/operate-safety/operate-safety.md", """# Operate Safety

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
""")

    write("primitives/operate-safety/README.md", """# Operate Safety

- [`operate-safety.md`](operate-safety.md)
""")

    write("primitives/smoke-result-schema/smoke-result-schema.md", """# Smoke Result Schema

```yaml
smoke:
  environment: string
  deploy_ref: string
  verdict: pass | fail | partial | blocked
summary: string
checks:
  - name: string
    type: health | critical-path | integration
    status: pass | fail | skip
    evidence: string
rollback_triggered: false
blockers: [string]
checks_run: [{cmd, status}]
```
""")

    write("primitives/smoke-result-schema/README.md", """# Smoke Result Schema

- [`smoke-result-schema.md`](smoke-result-schema.md)
""")

    write("primitives/cost-finding-schema/cost-finding-schema.md", """# Cost Finding Schema

```yaml
cost_review:
  period: string
  sources: [string]
findings:
  - category: overprovisioned | idle | misconfigured | unknown
    resource: string
    evidence: string
    estimated_savings: string
    risk: low | medium | high
recommendations:
  - action: string
    priority: high | medium | low
    requires_approval: true
```
""")

    write("primitives/cost-finding-schema/README.md", """# Cost Finding Schema

- [`cost-finding-schema.md`](cost-finding-schema.md)
""")

    # --- INVESTIGATE ---
    write("patterns/regression-hunt/regression-hunt.md", """# Regression Hunt Coordinator

Bisect-style regression investigation. **Read-only** until user approves a fix.

Extends [`investigation-before-change`](../investigation-before-change/investigation-before-change.md).

## Loop

1. Refresh live state
2. Capture symptom, repro steps, last-known-good signal
3. Narrow regression window via `git log`, tags, CI history
4. Spawn [`regression-worker`](regression-worker.md) per suspect commit range or hypothesis
5. Aggregate [`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md)
6. Stop at root cause, blocked, or inconclusive with evidence

## Stop rules

- Root cause identified with evidence
- Regression window narrowed to ≤3 suspect commits
- Blocked: cannot reproduce, no git history, or missing CI logs
- 3 hypothesis failures → document blockers, hand off to CCM if fix needed

## Safety

Read-only bisect. No `git bisect run` with auto-commits unless user approves.
""")

    write("patterns/regression-hunt/regression-worker.md", """# Regression Worker

One hypothesis or commit range per worker.

1. Reproduce symptom (test, build, or script)
2. Record evidence (logs, diff, env)
3. Classify: introduced by commit | flaky | env | pre-existing
4. Return compact investigation result — no unrelated fixes
""")

    write("patterns/regression-hunt/README.md", readme(
        "Regression Hunt", "regression-hunt.md", "prompts/bootstrap-investigate-regression.md",
        [("regression-hunt.md", "coordinator"), ("regression-worker.md", "disposable worker")],
    ))

    write("patterns/incident-coordinator/incident-coordinator.md", """# Incident Coordinator

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
""")

    write("patterns/incident-coordinator/incident-timeline-template.md", """# Incident Timeline Template

```markdown
## Incident: <title>
**Started:** <UTC>
**Status:** investigating | mitigated | resolved
**Severity:** sev1 | sev2 | sev3 | sev4
**Impact:** <users/systems affected>

### Timeline
| Time (UTC) | Event | Evidence |
|------------|-------|----------|
| | | |

### Mitigations (immediate)
- [ ] <action> — owner — status

### Fixes (follow-up)
- [ ] <action> — owner — issue link
```
""")

    write("patterns/incident-coordinator/README.md", readme(
        "Incident Coordinator", "incident-coordinator.md", "prompts/bootstrap-investigate-incident.md",
        [("incident-coordinator.md", "coordinator"), ("incident-timeline-template.md", "timeline template")],
    ))

    write("patterns/flake-hunter/flake-hunter.md", """# Flake Hunter

Focused workflow for intermittent CI failures.

## Loop

1. Refresh live state; pull CI logs for failed job(s)
2. Reproduce locally if possible (repeat run N times)
3. Classify per [`flake-classification.md`](flake-classification.md)
4. Route:
   - **flake** → quarantine recommendation + evidence
   - **env** → infra/config issue
   - **deterministic bug** → hand off to CCM
   - **blocked** → insufficient logs

## Output

[`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md) with `type: flake`.

## Evidence for quarantine

Require ≥3 failed runs with inconsistent failure point OR pass on retry without code change.
""")

    write("patterns/flake-hunter/flake-classification.md", """# Flake Classification

| Outcome | Signals | Next action |
|---------|---------|-------------|
| **flake** | Passes on retry; non-deterministic assertion/timing | Quarantine policy or fix test |
| **env** | Fails consistently in one runner/region | Check infra, deps, secrets scope |
| **deterministic bug** | Fails consistently locally | CCM implement fix |
| **blocked** | Cannot reproduce; logs truncated | Request more CI retention |

Document evidence for each classification.
""")

    write("patterns/flake-hunter/README.md", readme(
        "Flake Hunter", "flake-hunter.md", "prompts/bootstrap-investigate-flake.md",
        [("flake-hunter.md", "coordinator"), ("flake-classification.md", "classification outcomes")],
    ))

    write("patterns/postmortem/postmortem-generator.md", """# Postmortem Generator

Blameless postmortem from compact investigation or incident results.

## Input

- [`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md)
- Incident timeline (optional)
- CCM final-report (optional)

## Steps

1. Load inputs (paths or pasted YAML)
2. Fill [`postmortem-template.md`](postmortem-template.md)
3. Extract action items with owners
4. Optional: create follow-up issues via divide-and-conquer issue-generation

## Output

Markdown postmortem + action item list linkable to GitHub issues.
""")

    write("patterns/postmortem/postmortem-template.md", """# Postmortem Template

```markdown
# Postmortem: <title>
**Date:** <YYYY-MM-DD>
**Authors:** <names>
**Status:** draft | final

## Summary
<2-3 sentences>

## Impact
- Duration:
- Users/systems affected:
- Severity:

## Timeline
| Time | Event |
|------|-------|

## Root cause
<blameless technical explanation>

## Contributing factors
-

## What went well
-

## What went poorly
-

## Action items
| Action | Owner | Priority | Tracking |
|--------|-------|----------|----------|
| | | | #issue |

## Lessons learned
-
```
""")

    write("patterns/postmortem/README.md", readme(
        "Postmortem Generator", "postmortem-generator.md", "prompts/bootstrap-investigate-postmortem.md",
        [("postmortem-generator.md", "generator"), ("postmortem-template.md", "blameless template")],
    ))

    inv_bootstraps = [
        ("investigate-regression", "investigate", "regression hunt", "symptom: <description>\nlast_good_ref: <tag or sha>  # optional\nfailing_ref: HEAD  # optional", "patterns/regression-hunt/regression-hunt.md", "Pairs with failing-ci-remediation adapter."),
        ("investigate-incident", "investigate", "incident coordinator", "incident: <title>\nseverity: sev2  # optional", "patterns/incident-coordinator/incident-coordinator.md", "Document only — no prod changes without approval."),
        ("investigate-flake", "investigate", "flake hunter", "workflow_run: <url or id>  # optional\ntest_name: <name>  # optional", "patterns/flake-hunter/flake-hunter.md", "Classify flake vs env vs bug."),
        ("investigate-postmortem", "investigate", "postmortem generator", "input: <path to investigation result or timeline>", "patterns/postmortem/postmortem-generator.md", "Blameless postmortem output."),
    ]
    inv_manifests = {
        "investigate-regression": (
            ["patterns/regression-hunt/regression-hunt.md", "patterns/regression-hunt/regression-worker.md",
             "patterns/live-state-refresh/live-state-refresh.md", "patterns/investigation-before-change/investigation-before-change.md",
             "primitives/investigation-result-schema/investigation-result-schema.md"],
            ["adapters/failing-ci-remediation/domain-adapter.md"],
        ),
        "investigate-incident": (
            ["patterns/incident-coordinator/incident-coordinator.md", "patterns/incident-coordinator/incident-timeline-template.md",
             "patterns/live-state-refresh/live-state-refresh.md", "primitives/investigation-result-schema/investigation-result-schema.md"],
            ["patterns/postmortem/postmortem-generator.md"],
        ),
        "investigate-flake": (
            ["patterns/flake-hunter/flake-hunter.md", "patterns/flake-hunter/flake-classification.md",
             "patterns/live-state-refresh/live-state-refresh.md", "primitives/investigation-result-schema/investigation-result-schema.md"],
            None,
        ),
        "investigate-postmortem": (
            ["patterns/postmortem/postmortem-generator.md", "patterns/postmortem/postmortem-template.md",
             "primitives/investigation-result-schema/investigation-result-schema.md"],
            ["patterns/divide-and-conquer-audit/issue-generation.md"],
        ),
    }
    for name, family, title, config, pattern, extra in inv_bootstraps:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern, extra))
        files, opt = inv_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))

    print("Investigate family done.")


def generate_communicate() -> None:
    write("patterns/executive-brief/executive-brief.md", """# Executive Brief

One-screen synthesis from audit, CCM, investigation, or incident compact results.

## Input

Paths or pasted summaries from:
- audit executive report
- [`final-report-template`](../final-report/final-report-template.md)
- [`investigation-result-schema`](../../primitives/investigation-result-schema/investigation-result-schema.md)

## Output

Fill [`executive-brief-template.md`](executive-brief-template.md) — max one screen.

## Rules

- Lead with verdict and risk
- No raw log dumps
- Link to detailed artifacts for drill-down
""")

    write("patterns/executive-brief/executive-brief-template.md", """# Executive Brief Template

```markdown
# Executive brief: <initiative>
**Date:** <YYYY-MM-DD> | **Audience:** <role>

## Headline
<one sentence>

## Status
🟢 on track | 🟡 at risk | 🔴 blocked

## Key outcomes
-

## Top risks / blockers
-

## Decisions needed
-

## Next 7 days
-
```
""")

    write("patterns/executive-brief/README.md", readme(
        "Executive Brief", "executive-brief.md", "prompts/bootstrap-communicate-executive.md",
        [("executive-brief.md", "generator"), ("executive-brief-template.md", "one-screen template")],
    ))

    write("patterns/umbrella-issue-composer/umbrella-issue-composer.md", """# Umbrella Issue Composer

Proactive planning: compose umbrella epics with decomposed child issues.

Related: [`umbrella-issue-completion`](../../adapters/umbrella-issue-completion/domain-adapter.md) (execution).

## Loop

1. Load goal and acceptance criteria from user
2. Decompose via [`work-item-decomposition`](../work-item-decomposition/work-item-decomposition.md)
3. Draft umbrella body + child stubs per [`child-issue-template.md`](child-issue-template.md)
4. Optional: `gh issue create` batch with labels (user approves)

## Output

Umbrella issue body + child issue stubs each with acceptance criteria.
""")

    write("patterns/umbrella-issue-composer/child-issue-template.md", """# Child Issue Template

```markdown
## Summary
<worker-sized scope>

## Acceptance criteria
- [ ] <criterion>

## Parent
Umbrella: #<number>

## Labels
<workflow labels>
```
""")

    write("patterns/umbrella-issue-composer/README.md", readme(
        "Umbrella Issue Composer", "umbrella-issue-composer.md", "prompts/bootstrap-communicate-umbrella.md",
        [("umbrella-issue-composer.md", "composer"), ("child-issue-template.md", "child stub template")],
    ))

    write("patterns/stakeholder-status/stakeholder-status.md", """# Stakeholder Status

Periodic status digest from GitHub issues, PRs, and releases.

## Config

```yaml
since_date: <YYYY-MM-DD>  # optional
milestone: <name>         # optional
```

## Steps

1. `gh issue list`, `gh pr list`, merged PRs since date
2. Optional: ingest CCM [`final-report`](../final-report/final-report-template.md)
3. Fill [`status-digest-template.md`](status-digest-template.md)

## Sections

Shipped / In progress / Blocked / Next
""")

    write("patterns/stakeholder-status/status-digest-template.md", """# Status Digest Template

```markdown
# Status digest: <repo>
**Period:** <since> → <now>

## Shipped
- <item> (#PR)

## In progress
- <item> (#issue)

## Blocked
- <item> — blocker

## Next
-
```
""")

    write("patterns/stakeholder-status/README.md", readme(
        "Stakeholder Status", "stakeholder-status.md", "prompts/bootstrap-communicate-status.md",
        [("stakeholder-status.md", "generator"), ("status-digest-template.md", "digest template")],
    ))

    comm = [
        ("communicate-executive", "communicate", "executive brief", "input: <paths or pasted summaries>", "patterns/executive-brief/executive-brief.md"),
        ("communicate-umbrella", "communicate", "umbrella issue composer", "goal: <description>\ncreate_issues: false  # optional", "patterns/umbrella-issue-composer/umbrella-issue-composer.md"),
        ("communicate-status", "communicate", "stakeholder status", "since_date: <YYYY-MM-DD>  # optional\nmilestone: <name>  # optional", "patterns/stakeholder-status/stakeholder-status.md"),
    ]
    comm_manifests = {
        "communicate-executive": (["patterns/executive-brief/executive-brief.md", "patterns/executive-brief/executive-brief-template.md", "patterns/live-state-refresh/live-state-refresh.md"], ["patterns/final-report/final-report-template.md"]),
        "communicate-umbrella": (["patterns/umbrella-issue-composer/umbrella-issue-composer.md", "patterns/umbrella-issue-composer/child-issue-template.md", "patterns/work-item-decomposition/work-item-decomposition.md", "adapters/umbrella-issue-completion/domain-adapter.md"], None),
        "communicate-status": (["patterns/stakeholder-status/stakeholder-status.md", "patterns/stakeholder-status/status-digest-template.md", "patterns/live-state-refresh/live-state-refresh.md"], ["patterns/final-report/final-report-template.md"]),
    }
    for name, family, title, config, pattern in comm:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern))
        files, opt = comm_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))
    print("Communicate family done.")


def generate_transform() -> None:
    write("patterns/migration-sweep/migration-sweep.md", """# Migration Sweep Coordinator

CCM-style coordinator for framework/API migrations.

## Loop

1. Refresh live state
2. Load migration plan from [`adapters/framework-upgrade`](../../adapters/framework-upgrade/domain-adapter.md)
3. Build queue of migration units per [`migration-unit-template.md`](migration-unit-template.md)
4. Spawn [`migration-worker`](migration-worker.md) per unit
5. Validate per [`validation-ladder`](../../primitives/validation-ladder/validation-ladder.md)
6. Hand off blockers to CCM

Parallel to [`continuous-completion-model`](../continuous-completion-model/continuous-completion-model.md).
""")

    write("patterns/migration-sweep/migration-worker.md", """# Migration Worker

One migration unit per worker.

1. Apply scoped migration change
2. Run validation ladder for unit scope
3. Open PR or return compact result
4. Roll back unit on validation failure
""")

    write("patterns/migration-sweep/migration-unit-template.md", """# Migration Unit Template

```yaml
unit:
  id: string
  scope: <path or module>
  from_version: string
  to_version: string
acceptance:
  - <criterion>
validation:
  - <command>
```
""")

    write("patterns/migration-sweep/README.md", readme(
        "Migration Sweep", "migration-sweep.md", "prompts/bootstrap-transform-migration.md",
        [("migration-sweep.md", "coordinator"), ("migration-worker.md", "worker"), ("migration-unit-template.md", "unit template")],
    ))

    write("adapters/framework-upgrade/domain-adapter.md", """# Framework Upgrade Domain Adapter

Plug-in for migration-sweep.

## Responsibilities

- Define migration units from framework version delta
- Map breaking changes to scoped file sets
- Default validation commands per stack

## Config

```yaml
framework: <name>
from_version: string
to_version: string
unit_strategy: directory | module | feature-flag
```
""")

    write("adapters/framework-upgrade/README.md", """# Framework Upgrade Adapter

- [`domain-adapter.md`](domain-adapter.md)
""")

    write("patterns/deprecation-enforcer/deprecation-enforcer.md", """# Deprecation Enforcer

Find deprecated API/symbol usages; queue removals; verify zero usages before deleting exports.

Specialization of migration-sweep.

## Steps

1. Scan for deprecation markers (@deprecated, feature flags, docs)
2. Queue usage removal units
3. Verify empty usage set
4. Remove export in final unit after validation

See [`deprecation-adapter-template.md`](deprecation-adapter-template.md).
""")

    write("patterns/deprecation-enforcer/deprecation-adapter-template.md", """# Deprecation Adapter Template

```yaml
deprecation:
  symbol: string
  markers: [@deprecated, feature_flag, doc_notice]
scan:
  paths: [string]
verify_empty:
  command: string
remove_export:
  path: string
```
""")

    write("patterns/deprecation-enforcer/README.md", readme(
        "Deprecation Enforcer", "deprecation-enforcer.md", "prompts/bootstrap-transform-deprecation.md",
        [("deprecation-enforcer.md", "coordinator"), ("deprecation-adapter-template.md", "adapter template")],
    ))

    write("patterns/codemod-coordinator/codemod-coordinator.md", """# Codemod Coordinator

Coordinate mechanical codemods with per-chunk validation.

Uses migration-sweep discipline. Default: one module/directory per worker.

## Loop

1. Plan codemod chunks via work-item-decomposition
2. Spawn [`codemod-worker`](codemod-worker.md) per chunk
3. Validate; rollback chunk on failure
4. Aggregate PRs or single rolling PR per config
""")

    write("patterns/codemod-coordinator/codemod-worker.md", """# Codemod Worker

One directory/module per worker.

1. Run codemod tool or scripted transform
2. Run validation ladder for chunk
3. Return compact result; no cross-chunk changes
""")

    write("patterns/codemod-coordinator/README.md", readme(
        "Codemod Coordinator", "codemod-coordinator.md", "prompts/bootstrap-transform-codemod.md",
        [("codemod-coordinator.md", "coordinator"), ("codemod-worker.md", "worker")],
    ))

    write("patterns/config-drift-fix/config-drift-fix.md", """# Config Drift Fix

Align env templates, compose profiles, CI matrices — detect drift and queue fixes.

## Drift checklist

- `.env.example` vs documented vars vs CI secrets names
- `docker-compose*.yml` service/env parity
- CI matrix vs supported runtimes
- Feature flags default consistency

Execute fixes via CCM. Adapter: [`env-compose-ci-drift`](../../adapters/env-compose-ci-drift/domain-adapter.md).
""")

    write("adapters/env-compose-ci-drift/domain-adapter.md", """# Env / Compose / CI Drift Adapter

```yaml
sources:
  env_example: .env.example
  compose_files: [docker-compose.yml]
  ci_workflows: [.github/workflows/*.yml]
drift_rules:
  - name: missing_env_in_example
  - name: compose_service_env_mismatch
  - name: ci_runtime_not_in_matrix
```
""")

    write("adapters/env-compose-ci-drift/README.md", """# Env Compose CI Drift Adapter

- [`domain-adapter.md`](domain-adapter.md)
""")

    write("patterns/config-drift-fix/README.md", readme(
        "Config Drift Fix", "config-drift-fix.md", "prompts/bootstrap-transform-config-drift.md",
        [("config-drift-fix.md", "coordinator")],
    ))

    xf = [
        ("transform-migration", "transform", "migration sweep", "framework: <name>\nfrom_version: string\nto_version: string", "patterns/migration-sweep/migration-sweep.md"),
        ("transform-deprecation", "transform", "deprecation enforcer", "symbol: <name>", "patterns/deprecation-enforcer/deprecation-enforcer.md"),
        ("transform-codemod", "transform", "codemod coordinator", "codemod: <tool or script>\nscope: <path>", "patterns/codemod-coordinator/codemod-coordinator.md"),
        ("transform-config-drift", "transform", "config drift fix", "paths: []  # optional override", "patterns/config-drift-fix/config-drift-fix.md"),
    ]
    xf_manifests = {
        "transform-migration": (["patterns/migration-sweep/migration-sweep.md", "patterns/migration-sweep/migration-worker.md", "adapters/framework-upgrade/domain-adapter.md", "patterns/continuous-completion-model/continuous-completion-model.md", "primitives/validation-ladder/validation-ladder.md"], None),
        "transform-deprecation": (["patterns/deprecation-enforcer/deprecation-enforcer.md", "patterns/migration-sweep/migration-sweep.md"], None),
        "transform-codemod": (["patterns/codemod-coordinator/codemod-coordinator.md", "patterns/codemod-coordinator/codemod-worker.md", "patterns/migration-sweep/migration-sweep.md", "primitives/validation-ladder/validation-ladder.md"], None),
        "transform-config-drift": (["patterns/config-drift-fix/config-drift-fix.md", "adapters/env-compose-ci-drift/domain-adapter.md", "patterns/continuous-completion-model/continuous-completion-model.md"], None),
    }
    for name, family, title, config, pattern in xf:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern))
        files, opt = xf_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))
    print("Transform family done.")


def generate_generate() -> None:
    write("patterns/doc-sync/doc-sync.md", """# Doc Sync

Generate or update docs from source with round-trip validation.

## Steps

1. Discover API surface, config, CLI commands from code
2. Generate/update doc sections per [`doc-sync-template.md`](doc-sync-template.md)
3. Round-trip check: doc claims match code
4. PR-only output; user approves merge

Validated by documentation-accuracy auditor persona.
""")

    write("patterns/doc-sync/doc-sync-template.md", """# Doc Sync Template

```markdown
## <Section>
**Source:** `<path>`
**Generated:** <date>

### Commands / API / Config
<content>

### Verification
- [ ] Source path cited
- [ ] Round-trip check passed
```
""")

    write("patterns/doc-sync/README.md", readme(
        "Doc Sync", "doc-sync.md", "prompts/bootstrap-generate-doc-sync.md",
        [("doc-sync.md", "generator"), ("doc-sync-template.md", "section template")],
    ))

    write("patterns/runbook-generator/runbook-generator.md", """# Runbook Generator

Generate operability runbooks from compose, scripts, and deploy manifests.

## Sections

Start, stop, logs, health checks, rollback link (see ship rollback-plan).

Cite compose/script paths as evidence.
""")

    write("patterns/runbook-generator/runbook-template.md", """# Runbook Template

```markdown
# Runbook: <service>
**Sources:** <compose paths, scripts>

## Prerequisites
-

## Start
```bash
```

## Stop
```bash
```

## Logs & health
-

## Rollback
Link: rollback-plan output or manual steps

## Troubleshooting
-
```
""")

    write("patterns/runbook-generator/README.md", readme(
        "Runbook Generator", "runbook-generator.md", "prompts/bootstrap-generate-runbook.md",
        [("runbook-generator.md", "generator"), ("runbook-template.md", "runbook template")],
    ))

    write("patterns/changelog-from-reality/changelog-from-reality.md", """# Changelog From Reality

Build changelog from merged PRs, commits, and labels since last tag.

## Config

```yaml
since_tag: vX.Y.Z
```

## Steps

1. `git log` / `gh pr list --state merged` since tag
2. Classify: breaking, feat, fix, deps
3. Link PRs/issues
4. Fill [`changelog-template.md`](changelog-template.md)

Used by release-coordinator.
""")

    write("patterns/changelog-from-reality/changelog-template.md", """# Changelog Template

```markdown
# Changelog

## Breaking
-

## Features
-

## Fixes
-

## Dependencies
-
```
""")

    write("patterns/changelog-from-reality/README.md", readme(
        "Changelog From Reality", "changelog-from-reality.md", "prompts/bootstrap-generate-changelog.md",
        [("changelog-from-reality.md", "generator"), ("changelog-template.md", "changelog template")],
    ))

    write("patterns/openapi-drift-fix/openapi-drift-fix.md", """# OpenAPI Drift Fix

Generate or patch OpenAPI/spec to match handlers (inverse of openapi-api-surface audit).

## Steps

1. Read route handlers / controllers
2. Update OpenAPI spec to match
3. Validate spec against routes
4. PR with spec + optional client regen

Pairs with schema-contract-drift and openapi-api-surface persona.
""")

    write("patterns/openapi-drift-fix/README.md", readme(
        "OpenAPI Drift Fix", "openapi-drift-fix.md", "prompts/bootstrap-generate-openapi.md",
        [("openapi-drift-fix.md", "generator")],
    ))

    gen = [
        ("generate-doc-sync", "generate", "doc sync", "paths: [docs/]  # optional", "patterns/doc-sync/doc-sync.md"),
        ("generate-runbook", "generate", "runbook generator", "compose: docker-compose.yml  # optional", "patterns/runbook-generator/runbook-generator.md"),
        ("generate-changelog", "generate", "changelog from reality", "since_tag: vX.Y.Z", "patterns/changelog-from-reality/changelog-from-reality.md"),
        ("generate-openapi", "generate", "OpenAPI drift fix", "spec_path: openapi.yaml  # optional", "patterns/openapi-drift-fix/openapi-drift-fix.md"),
    ]
    gen_manifests = {
        "generate-doc-sync": (["patterns/doc-sync/doc-sync.md", "patterns/doc-sync/doc-sync-template.md", "patterns/live-state-refresh/live-state-refresh.md"], None),
        "generate-runbook": (["patterns/runbook-generator/runbook-generator.md", "patterns/runbook-generator/runbook-template.md", "patterns/rollback-plan/rollback-plan.md"], None),
        "generate-changelog": (["patterns/changelog-from-reality/changelog-from-reality.md", "patterns/changelog-from-reality/changelog-template.md"], ["patterns/release-coordinator/release-coordinator.md"]),
        "generate-openapi": (["patterns/openapi-drift-fix/openapi-drift-fix.md", "primitives/validation-ladder/validation-ladder.md"], None),
    }
    for name, family, title, config, pattern in gen:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern))
        files, opt = gen_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))
    print("Generate family done.")


def generate_govern() -> None:
    write("patterns/oss-hygiene/oss-hygiene.md", """# OSS Hygiene

Enforce OSS repo hygiene: LICENSE, CONTRIBUTING, CODEOWNERS, issue/PR templates, SECURITY.md.

## Loop

1. Check checklist per [`oss-hygiene-checklist.md`](oss-hygiene-checklist.md)
2. Record evidence per file (present/missing/stale)
3. File issues or open PRs per config

Adapter distinguishes OSS vs internal repo policy.
""")

    write("patterns/oss-hygiene/oss-hygiene-checklist.md", """# OSS Hygiene Checklist

| File | Required (OSS) | Evidence |
|------|----------------|----------|
| LICENSE | yes | |
| CONTRIBUTING.md | yes | |
| CODEOWNERS | recommended | |
| SECURITY.md | yes | |
| Issue template | recommended | |
| PR template | recommended | |
| README install/build | yes | |
""")

    write("patterns/oss-hygiene/README.md", readme(
        "OSS Hygiene", "oss-hygiene.md", "prompts/bootstrap-govern-oss.md",
        [("oss-hygiene.md", "coordinator"), ("oss-hygiene-checklist.md", "checklist")],
    ))

    write("patterns/label-policy-enforcement/label-policy-enforcement.md", """# Label Policy Enforcement

Recurring enforcement of issue label taxonomy.

Extends [`issue-label-normalization`](../../adapters/issue-label-normalization/domain-adapter.md) for scheduled sweeps.

## Mode

- `audit`: report mismatches
- `fix`: CCM queue per mismatch (user approves `gh issue edit`)

Requires policy template before run.
""")

    write("patterns/label-policy-enforcement/README.md", readme(
        "Label Policy Enforcement", "label-policy-enforcement.md", "prompts/bootstrap-govern-labels.md",
        [("label-policy-enforcement.md", "coordinator")],
    ))

    write("patterns/secret-rotation-sweep/secret-rotation-sweep.md", """# Secret Rotation Sweep

Beyond secrets-hygiene audit: rotation due dates, history exposure signals, CI secret scope.

**Never prints secret values.** Does not rotate without explicit approval.

Classify: rotate | revoke | false-positive. Use [`rotation-record-template.md`](rotation-record-template.md).
""")

    write("patterns/secret-rotation-sweep/rotation-record-template.md", """# Rotation Record Template

```yaml
credential:
  name: string
  location: string  # no value
  last_rotated: date | unknown
  classification: rotate | revoke | false-positive
  evidence: string
  owner: string
```
""")

    write("patterns/secret-rotation-sweep/README.md", readme(
        "Secret Rotation Sweep", "secret-rotation-sweep.md", "prompts/bootstrap-govern-secret-rotation.md",
        [("secret-rotation-sweep.md", "coordinator"), ("rotation-record-template.md", "rotation record")],
    ))

    write("patterns/license-policy-gate/license-policy-gate.md", """# License Policy Gate

Merge/release gate on dependency licenses against project policy.

Uses [`license-policy-template`](../../primitives/license-policy-template/license-policy-template.md).

## Output

```yaml
verdict: pass | fail | review-required
violations: [{dep, license, action}]
```

Integrates with ship-checklist and release-coordinator.
""")

    write("patterns/license-policy-gate/README.md", readme(
        "License Policy Gate", "license-policy-gate.md", "prompts/bootstrap-govern-license-gate.md",
        [("license-policy-gate.md", "gate evaluator")],
    ))

    gov = [
        ("govern-oss", "govern", "OSS hygiene", "repo_type: oss | internal", "patterns/oss-hygiene/oss-hygiene.md"),
        ("govern-labels", "govern", "label policy enforcement", "mode: audit | fix\npolicy: <path>", "patterns/label-policy-enforcement/label-policy-enforcement.md"),
        ("govern-secret-rotation", "govern", "secret rotation sweep", "paths: []  # optional", "patterns/secret-rotation-sweep/secret-rotation-sweep.md"),
        ("govern-license-gate", "govern", "license policy gate", "policy: <path to license-policy-template>", "patterns/license-policy-gate/license-policy-gate.md"),
    ]
    gov_manifests = {
        "govern-oss": (["patterns/oss-hygiene/oss-hygiene.md", "patterns/oss-hygiene/oss-hygiene-checklist.md"], None),
        "govern-labels": (["patterns/label-policy-enforcement/label-policy-enforcement.md", "adapters/issue-label-normalization/domain-adapter.md", "adapters/issue-label-normalization/label-policy-template.md"], None),
        "govern-secret-rotation": (["patterns/secret-rotation-sweep/secret-rotation-sweep.md", "auditors/secrets-hygiene/persona.md"], None),
        "govern-license-gate": (["patterns/license-policy-gate/license-policy-gate.md", "primitives/license-policy-template/license-policy-template.md", "patterns/ship-checklist/ship-checklist.md"], None),
    }
    for name, family, title, config, pattern in gov:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern))
        files, opt = gov_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))
    print("Govern family done.")


def generate_decide() -> None:
    write("patterns/spike-coordinator/spike-coordinator.md", """# Spike Coordinator

Time-boxed exploration: options, evidence, recommendation. **Explicit no-merge default.**

## Loop

1. Define question and time box
2. Optional: repo-archaeology or blast-radius input
3. Spawn [`spike-worker`](spike-worker.md) per option or evidence gather
4. Output [`decision-record-schema`](../../primitives/decision-record-schema/decision-record.md)
5. Optional: promote follow-ups to issues/CCM — no production commits

## Rules

- `no_commit: true` unless user explicitly overrides
- Options matrix required
""")

    write("patterns/spike-coordinator/spike-worker.md", """# Spike Worker

Gather evidence for one option or hypothesis.

Read-only by default. Return evidence bullets — no implementation.
""")

    write("patterns/spike-coordinator/README.md", readme(
        "Spike Coordinator", "spike-coordinator.md", "prompts/bootstrap-decide-spike.md",
        [("spike-coordinator.md", "coordinator"), ("spike-worker.md", "worker")],
    ))

    write("patterns/build-vs-buy/build-vs-buy.md", """# Build vs Buy

Structured comparison specialization of spike-coordinator.

Fill [`comparison-matrix-template.md`](comparison-matrix-template.md):

Cost, security, maintenance, lock-in, fit.

Output decision record with recommendation and non-goals.
""")

    write("patterns/build-vs-buy/comparison-matrix-template.md", """# Build vs Buy Matrix

| Criterion | Build | Buy / Adopt |
|-----------|-------|-------------|
| Cost (initial + ongoing) | | |
| Security / compliance | | |
| Maintenance burden | | |
| Lock-in risk | | |
| Fit to requirements | | |

**Recommendation:**
**Non-goals:**
""")

    write("patterns/build-vs-buy/README.md", readme(
        "Build vs Buy", "build-vs-buy.md", "prompts/bootstrap-decide-build-vs-buy.md",
        [("build-vs-buy.md", "coordinator"), ("comparison-matrix-template.md", "matrix template")],
    ))

    write("patterns/threat-modeling-lite/threat-modeling-lite.md", """# Threat Modeling Lite

STRIDE-lite per module/boundary → ranked threats → mitigations or spikes.

Read-only. File issues in separate phase if configured.

Uses [`threat-record-template.md`](threat-record-template.md).
""")

    write("patterns/threat-modeling-lite/threat-record-template.md", """# Threat Record Template

```yaml
component: string
threats:
  - category: spoofing | tampering | repudiation | information_disclosure | denial_of_service | elevation
    description: string
    rank: high | medium | low
    mitigation: string | accept-with-justification
```
""")

    write("patterns/threat-modeling-lite/README.md", readme(
        "Threat Modeling Lite", "threat-modeling-lite.md", "prompts/bootstrap-decide-threat-model.md",
        [("threat-modeling-lite.md", "coordinator"), ("threat-record-template.md", "threat record")],
    ))

    dec = [
        ("decide-spike", "decide", "spike coordinator", "question: <description>\ntimebox_hours: 4", "patterns/spike-coordinator/spike-coordinator.md"),
        ("decide-build-vs-buy", "decide", "build vs buy", "capability: <description>", "patterns/build-vs-buy/build-vs-buy.md"),
        ("decide-threat-model", "decide", "threat modeling lite", "scope: <module or boundary>", "patterns/threat-modeling-lite/threat-modeling-lite.md"),
    ]
    dec_manifests = {
        "decide-spike": (["patterns/spike-coordinator/spike-coordinator.md", "patterns/spike-coordinator/spike-worker.md", "primitives/decision-record-schema/decision-record.md"], ["patterns/repo-archaeology/repo-archaeology.md"]),
        "decide-build-vs-buy": (["patterns/build-vs-buy/build-vs-buy.md", "patterns/spike-coordinator/spike-coordinator.md", "primitives/decision-record-schema/decision-record.md"], None),
        "decide-threat-model": (["patterns/threat-modeling-lite/threat-modeling-lite.md", "primitives/decision-record-schema/decision-record.md"], ["auditors/network-segmentation-policy/persona.md"]),
    }
    for name, family, title, config, pattern in dec:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern))
        files, opt = dec_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))
    print("Decide family done.")


def generate_operate() -> None:
    write("patterns/deploy-smoke-coordinator/deploy-smoke-coordinator.md", """# Deploy Smoke Coordinator

Post-deploy smoke checks: health endpoints, critical paths, rollback triggers.

Follow [`operate-safety`](../../primitives/operate-safety/operate-safety.md). Read-only unless explicit deploy approval.

Uses [`smoke-checklist.md`](smoke-checklist.md) and [`smoke-result-schema`](../../primitives/smoke-result-schema/smoke-result-schema.md).

Pairs with rollback-plan output.
""")

    write("patterns/deploy-smoke-coordinator/smoke-checklist.md", """# Smoke Checklist

| Check | Type | Command / URL | Pass criteria |
|-------|------|---------------|---------------|
| Health endpoint | health | GET /health | 200 |
| Critical path | critical-path | | |
| Integration | integration | | |

Document rollback trigger conditions.
""")

    write("patterns/deploy-smoke-coordinator/README.md", readme(
        "Deploy Smoke Coordinator", "deploy-smoke-coordinator.md", "prompts/bootstrap-operate-deploy-smoke.md",
        [("deploy-smoke-coordinator.md", "coordinator"), ("smoke-checklist.md", "checklist")],
    ))

    write("patterns/slo-error-budget-review/slo-error-budget-review.md", """# SLO / Error Budget Review

Review SLOs, error budgets, alert noise from metrics/logs when available.

Read-only on metrics sources. Action items as suggestions only.

Use [`slo-review-template.md`](slo-review-template.md). Template branch when metrics unavailable.
""")

    write("patterns/slo-error-budget-review/slo-review-template.md", """# SLO Review Template

```markdown
## SLOs
| SLI | Target | Current | Budget remaining |

## Alert noise
-

## Recommendations
-
```
""")

    write("patterns/slo-error-budget-review/README.md", readme(
        "SLO Error Budget Review", "slo-error-budget-review.md", "prompts/bootstrap-operate-slo.md",
        [("slo-error-budget-review.md", "review"), ("slo-review-template.md", "template")],
    ))

    write("patterns/cost-review/cost-review.md", """# Cost Review

Review cloud cost drivers, overprovisioned resources, idle assets. Read-only.

Output [`cost-finding-schema`](../../primitives/cost-finding-schema/cost-finding-schema.md).

No automatic resource deletion. Evidence from billing export or manifest review only.
""")

    write("patterns/cost-review/cost-review-template.md", """# Cost Review Template

```markdown
## Period
## Sources reviewed

## Findings
| Category | Resource | Savings est. | Risk |

## Ranked recommendations
```
""")

    write("patterns/cost-review/README.md", readme(
        "Cost Review", "cost-review.md", "prompts/bootstrap-operate-cost.md",
        [("cost-review.md", "review"), ("cost-review-template.md", "template")],
    ))

    op = [
        ("operate-deploy-smoke", "operate", "deploy smoke coordinator", "environment: staging | production\nbase_url: <url>", "patterns/deploy-smoke-coordinator/deploy-smoke-coordinator.md"),
        ("operate-slo", "operate", "SLO error budget review", "metrics_source: <optional>", "patterns/slo-error-budget-review/slo-error-budget-review.md"),
        ("operate-cost", "operate", "cost review", "period: <YYYY-MM>  # optional", "patterns/cost-review/cost-review.md"),
    ]
    op_manifests = {
        "operate-deploy-smoke": (["patterns/deploy-smoke-coordinator/deploy-smoke-coordinator.md", "patterns/deploy-smoke-coordinator/smoke-checklist.md", "primitives/operate-safety/operate-safety.md", "primitives/smoke-result-schema/smoke-result-schema.md", "patterns/rollback-plan/rollback-plan.md"], None),
        "operate-slo": (["patterns/slo-error-budget-review/slo-error-budget-review.md", "patterns/slo-error-budget-review/slo-review-template.md", "primitives/operate-safety/operate-safety.md", "auditors/observability-readiness/persona.md"], None),
        "operate-cost": (["patterns/cost-review/cost-review.md", "patterns/cost-review/cost-review-template.md", "primitives/cost-finding-schema/cost-finding-schema.md", "primitives/operate-safety/operate-safety.md"], None),
    }
    for name, family, title, config, pattern in op:
        write(f"prompts/bootstrap-{name}.md", bootstrap(name, family, title, config, pattern))
        files, opt = op_manifests[name]
        write(f"prompts/manifests/{name}-manifest.md", manifest(name, files, opt))
    print("Operate family done.")


if __name__ == "__main__":
    main()
    generate_communicate()
    generate_transform()
    generate_generate()
    generate_govern()
    generate_decide()
    generate_operate()
    print("All families generated.")
