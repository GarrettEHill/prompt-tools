# Remote ship bootstrap — release coordinator

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current workspace.

## Config (from user prompt)

```yaml
repo: <owner/repo>
version: <semver>              # e.g. 1.2.0 — required
base_ref: main                 # optional
previous_tag: v1.1.0             # optional; infer from git if omitted
required_gates: []               # optional override
```

## Remote base

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

## Load

Fetch `{PROMPT_TOOLS_BASE}prompts/manifests/ship-release-manifest.md` and all bootstrap files listed.

## Run

Release coordinator per `release-coordinator.md` with `semver-release` domain adapter.

**Begin:** load manifest, refresh live state, run ship gate, then process release slices or hand off to CCM.
