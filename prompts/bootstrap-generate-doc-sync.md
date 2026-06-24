# Remote generate bootstrap — doc sync

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
paths: [docs/]  # optional
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/generate-doc-sync-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. 

**Begin:** load manifest, refresh live state, then run coordinator.
