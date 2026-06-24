# Remote ship bootstrap — checklist

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace. Read-only gate evaluation.

## Config (from user prompt)

```yaml
repo: <owner/repo>
version: <semver>              # optional; for gate metadata
base_ref: main                 # optional
required_gates: []               # optional override
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/ship-checklist-manifest.md` and all bootstrap files listed.

## Run

Evaluate release gates per `ship-checklist.md`. Output `ship-gate-schema` verdict.

**Begin:** load manifest, refresh live state, evaluate gates.
