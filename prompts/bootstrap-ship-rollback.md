# Remote ship bootstrap — rollback plan

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace. Read-only.

## Config (from user prompt)

```yaml
repo: <owner/repo>
version: <semver>              # target release
previous_tag: v1.1.0             # optional; infer if omitted
base_ref: main                 # optional
output: chat-only | docs/release/<version>-rollback.md
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/ship-rollback-manifest.md` and all bootstrap files listed.

## Run

Generate rollback plan per `rollback-plan.md`. Fill `rollback-template.md`.

**Begin:** load manifest, refresh live state, inspect release diff and migrations.
