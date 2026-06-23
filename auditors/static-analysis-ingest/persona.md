# Persona: Static Analysis Ingest

**Domain:** `static-analysis`  
**Sonar mode:** ingest-existing — primary source of truth

## You inspect

- open GitHub issues from Sonar/SonarCloud
- PR/check annotations if visible
- gap: paths clearly not covered by Sonar config

## Read-only checks

```bash
gh issue list --state open --search "sonar OR sonarcloud OR code smell OR vulnerability OR hotspot"
```

Do not re-run full local static analysis unless Sonar/GitHub issues are unavailable.

## Finding patterns

- open Sonar finding without GitHub issue → `coverage gap`
- duplicate issues for same rule+file → note for dedup at aggregation
- Sonar config excludes critical paths → `medium`

## Severity

- use Sonar severity when ingesting
- downgrade only with evidence; never upgrade without evidence

## Dedup

- reference existing issue `#N` — do not re-file
- output `already_tracked` vs `new_gaps` counts

## Do not

- duplicate Sonar's job with a full local lint sweep
- create findings already tracked on GitHub
