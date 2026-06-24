# Remote epic completion bootstrap

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace. Works on any repo with GitHub issues — no prompt-tools files needed in the target repo.

## Config (from user prompt)

```yaml
repo: <owner/repo>              # infer from gh/git remote if omitted
epic: <issue-number>            # parent/umbrella epic issue — required
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/epic-completion-manifest.md` and all bootstrap files listed.

## Run

CCM coordinator per `continuous-completion-model.md` with the `umbrella-issue-completion` domain adapter.

1. **Refresh live state** — auth, git hygiene, baseline validation.
2. **Load epic** — `gh issue view <epic>`; read body, checklist, linked children, sub-issues, and task lists.
3. **Build queue** — open child issues + unchecked umbrella criteria. Decompose broad criteria into child issues before implementation (`work-item-decomposition.md`).
4. **Loop** — select exactly one concrete, unblocked item; spawn a fresh disposable worker; discard worker context after compact result.
5. **Progress** — after each child, comment on the parent with child id, PR link, and remaining work.
6. **Stop** — when all children and umbrella criteria are complete, all remaining work is blocked, or CCM stop rules trigger.

One work item per worker. Re-fetch manifest files each iteration if needed. Do not close the epic until every child and umbrella acceptance criterion is satisfied.

**Begin:** load manifest, refresh live state, load epic `<epic>`, build queue, spawn worker for first item.
