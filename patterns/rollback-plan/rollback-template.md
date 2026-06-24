# Rollback Plan Template

Generate before deploy. Read-only — no rollback execution.

## Release metadata

| Field | Value |
|-------|-------|
| Version | |
| Previous stable tag | |
| Candidate SHA | |
| Deploy target | |

## Pre-deploy snapshot

| Asset | Current state | Capture command / location |
|-------|---------------|----------------------------|
| Git tag/commit | | |
| Container images | | |
| Config / env | | |
| Database schema | | |

## Rollback triggers

When to execute rollback (define before deploy):

1.
2.

## Rollback steps (ordered)

| Step | Action | Owner | Est. time | Verification |
|------|--------|-------|-----------|--------------|
| 1 | Revert to previous tag/commit | | | |
| 2 | Roll back container images | | | |
| 3 | Restore config/secrets | | | |
| 4 | Run migration down / restore DB | | | |
| 5 | Smoke test previous version | | | |

## Migration rollback

| Migration | Up revision | Down command / procedure | Data loss risk |
|-----------|-------------|----------------------------|----------------|
| | | | |

## Config restore

| File / secret | Pre-release value source | Restore procedure |
|---------------|--------------------------|-------------------|
| | | |

## Verification after rollback

- [ ] Health checks green
- [ ] Critical user paths verified
- [ ] Metrics/alerts nominal

## Communication

| Audience | Message | Channel |
|----------|---------|---------|
| On-call | | |
| Stakeholders | | |

## Risks and limitations

- Irreversible migrations:
- External dependencies:
- Known partial rollback:
