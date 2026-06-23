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
