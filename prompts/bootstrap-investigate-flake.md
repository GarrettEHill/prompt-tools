# Remote investigate bootstrap — flake hunter

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
workflow_run: <url or id>  # optional
test_name: <name>  # optional
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/investigate-flake-manifest.md` and all bootstrap files listed.

## Run

Execute per listed pattern files. Classify flake vs env vs bug.

**Begin:** load manifest, refresh live state, then run coordinator.
