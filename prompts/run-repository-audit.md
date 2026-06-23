# Run Repository Audit

Paste into Cursor on the **target repo**. Instructions live in prompt-tools — load them, don't duplicate.

## Config

```yaml
repo: <owner/repo>
prompt_tools: <local path | GarrettEHill/prompt-tools>   # local clone preferred for @-mentions
sonar: yes | no
create_issues: yes | no
reports: docs/audits/<YYYY-MM-DD>/ | chat-only
extra_personas: []      # optional, e.g. [network-segmentation-policy]
skip_personas: []       # optional
```

## Bootstrap

1. Set `PROMPT_TOOLS_BASE`:
   - local: `{prompt_tools}/`
   - remote: `https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/`
2. **Load and read** `prompts/manifests/audit-manifest.md` from prompt-tools.
3. Load all **Bootstrap** files listed in that manifest.
4. Inspect **this workspace** (layout, stacks, CI, compose, docs) to customize the audit plan.

## Run

Act as audit coordinator per `divide-and-conquer-audit.md`.  
Execute manifest phases **0→8** in order. Before each phase, load that phase's files from the manifest.

- Phases 0–5: **read-only** on target repo (no commits)
- Phase 6: create issues only if `create_issues: yes`
- Phase 3: one auditor run at a time; load only that run's persona files; keep compact results only
- Phase 8: output CCM handoff → `prompts/run-audit-remediation.md`

**Start now:** resolve `PROMPT_TOOLS_BASE`, load the audit manifest, run Phase 0.
