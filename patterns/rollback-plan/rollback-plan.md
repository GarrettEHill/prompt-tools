# Rollback Plan Generator

Read-only. Produce a rollback plan **before** deploy — no rollback execution.

## Inputs

- Target version and previous stable tag
- Release diff (`git log`, `git diff` tag..HEAD)
- Deploy manifests (compose, k8s, Terraform) if present
- Migration files (sql, alembic, diesel, etc.)
- Config/env changes in release diff

## Steps

1. **Identify deploy surfaces** — images, configs, infra, migrations.
2. **Capture pre-deploy snapshot** — tag, image digests, config hashes.
3. **Map migration reversibility** — up/down scripts or manual restore notes.
4. **Draft ordered rollback steps** — revert code, images, config, DB.
5. **Define verification** — smoke tests after rollback.
6. **Note irreversible changes** — flag data-loss or partial rollback limits.

## Sources to inspect

- `CHANGELOG.md`, release PR body
- `compose/`, `deploy/`, `.github/workflows/`
- `migrations/`, `db/`, `schema/`
- `config/`, `env/*.example`

## Output

Fill [`rollback-template.md`](rollback-template.md).

## Safety

- Read-only — do not run deploy, rollback, or destructive commands.
- Pairs with [`deploy-smoke`](../operate/) (operate family) when available.
- Used by [`release-coordinator`](../release-coordinator/) as release bundle artifact.
