# Prompts

## Reuse on any repo

Copy from **[`SNIPPET.md`](SNIPPET.md)** — short text you paste into Cursor. The agent fetches **latest `main`** from GitHub; the target repo needs no prompt-tools files.

## Remote entry points (canonical)

| Action | URL |
|--------|-----|
| Audit | `https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-audit.md` |
| Remediate | `https://raw.githubusercontent.com/GarrettEHill/prompt-tools/main/prompts/bootstrap-remediate.md` |

Bootstraps load [`manifests/`](manifests/) → `patterns/`, `auditors/`, `primitives/` on demand.

## Local development

When editing prompt-tools, test by pasting the SNIPPET with `repo` set to a target project. Push to `main` to update what all snippets fetch.
