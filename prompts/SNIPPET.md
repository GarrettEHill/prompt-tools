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
