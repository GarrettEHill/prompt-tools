# Remote audit bootstrap

**Fetched from GarrettEHill/prompt-tools `main`.** Execute on the current Cursor workspace (target repo). Do not copy these files into the target repo.

## Config (from user prompt — fill defaults if omitted)

```yaml
repo: <owner/repo>              # infer from gh/git remote if omitted
sonar: auto                     # auto | yes | no
create_issues: yes              # yes | no
reports: chat-only              # chat-only | docs/audits/<YYYY-MM-DD>/
extra_personas: []
skip_personas: []
```

## Remote base (always latest)

```text
PROMPT_TOOLS_BASE=https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/
```

Before each phase, re-fetch manifest and phase files from this base so instructions stay current.

## Step 1 — Load manifest

Fetch and read:

```text
{PROMPT_TOOLS_BASE}prompts/manifests/audit-manifest.md
```

Then fetch all **Bootstrap** paths listed there.

## Step 2 — Inspect target workspace

This workspace is the audit target. Infer stack, layout, CI, compose, docs. Customize `audit_runs` per `audit-domains.md` + repo inspection. Apply `extra_personas` / `skip_personas`.

## Step 3 — Execute phases 0→8

Coordinator behavior: `{PROMPT_TOOLS_BASE}patterns/divide-and-conquer-audit/divide-and-conquer-audit.md`

Before each phase, fetch that phase's files from the manifest.  
Phases 0–5: read-only. Phase 6: issues only if `create_issues: yes`.  
Phase 3: one run at a time; fetch only assigned `auditors/<persona>/persona.md` files per run.

## Step 4 — Deliverables

Per manifest: compact results → registry → executive + detailed reports → issues (optional) → remediation queue → CCM handoff.

Remediation: user pastes snippet pointing at `{PROMPT_TOOLS_BASE}prompts/bootstrap-remediate.md`

## Safety

Read-only until issue creation. No secret values in output. Dedup Sonar/existing issues. No destructive git.

**Begin:** fetch manifest, run Phase 0 on this workspace.
