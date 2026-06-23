#!/usr/bin/env python3
"""Create workflow epic and sub-issues on GarrettEHill/prompt-tools. Run once."""
import json
import subprocess
import tempfile
from pathlib import Path

REPO = "GarrettEHill/prompt-tools"

EPICS = [
    {
        "key": "map",
        "title": "[Epic] Map — Understand workflows",
        "labels": "epic,workflow-map,meta",
        "body": """## Summary

Epic for **Map** workflow family: read-only understanding of a repository before change, audit, or remediation.

## Meta-pattern

```text
coordinator + disposable map specialists + compact map notes + handoff to audit/CCM/spike
```

## Sub-issues (this epic)

- [ ] Repo archaeology
- [ ] Onboarding brief
- [ ] Decision archaeology
- [ ] Blast radius analysis

## Packaging (per sub-issue)

```text
prompts/SNIPPET-map-<name>.md
prompts/bootstrap-map-<name>.md
prompts/manifests/map-<name>-manifest.md
patterns/map-<name>/ OR patterns/<coordinator>/
specialists/ or personas/
primitives/map-result-schema (shared)
```

## Relationship to existing tools

- **Upstream of:** divide-and-conquer-audit, spike coordinator, CCM
- **Distinct from:** audit (finds problems), archaeology (builds mental model)

## Epic acceptance criteria

- [ ] Shared `primitives/map-result-schema` or reuse compact-result with map types
- [ ] Remote bootstrap pattern like audit (fetch from main, no target-repo integration)
- [ ] README workflow family table includes Map
- [ ] At least one sub-issue implemented end-to-end
""",
    },
    {
        "key": "ship",
        "title": "[Epic] Ship — Release readiness workflows",
        "labels": "epic,workflow-ship,meta",
        "body": """## Summary

Epic for **Ship** workflow family: version-cut readiness — changelog, breaking changes, migrations, go/no-go.

## Meta-pattern

Coordinator validates release gate checklist; workers verify slices; output is **ship decision + release PR bundle**, not an open-ended backlog.

## Sub-issues

- [ ] Release coordinator
- [ ] Ship checklist
- [ ] Rollback plan generator

## Distinct from audit

Audit finds health gaps; Ship answers **can we tag vX.Y.Z today**.

## Epic acceptance criteria

- [ ] Remote bootstrap snippet for release runs
- [ ] Handoff to CCM for blockers found during ship gate
- [ ] README documents Ship family
""",
    },
    {
        "key": "investigate",
        "title": "[Epic] Investigate — Failure and regression workflows",
        "labels": "epic,workflow-investigate,meta",
        "body": """## Summary

Epic for **Investigate** workflow family: narrow, time-sensitive failure analysis (CI flake, regression, incident).

## Meta-pattern

Stop when root cause is identified or mitigated — not when a full queue is empty.

## Sub-issues

- [ ] Regression hunt
- [ ] Incident coordinator
- [ ] Flake hunter
- [ ] Postmortem generator

## Relationship

Extends `investigation-before-change` pattern; pairs with `failing-ci-remediation` adapter.

## Epic acceptance criteria

- [ ] Investigation result schema (distinct from audit finding)
- [ ] Remote bootstrap for incident/regression entry
""",
    },
    {
        "key": "transform",
        "title": "[Epic] Transform — Migration and change at scale",
        "labels": "epic,workflow-transform,meta",
        "body": """## Summary

Epic for **Transform** workflow family: planned migrations (framework upgrades, API versions, deprecations, codemods).

## Meta-pattern

Same CCM loop but queue is **migration units** (call sites, modules, schemas), not audit findings.

## Sub-issues

- [ ] Migration sweep
- [ ] Deprecation enforcer
- [ ] Codemod coordinator
- [ ] Config drift fix

## Epic acceptance criteria

- [ ] Migration unit decomposition primitive
- [ ] Validation ladder integration for mechanical changes
""",
    },
    {
        "key": "review",
        "title": "[Epic] Review — Change-scoped judgment workflows",
        "labels": "epic,workflow-review,meta",
        "body": """## Summary

Epic for **Review** workflow family: PR-scoped review with composable reviewer personas.

## Meta-pattern

One PR (or diff) per worker; personas = security, API compat, design, deps.

## Sub-issues

- [ ] PR review personas
- [ ] Design review
- [ ] Dependency review

## Epic acceptance criteria

- [ ] Remote snippet: review PR #N using latest prompt-tools
- [ ] Review result schema (approve/block/comment with evidence)
""",
    },
    {
        "key": "generate",
        "title": "[Epic] Generate — Artifacts from truth",
        "labels": "epic,workflow-generate,meta",
        "body": """## Summary

Epic for **Generate** workflow family: produce docs, runbooks, changelogs, specs from repository truth.

## Meta-pattern

Read source → generate artifact → validate artifact against source (round-trip check).

## Sub-issues

- [ ] Doc sync
- [ ] Runbook generator
- [ ] Changelog from reality
- [ ] OpenAPI drift fix (generative)

## Epic acceptance criteria

- [ ] Generative outputs require validation step before commit
""",
    },
    {
        "key": "govern",
        "title": "[Epic] Govern — Policy and hygiene workflows",
        "labels": "epic,workflow-govern,meta",
        "body": """## Summary

Epic for **Govern** workflow family: ongoing policy enforcement (OSS hygiene, labels, secrets rotation, license gates).

## Meta-pattern

Like audit but **policy-centric** and often recurring; may integrate with CI gates.

## Sub-issues

- [ ] OSS hygiene
- [ ] Label/policy enforcement
- [ ] Secret rotation sweep
- [ ] License policy gate

## Epic acceptance criteria

- [ ] Distinct from one-shot audit — supports scheduled re-runs
""",
    },
    {
        "key": "decide",
        "title": "[Epic] Decide — Explore without committing",
        "labels": "epic,workflow-decide,meta",
        "body": """## Summary

Epic for **Decide** workflow family: spikes, build-vs-buy, threat modeling — output is **decision record**, not merged code.

## Meta-pattern

Read-only or time-boxed; mandatory recommendation + options matrix; no PR unless explicitly promoted.

## Sub-issues

- [ ] Spike coordinator
- [ ] Build vs buy
- [ ] Threat modeling lite

## Epic acceptance criteria

- [ ] Decision record schema and template
- [ ] Explicit no-merge rules in coordinator
""",
    },
    {
        "key": "operate",
        "title": "[Epic] Operate — Runtime and production workflows",
        "labels": "epic,workflow-operate,meta",
        "body": """## Summary

Epic for **Operate** workflow family: post-deploy smoke, SLO/error budget, cost review.

## Meta-pattern

Read-only on live systems where possible; strict no-production-risk boundaries.

## Sub-issues

- [ ] Deploy smoke coordinator
- [ ] SLO/error budget review
- [ ] Cost review

## Epic acceptance criteria

- [ ] Safety primitive for production access boundaries
""",
    },
    {
        "key": "communicate",
        "title": "[Epic] Communicate — Audience beyond the repo",
        "labels": "epic,workflow-communicate,meta",
        "body": """## Summary

Epic for **Communicate** workflow family: executive briefs, umbrella issue composition, stakeholder status.

## Meta-pattern

Consumes compact results from audit/CCM/investigate; produces human-facing summaries.

## Sub-issues

- [ ] Executive brief
- [ ] Umbrella issue composer
- [ ] Stakeholder status

## Relationship

Extends `final-report` pattern; links to `umbrella-issue-completion` adapter.

## Epic acceptance criteria

- [ ] Input schema from other workflow outputs
""",
    },
]

def sub_body(epic_title: str, epic_num: int, **kwargs) -> str:
    return f"""## Summary

{kwargs['summary']}

**Epic:** #{epic_num} — {epic_title}

## Why this belongs in prompt-tools

{kwargs['why']}

## Problem

{kwargs['problem']}

## Proposed contents

{kwargs['contents']}

## Remote bootstrap (target-repo agnostic)

```text
prompts/bootstrap-{kwargs['bootstrap']}.md
prompts/manifests/{kwargs['bootstrap']}-manifest.md
prompts/SNIPPET.md (add snippet block)
```

Fetch from `https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/` at runtime.

## Relationship to existing patterns

{kwargs['relationships']}

## Acceptance criteria

{kwargs['acceptance']}

## Labels

`pattern` or `primitive`, `{kwargs['workflow_label']}`, `enhancement`
"""


SUBS = {
    "map": [
        {
            "title": "Add Repo archaeology pattern",
            "bootstrap": "map-archaeology",
            "workflow_label": "workflow-map",
            "summary": "Read-only coordinator that maps repository structure, entrypoints, data flows, and 'where to start' for humans and agents.",
            "why": "Every audit, CCM sweep, or spike needs a mental model. Archaeology runs before change and produces a durable map artifact.",
            "problem": "Agents and contributors waste context re-discovering layout, boundaries, and critical paths on every session.",
            "contents": """```text
patterns/repo-archaeology/
  README.md
  repo-archaeology.md          # coordinator loop
  disposable-mapper.md         # one module/area per worker
  map-scope-discovery.md
primitives/map-result-schema/
  map-result-schema.md         # module, entrypoints, deps, risks
specialists/ or personas/
  api-surface-mapper/persona.md
  data-flow-mapper/persona.md
  deploy-topology-mapper/persona.md
prompts/bootstrap-map-archaeology.md
prompts/manifests/map-archaeology-manifest.md
```""",
            "relationships": "- **Feeds:** divide-and-conquer-audit (scope discovery), onboarding brief\n- **Uses:** live-state-refresh, compact result discipline\n- **Distinct from:** documentation-accuracy (validates commands, not structure)",
            "acceptance": """- [ ] `patterns/repo-archaeology/` with coordinator + mapper shell
- [ ] Map result schema with module graph fields
- [ ] Remote bootstrap + SNIPPET block
- [ ] README workflow family entry
- [ ] Example output for a monorepo and a single-app repo""",
        },
        {
            "title": "Add Onboarding brief pattern",
            "bootstrap": "map-onboarding",
            "workflow_label": "workflow-map",
            "summary": "Generate a 1–2 page onboarding brief: how to build, test, deploy, debug, and where key docs live.",
            "why": "Standardizes first-day orientation for humans and agents; reduces repeated exploration.",
            "problem": "READMEs are uneven; onboarding knowledge is tribal and scattered.",
            "contents": """```text
patterns/onboarding-brief/
  onboarding-brief.md
  brief-template.md
prompts/bootstrap-map-onboarding.md
```""",
            "relationships": "- **Consumes:** repo-archaeology output if available\n- **Pairs with:** documentation-accuracy findings",
            "acceptance": """- [ ] Brief template with required sections (build, test, deploy, debug, layout)
- [ ] Remote bootstrap
- [ ] Validates documented commands where safe (read-only spot-check)""",
        },
        {
            "title": "Add Decision archaeology pattern",
            "bootstrap": "map-decisions",
            "workflow_label": "workflow-map",
            "summary": "Extract implicit technical decisions from ADRs, comments, DESIGN docs, and code structure into a decision register.",
            "why": "Surfaces why the system looks the way it does — critical before refactors and audits.",
            "problem": "Decisions are buried in PR history, comments, and unstated conventions.",
            "contents": """```text
patterns/decision-archaeology/
  decision-archaeology.md
  decision-record-template.md
primitives/decision-register-schema/
```""",
            "relationships": "- **Feeds:** spike coordinator, design review\n- **Pairs with:** requirements-traceability auditor persona",
            "acceptance": """- [ ] Decision register schema\n- [ ] Coordinator scans ADR/DESIGN/CHANGELOG locations\n- [ ] Output links decisions to files/modules""",
        },
        {
            "title": "Add Blast radius analysis pattern",
            "bootstrap": "map-blast-radius",
            "workflow_label": "workflow-map",
            "summary": "For a proposed change target (file/module/API), map affected tests, deploy surfaces, and dependents.",
            "why": "Answers 'if I touch X, what breaks?' before implementation.",
            "problem": "Agents and devs make changes without understanding downstream impact.",
            "contents": """```text
patterns/blast-radius/
  blast-radius.md
  blast-radius-template.md
```""",
            "relationships": "- **Input:** user-supplied target path/symbol\n- **Uses:** architecture-boundaries persona, test-quality persona\n- **Feeds:** CCM worker scope validation",
            "acceptance": """- [ ] Template output: dependents, tests, deploy, API consumers\n- [ ] Remote bootstrap accepting `target:` in config\n- [ ] Read-only analysis only""",
        },
    ],
    "ship": [
        {
            "title": "Add Release coordinator pattern",
            "bootstrap": "ship-release",
            "workflow_label": "workflow-ship",
            "summary": "Coordinator for a version cut: version bump, changelog, breaking-change scan, migration notes, release PR.",
            "why": "Releases are recurring and error-prone; need same discipline as audit/CCM.",
            "problem": "Release steps are ad-hoc; breaking changes and docs drift ship unnoticed.",
            "contents": """```text
patterns/release-coordinator/
  release-coordinator.md
  release-worker.md
  release-checklist.md
adapters/semver-release/
  domain-adapter.md
prompts/bootstrap-ship-release.md
```""",
            "relationships": "- **Uses:** git-github-safety, validation-ladder\n- **Consumes:** changelog-from-reality (generate family)\n- **Handoff:** CCM for blockers",
            "acceptance": """- [ ] Coordinator loop for release PR assembly\n- [ ] Breaking change scan step\n- [ ] Go/no-go output\n- [ ] Remote bootstrap with `version:` config""",
        },
        {
            "title": "Add Ship checklist pattern",
            "bootstrap": "ship-checklist",
            "workflow_label": "workflow-ship",
            "summary": "Gate checklist: required CI green, docs updated, migrations noted, deprecations handled, audit blockers resolved.",
            "why": "Separates 'are we allowed to ship' from 'cut the release'.",
            "problem": "Teams ship with failing checks or missing migration notes.",
            "contents": """```text
patterns/ship-checklist/
  ship-checklist.md
  gate-template.md
primitives/ship-gate-schema/
```""",
            "relationships": "- **Used by:** release-coordinator\n- **Pulls from:** open audit-finding issues, failing CI adapter signals",
            "acceptance": """- [ ] Checklist with pass/fail/blocked per gate\n- [ ] Configurable required checks list\n- [ ] Compact gate result schema""",
        },
        {
            "title": "Add Rollback plan generator pattern",
            "bootstrap": "ship-rollback",
            "workflow_label": "workflow-ship",
            "summary": "Generate rollback plan from deploy manifests, migrations, and release diff.",
            "why": "Every release should have documented rollback before deploy.",
            "problem": "Rollback is improvised during incidents.",
            "contents": """```text
patterns/rollback-plan/
  rollback-plan.md
  rollback-template.md
```""",
            "relationships": "- **Pairs with:** container-runtime-hardening, database-migration-hygiene\n- **Used by:** deploy-smoke coordinator (operate)",
            "acceptance": """- [ ] Template: revert steps, migration down, config restore\n- [ ] Read-only generation; no deploy actions""",
        },
    ],
    "investigate": [
        {
            "title": "Add Regression hunt pattern",
            "bootstrap": "investigate-regression",
            "workflow_label": "workflow-investigate",
            "summary": "Coordinator for bisect-style regression: reproduce → narrow commit range → hypothesize → report.",
            "why": "Distinct from broad audit; optimized for 'it broke recently'.",
            "problem": "Agents jump to fixes without narrowing regression window.",
            "contents": """```text
patterns/regression-hunt/
  regression-hunt.md
  regression-worker.md
primitives/investigation-result-schema/
prompts/bootstrap-investigate-regression.md
```""",
            "relationships": "- **Extends:** investigation-before-change\n- **Pairs with:** failing-ci-remediation adapter",
            "acceptance": """- [ ] Investigation result schema\n- [ ] Stop rules: root cause or blocked\n- [ ] Git log/read-only bisect guidance""",
        },
        {
            "title": "Add Incident coordinator pattern",
            "bootstrap": "investigate-incident",
            "workflow_label": "workflow-investigate",
            "summary": "Incident response coordinator: timeline, evidence collection, impact, immediate mitigations (document only).",
            "why": "Structured incident handling for agent-assisted response.",
            "problem": "Chaotic incident chats lose timeline and evidence.",
            "contents": """```text
patterns/incident-coordinator/
  incident-coordinator.md
  incident-timeline-template.md
```""",
            "relationships": "- **Feeds:** postmortem generator\n- **Safety:** no production changes without explicit user approval",
            "acceptance": """- [ ] Timeline template\n- [ ] Severity/impact fields\n- [ ] Mitigation vs fix distinction""",
        },
        {
            "title": "Add Flake hunter pattern",
            "bootstrap": "investigate-flake",
            "workflow_label": "workflow-investigate",
            "summary": "Focused workflow for intermittent CI failures: reproduce, classify flake vs env vs bug.",
            "why": "Flakes waste CCM cycles if treated as normal bugs.",
            "problem": "Flaky tests are misclassified as code defects.",
            "contents": """```text
patterns/flake-hunter/
  flake-hunter.md
  flake-classification.md
```""",
            "relationships": "- **Routes to:** CCM implement OR quarantine policy OR blocked\n- **Uses:** test-quality persona",
            "acceptance": """- [ ] Classification outcomes: flake, env, deterministic bug\n- [ ] Evidence requirements for quarantine recommendation""",
        },
        {
            "title": "Add Postmortem generator pattern",
            "bootstrap": "investigate-postmortem",
            "workflow_label": "workflow-investigate",
            "summary": "Blameless postmortem from compact investigation/incident results.",
            "why": "Closes the investigate loop with durable learning artifacts.",
            "problem": "Incidents end without written postmortems.",
            "contents": """```text
patterns/postmortem/
  postmortem-template.md
  postmortem-generator.md
```""",
            "relationships": "- **Consumes:** investigation-result-schema, incident timeline\n- **Optional:** create follow-up issues via issue-generation pattern",
            "acceptance": """- [ ] Blameless template (timeline, root cause, action items)\n- [ ] Action items linkable to GitHub issues""",
        },
    ],
    "transform": [
        {
            "title": "Add Migration sweep pattern",
            "bootstrap": "transform-migration",
            "workflow_label": "workflow-transform",
            "summary": "CCM-style coordinator for framework/API migrations: queue migration units, worker per unit, validate per ladder.",
            "why": "Migrations are queue-shaped like audit remediation but different adapters.",
            "problem": "Big-bang migrations stall; need item-by-item migration loop.",
            "contents": """```text
patterns/migration-sweep/
  migration-sweep.md
  migration-worker.md
  migration-unit-template.md
adapters/framework-upgrade/
  domain-adapter.md
```""",
            "relationships": "- **Parallel to:** continuous-completion-model\n- **Uses:** work-item-decomposition, validation-ladder",
            "acceptance": """- [ ] Migration unit definition in adapter template\n- [ ] CCM-compatible handoff from migration plan\n- [ ] Remote bootstrap""",
        },
        {
            "title": "Add Deprecation enforcer pattern",
            "bootstrap": "transform-deprecation",
            "workflow_label": "workflow-transform",
            "summary": "Find usages of deprecated APIs/symbols; queue removals; verify zero usages before deleting exports.",
            "why": "Deprecation without enforcement rots.",
            "problem": "Deprecated code never gets removed.",
            "contents": """```text
patterns/deprecation-enforcer/
  deprecation-enforcer.md
  deprecation-adapter-template.md
```""",
            "relationships": "- **Specialization of:** migration-sweep\n- **Uses:** architecture-boundaries persona",
            "acceptance": """- [ ] Usage scan + queue + verify-empty steps\n- [ ] Adapter template for @deprecated, feature flags, etc.""",
        },
        {
            "title": "Add Codemod coordinator pattern",
            "bootstrap": "transform-codemod",
            "workflow_label": "workflow-transform",
            "summary": "Coordinate mechanical codemods across modules with per-chunk validation.",
            "why": "Codemods need CCM discipline to avoid giant broken PRs.",
            "problem": "Repo-wide codemods fail CI or get abandoned mid-way.",
            "contents": """```text
patterns/codemod-coordinator/
  codemod-coordinator.md
  codemod-worker.md
```""",
            "relationships": "- **Uses:** migration-sweep, validation-ladder\n- **Chunking:** work-item-decomposition",
            "acceptance": """- [ ] One module/directory per worker default\n- [ ] Rollback on validation failure per chunk""",
        },
        {
            "title": "Add Config drift fix pattern",
            "bootstrap": "transform-config-drift",
            "workflow_label": "workflow-transform",
            "summary": "Align env templates, compose profiles, CI matrices — detect drift and queue fixes.",
            "why": "Config drift causes 'works on my machine' and deploy surprises.",
            "problem": "`.env.example`, compose overrides, and CI configs diverge silently.",
            "contents": """```text
patterns/config-drift-fix/
  config-drift-fix.md
adapters/env-compose-ci-drift/
  domain-adapter.md
```""",
            "relationships": "- **Audited by:** secrets-hygiene, container-runtime personas\n- **Execute via:** CCM",
            "acceptance": """- [ ] Drift detection checklist\n- [ ] Adapter for env/compose/ci trio""",
        },
    ],
    "review": [
        {
            "title": "Add PR review personas system",
            "bootstrap": "review-pr",
            "workflow_label": "workflow-review",
            "summary": "Composable PR reviewer personas (security, API compat, tests, design) — one PR per coordinator run.",
            "why": "Mirrors auditor persona model for daily PR review.",
            "problem": "Generic PR review misses domain risks.",
            "contents": """```text
patterns/pr-review/
  pr-review-coordinator.md
  disposable-reviewer.md
reviewers/
  security-reviewer/persona.md
  api-compat-reviewer/persona.md
  test-adequacy-reviewer/persona.md
  design-reviewer/persona.md
primitives/review-result-schema/
prompts/bootstrap-review-pr.md
```""",
            "relationships": "- **Parallel to:** disposable-auditor + auditors/\n- **Input:** PR number or branch diff",
            "acceptance": """- [ ] Review result schema (approve/request-changes/block + evidence)\n- [ ] 4 starter personas\n- [ ] SNIPPET: review PR #N remotely""",
        },
        {
            "title": "Add Design review pattern",
            "bootstrap": "review-design",
            "workflow_label": "workflow-review",
            "summary": "Verify PR aligns with DESIGN.md / ADRs / architecture boundaries.",
            "why": "Catches architectural drift before merge.",
            "problem": "Design docs are ignored during review.",
            "contents": """```text
patterns/design-review/
  design-review.md
reviewers/design-reviewer/persona.md  # may merge with above
```""",
            "relationships": "- **Uses:** requirements-traceability, architecture-boundaries\n- **Pairs with:** PR review personas",
            "acceptance": """- [ ] Checklist: design doc citations, boundary violations\n- [ ] Output links PR to violated design clauses""",
        },
        {
            "title": "Add Dependency review pattern",
            "bootstrap": "review-dependency",
            "workflow_label": "workflow-review",
            "summary": "PR-scoped dependency diff review: new deps, license, CVE, supply chain risk.",
            "why": "Dependency changes need focused review beyond generic security.",
            "problem": "Lockfile-only PRs get rubber-stamped.",
            "contents": """```text
patterns/dependency-review/
  dependency-review.md
reviewers/dependency-reviewer/persona.md
```""",
            "relationships": "- **Uses:** dependency-supply-chain persona scoped to PR diff\n- **Pairs with:** license-compliance",
            "acceptance": """- [ ] PR lockfile/manifest diff scope\n- [ ] CVE/license/new-dep classification in review result""",
        },
    ],
    "generate": [
        {
            "title": "Add Doc sync pattern",
            "bootstrap": "generate-doc-sync",
            "workflow_label": "workflow-generate",
            "summary": "Generate or update docs from source (API surface, config, commands) with round-trip validation.",
            "why": "Generative complement to documentation-accuracy auditor.",
            "problem": "Docs drift; manual updates lag code.",
            "contents": """```text
patterns/doc-sync/
  doc-sync.md
  doc-sync-template.md
```""",
            "relationships": "- **Validated by:** documentation-accuracy persona\n- **Distinct from:** docs-backlog CCM adapter (fixes issues)",
            "acceptance": """- [ ] Round-trip check: generated doc matches code\n- [ ] PR-only output; user approves merge""",
        },
        {
            "title": "Add Runbook generator pattern",
            "bootstrap": "generate-runbook",
            "workflow_label": "workflow-generate",
            "summary": "Generate operability runbooks from compose, scripts, and deploy manifests.",
            "why": "Ops knowledge should be derived from actual deploy artifacts.",
            "problem": "Runbooks are stale or missing for compose/k8s stacks.",
            "contents": """```text
patterns/runbook-generator/
  runbook-generator.md
  runbook-template.md
```""",
            "relationships": "- **Ideal for:** Xyberus-style compose stacks\n- **Uses:** container-runtime, observability personas as input",
            "acceptance": """- [ ] Runbook sections: start, stop, logs, health, rollback link\n- [ ] Citations to compose/script paths""",
        },
        {
            "title": "Add Changelog from reality pattern",
            "bootstrap": "generate-changelog",
            "workflow_label": "workflow-generate",
            "summary": "Build changelog from merged PRs, commits, and labels since last tag.",
            "why": "Release coordinator needs accurate changelog source.",
            "problem": "Manual changelogs omit changes or misclassify breaking fixes.",
            "contents": """```text
patterns/changelog-from-reality/
  changelog-from-reality.md
  changelog-template.md
```""",
            "relationships": "- **Used by:** release-coordinator\n- **Input:** `gh` git range since tag",
            "acceptance": """- [ ] Conventional sections: breaking, feat, fix, deps\n- [ ] Links PRs/issues\n- [ ] Config: `since_tag:`""",
        },
        {
            "title": "Add OpenAPI drift fix (generative) pattern",
            "bootstrap": "generate-openapi",
            "workflow_label": "workflow-generate",
            "summary": "Generate or patch OpenAPI/spec to match handlers (inverse of openapi-api-surface audit).",
            "why": "Closes the loop when audit finds spec drift.",
            "problem": "Specs are updated manually and lag routes.",
            "contents": """```text
patterns/openapi-drift-fix/
  openapi-drift-fix.md
```""",
            "relationships": "- **Pairs with:** openapi-api-surface persona, schema-contract-drift\n- **Validate:** spec matches routes after generation",
            "acceptance": """- [ ] Read handlers → update spec → validate\n- [ ] PR with spec + optional client regen""",
        },
    ],
    "govern": [
        {
            "title": "Add OSS hygiene pattern",
            "bootstrap": "govern-oss",
            "workflow_label": "workflow-govern",
            "summary": "Enforce OSS repo hygiene: LICENSE, CONTRIBUTING, CODEOWNERS, issue/PR templates, SECURITY.md.",
            "why": "Recurring governance distinct from security audit.",
            "problem": "OSS repos ship without standard community files.",
            "contents": """```text
patterns/oss-hygiene/
  oss-hygiene.md
  oss-hygiene-checklist.md
```""",
            "relationships": "- **Related:** license-compliance persona\n- **May file:** issues or open PRs per config",
            "acceptance": """- [ ] Checklist with evidence per file\n- [ ] Adapter for OSS vs internal repo policy""",
        },
        {
            "title": "Add Label/policy enforcement pattern",
            "bootstrap": "govern-labels",
            "workflow_label": "workflow-govern",
            "summary": "Recurring enforcement of issue label taxonomy (extends issue-label-normalization adapter for scheduled runs).",
            "why": "Label drift is ongoing; not one-shot.",
            "problem": "Issues accumulate wrong labels between audits.",
            "contents": """```text
patterns/label-policy-enforcement/
  label-policy-enforcement.md
adapters/issue-label-normalization/  # extend
```""",
            "relationships": "- **Extends:** issue-label-normalization adapter\n- **CCM-compatible** for fixes",
            "acceptance": """- [ ] Scheduled sweep mode in adapter\n- [ ] Policy template required before run""",
        },
        {
            "title": "Add Secret rotation sweep pattern",
            "bootstrap": "govern-secret-rotation",
            "workflow_label": "workflow-govern",
            "summary": "Beyond secrets-hygiene audit: rotation due dates, exposed-in-history signals, CI secret scope review.",
            "why": "Finding secrets is step one; rotation governance is step two.",
            "problem": "No process for aging credentials.",
            "contents": """```text
patterns/secret-rotation-sweep/
  secret-rotation-sweep.md
  rotation-record-template.md
```""",
            "relationships": "- **Builds on:** secrets-hygiene persona\n- **Does not:** rotate secrets automatically without explicit approval",
            "acceptance": """- [ ] Rotation record template\n- [ ] Classify: rotate, revoke, false-positive\n- [ ] Never prints secret values""",
        },
        {
            "title": "Add License policy gate pattern",
            "bootstrap": "govern-license-gate",
            "workflow_label": "workflow-govern",
            "summary": "Merge/release gate on dependency licenses against project policy.",
            "why": "License issues should block ship, not just appear in audits.",
            "problem": "Copyleft or unknown licenses slip in via deps.",
            "contents": """```text
patterns/license-policy-gate/
  license-policy-gate.md
primitives/license-policy-template.md
```""",
            "relationships": "- **Uses:** license-compliance persona\n- **Integrates:** ship-checklist, release-coordinator",
            "acceptance": """- [ ] Policy template (allowed/denied licenses)\n- [ ] Gate result: pass/fail with dep list\n- [ ] Human review flag for edge licenses""",
        },
    ],
    "decide": [
        {
            "title": "Add Spike coordinator pattern",
            "bootstrap": "decide-spike",
            "workflow_label": "workflow-decide",
            "summary": "Time-boxed exploration: options, evidence, recommendation — explicit no-merge default.",
            "why": "Prevents agents from implementing during exploration.",
            "problem": "Spikes turn into unreviewed production code.",
            "contents": """```text
patterns/spike-coordinator/
  spike-coordinator.md
  spike-worker.md
primitives/decision-record-schema/
  decision-record.md
```""",
            "relationships": "- **Consumes:** repo-archaeology, blast-radius optional\n- **Output:** decision record; optional promote to issues/CCM",
            "acceptance": """- [ ] Decision record schema\n- [ ] Explicit no-commit rules\n- [ ] Options matrix in output""",
        },
        {
            "title": "Add Build vs buy pattern",
            "bootstrap": "decide-build-vs-buy",
            "workflow_label": "workflow-decide",
            "summary": "Structured comparison of build in-house vs adopt library/service.",
            "why": "Common decision type deserves a reusable template.",
            "problem": "Ad-hoc comparisons omit security, ops cost, lock-in.",
            "contents": """```text
patterns/build-vs-buy/
  build-vs-buy.md
  comparison-matrix-template.md
```""",
            "relationships": "- **Specialization of:** spike-coordinator\n- **May use:** dependency-supply-chain persona for dep option",
            "acceptance": """- [ ] Matrix: cost, security, maintenance, lock-in, fit\n- [ ] Recommendation + non-goals""",
        },
        {
            "title": "Add Threat modeling lite pattern",
            "bootstrap": "decide-threat-model",
            "workflow_label": "workflow-decide",
            "summary": "STRIDE-lite pass per module/boundary → ranked threats → recommended mitigations or spikes.",
            "why": "Lightweight threat modeling without full formal TM process.",
            "problem": "Security audit finds bugs; threat modeling finds missing controls.",
            "contents": """```text
patterns/threat-modeling-lite/
  threat-modeling-lite.md
  threat-record-template.md
```""",
            "relationships": "- **Feeds:** audit issue generation, security personas\n- **Pairs with:** network-segmentation, auth-session personas",
            "acceptance": """- [ ] STRIDE categories per component\n- [ ] Threat ranked; mitigation or accept with justification\n- [ ] Read-only; issues filed in separate phase if configured""",
        },
    ],
    "operate": [
        {
            "title": "Add Deploy smoke coordinator pattern",
            "bootstrap": "operate-deploy-smoke",
            "workflow_label": "workflow-operate",
            "summary": "Post-deploy smoke checks coordinator: health endpoints, critical paths, rollback triggers.",
            "why": "Validates deploy success beyond CI.",
            "problem": "Deploys pass CI but fail in target environment.",
            "contents": """```text
patterns/deploy-smoke-coordinator/
  deploy-smoke-coordinator.md
  smoke-checklist.md
primitives/operate-safety.md
```""",
            "relationships": "- **Uses:** rollback-plan output\n- **Safety:** read-only unless explicit deploy approval",
            "acceptance": """- [ ] Smoke checklist template\n- [ ] operate-safety primitive (no prod without approval)\n- [ ] Compact smoke result schema""",
        },
        {
            "title": "Add SLO/error budget review pattern",
            "bootstrap": "operate-slo",
            "workflow_label": "workflow-operate",
            "summary": "Review SLOs, error budgets, alert noise from metrics/logs if available.",
            "why": "Operational health distinct from code audit.",
            "problem": "Teams lack periodic SLO/error budget discipline.",
            "contents": """```text
patterns/slo-error-budget-review/
  slo-error-budget-review.md
  slo-review-template.md
```""",
            "relationships": "- **Uses:** observability-readiness persona findings\n- **Read-only** on metrics sources",
            "acceptance": """- [ ] Template when metrics available vs unavailable\n- [ ] Action items as suggestions, not auto-changes""",
        },
        {
            "title": "Add Cost review pattern",
            "bootstrap": "operate-cost",
            "workflow_label": "workflow-operate",
            "summary": "Review cloud cost drivers, overprovisioned resources, idle assets (read-only).",
            "why": "Cost is an operational risk vector.",
            "problem": "Infra costs drift up unnoticed.",
            "contents": """```text
patterns/cost-review/
  cost-review.md
  cost-review-template.md
```""",
            "relationships": "- **Optional:** compose/cloud manifest review\n- **No:** automatic resource deletion",
            "acceptance": """- [ ] Cost finding schema\n- [ ] Evidence from billing export or manifest review only\n- [ ] Recommendations ranked by savings/risk""",
        },
    ],
    "communicate": [
        {
            "title": "Add Executive brief pattern",
            "bootstrap": "communicate-executive",
            "workflow_label": "workflow-communicate",
            "summary": "One-screen executive brief from audit, CCM, or incident compact results.",
            "why": "Leads need synthesis, not detailed reports.",
            "problem": "Detailed audit reports don't translate to stakeholder updates.",
            "contents": """```text
patterns/executive-brief/
  executive-brief.md
  executive-brief-template.md
```""",
            "relationships": "- **Consumes:** audit executive report, final-report, investigation results\n- **Distinct from:** detailed audit report",
            "acceptance": """- [ ] One screen max template\n- [ ] Input: paths or pasted compact summaries\n- [ ] Remote bootstrap""",
        },
        {
            "title": "Add Umbrella issue composer pattern",
            "bootstrap": "communicate-umbrella",
            "workflow_label": "workflow-communicate",
            "summary": "Compose umbrella epics with child issues, acceptance criteria, and links — planning artifact generator.",
            "why": "Extends umbrella-issue adapter to proactive planning (not just completion).",
            "problem": "Large work lands as vague epics without decomposed children.",
            "contents": """```text
patterns/umbrella-issue-composer/
  umbrella-issue-composer.md
  child-issue-template.md
```""",
            "relationships": "- **Related:** umbrella-issue-completion adapter (execution)\n- **Uses:** work-item-decomposition",
            "acceptance": """- [ ] Composer outputs umbrella body + child issue stubs\n- [ ] Optional: `gh issue create` batch with labels\n- [ ] Each child has acceptance criteria""",
        },
        {
            "title": "Add Stakeholder status pattern",
            "bootstrap": "communicate-status",
            "workflow_label": "workflow-communicate",
            "summary": "Periodic status digest: shipped, in progress, blocked, next — from issues/PRs/releases.",
            "why": "Recurring communication workflow for maintainers.",
            "problem": "Status updates are manual and inconsistent.",
            "contents": """```text
patterns/stakeholder-status/
  stakeholder-status.md
  status-digest-template.md
```""",
            "relationships": "- **Input:** `gh` issues, PRs, merged since date\n- **Consumes:** CCM final-report optional",
            "acceptance": """- [ ] Template: shipped / in progress / blocked / next\n- [ ] Config: `since_date:`, `milestone:`\n- [ ] Remote bootstrap""",
        },
    ],
}


def gh_issue_create(title: str, body: str, labels: str) -> int:
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(body)
        path = f.name
    cmd = [
        "gh", "issue", "create",
        "--repo", REPO,
        "--title", title,
        "--body-file", path,
        "--label", labels,
    ]
    url = subprocess.check_output(cmd, text=True).strip()
    num = int(url.rsplit("/", 1)[-1])
    Path(path).unlink(missing_ok=True)
    return num


def main():
    epic_nums = {}
    results = {"epics": [], "subs": []}

    for epic in EPICS:
        num = gh_issue_create(epic["title"], epic["body"], epic["labels"])
        epic_nums[epic["key"]] = num
        results["epics"].append({"key": epic["key"], "num": num, "title": epic["title"]})
        print(f"Epic #{num}: {epic['title']}")

    for key, subs in SUBS.items():
        epic_num = epic_nums[key]
        epic_title = next(e["title"] for e in EPICS if e["key"] == key)
        for sub in subs:
            body = sub_body(
                epic_title=epic_title,
                epic_num=epic_num,
                summary=sub["summary"],
                why=sub["why"],
                problem=sub["problem"],
                contents=sub["contents"],
                relationships=sub["relationships"],
                acceptance=sub["acceptance"],
                bootstrap=sub["bootstrap"],
                workflow_label=sub["workflow_label"],
            )
            labels = f"enhancement,{sub['workflow_label']}"
            num = gh_issue_create(sub["title"], body, labels)
            results["subs"].append({"epic": key, "num": num, "title": sub["title"]})
            print(f"  Sub #{num}: {sub['title']}")

    out = Path(__file__).parent / "workflow-issues-created.json"
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nWrote {out}")
    print(f"Created {len(results['epics'])} epics and {len(results['subs'])} sub-issues.")


if __name__ == "__main__":
    main()
