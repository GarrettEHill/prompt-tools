# Reusable Cursor snippets

Copy one block into Agent on **any repo**. Nothing from prompt-tools needs to live in that repo. Each run fetches **latest `main`** from GitHub.

---

## Audit

```text
Run a divide-and-conquer repo audit (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-audit.md

Target: this workspace
repo: <owner/repo>
sonar: yes
create_issues: yes
reports: chat-only
```

---

## Remediate (after audit)

```text
Remediate audit findings (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-remediate.md

Target: this workspace
repo: <owner/repo>
```

---

## One-liner audit

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-audit.md — execute on this workspace; repo=<owner/repo>; create_issues=yes
```

Change only `repo` and flags between runs. Personas, phases, and schemas load from prompt-tools at runtime.

---

## Complete issue epic

```text
Complete issue epic (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-complete-epic.md

Target: this workspace
repo: <owner/repo>
epic: <issue-number>
```

Coordinator + one disposable worker per child issue. Runs until the epic is fully closed or blocked.

---

## Map — repo archaeology

```text
Map this repo (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-map-archaeology.md

Target: this workspace
repo: <owner/repo>
```

## Map — onboarding brief

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-map-onboarding.md
Target: this workspace
repo: <owner/repo>
```

## Map — blast radius

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-map-blast-radius.md
Target: this workspace
repo: <owner/repo>
target: <path or symbol>
```

---

## Review PR

```text
Review PR (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-review-pr.md

Target: this workspace
repo: <owner/repo>
pr: <number>
```

---

## Ship — release coordinator

```text
Ship release (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-ship-release.md

Target: this workspace
repo: <owner/repo>
version: <semver>
```

## Ship — gate checklist only

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-ship-checklist.md
Target: this workspace
repo: <owner/repo>
version: <semver>
```

## Ship — rollback plan

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-ship-rollback.md
Target: this workspace
repo: <owner/repo>
version: <semver>
previous_tag: <tag>
```

---

## Investigate — regression hunt

```text
Investigate regression (latest prompt-tools).

Fetch and fully execute:
https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-investigate-regression.md

Target: this workspace
repo: <owner/repo>
symptom: <description>
```

## Investigate — incident coordinator

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-investigate-incident.md
Target: this workspace
repo: <owner/repo>
incident: <title>
```

## Investigate — flake hunter

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-investigate-flake.md
Target: this workspace
repo: <owner/repo>
workflow_run: <url or id>
```

## Investigate — postmortem

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-investigate-postmortem.md
Target: this workspace
repo: <owner/repo>
input: <investigation result path>
```

---

## Communicate — executive brief

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-communicate-executive.md
Target: this workspace
repo: <owner/repo>
input: <audit or CCM summary paths>
```

## Communicate — umbrella issue composer

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-communicate-umbrella.md
Target: this workspace
repo: <owner/repo>
goal: <epic description>
```

## Communicate — stakeholder status

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-communicate-status.md
Target: this workspace
repo: <owner/repo>
since_date: <YYYY-MM-DD>
```

---

## Transform — migration sweep

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-transform-migration.md
Target: this workspace
repo: <owner/repo>
framework: <name>
from_version: <ver>
to_version: <ver>
```

## Transform — deprecation enforcer

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-transform-deprecation.md
Target: this workspace
repo: <owner/repo>
symbol: <deprecated API>
```

## Transform — codemod coordinator

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-transform-codemod.md
Target: this workspace
repo: <owner/repo>
codemod: <tool or script>
scope: <path>
```

## Transform — config drift fix

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-transform-config-drift.md
Target: this workspace
repo: <owner/repo>
```

---

## Generate — doc sync

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-generate-doc-sync.md
Target: this workspace
repo: <owner/repo>
```

## Generate — runbook

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-generate-runbook.md
Target: this workspace
repo: <owner/repo>
```

## Generate — changelog

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-generate-changelog.md
Target: this workspace
repo: <owner/repo>
since_tag: vX.Y.Z
```

## Generate — OpenAPI drift fix

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-generate-openapi.md
Target: this workspace
repo: <owner/repo>
```

---

## Govern — OSS hygiene

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-govern-oss.md
Target: this workspace
repo: <owner/repo>
```

## Govern — label policy

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-govern-labels.md
Target: this workspace
repo: <owner/repo>
mode: audit
```

## Govern — secret rotation sweep

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-govern-secret-rotation.md
Target: this workspace
repo: <owner/repo>
```

## Govern — license policy gate

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-govern-license-gate.md
Target: this workspace
repo: <owner/repo>
```

---

## Decide — spike

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-decide-spike.md
Target: this workspace
repo: <owner/repo>
question: <exploration question>
```

## Decide — build vs buy

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-decide-build-vs-buy.md
Target: this workspace
repo: <owner/repo>
capability: <description>
```

## Decide — threat modeling lite

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-decide-threat-model.md
Target: this workspace
repo: <owner/repo>
scope: <module or boundary>
```

---

## Operate — deploy smoke

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-operate-deploy-smoke.md
Target: this workspace
repo: <owner/repo>
environment: staging
base_url: <url>
```

## Operate — SLO review

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-operate-slo.md
Target: this workspace
repo: <owner/repo>
```

## Operate — cost review

```text
Fetch https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-operate-cost.md
Target: this workspace
repo: <owner/repo>
```
