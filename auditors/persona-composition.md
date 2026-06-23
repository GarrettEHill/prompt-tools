# Persona Composition

How the audit coordinator assigns personas to each disposable auditor run.

## Rules

1. **One section per auditor run** — boundary comes from the audit plan, not the persona.
2. **1–3 personas per run** — prefer 1–2; use 3 only when tightly related.
3. **Personas must fit the boundary** — do not assign `ci-cd` to a `src/` module-only section.
4. **No persona duplication in one run** — each persona at most once per auditor.
5. **Conflicting personas → separate runs** — e.g. `architecture-boundaries` across whole repo vs `documentation-accuracy` per doc folder → split.

## Composition patterns

### Single persona (default)

Tightest runs. Use when domain is distinct.

```text
Auditor run 1: [dependency-supply-chain]
Auditor run 2: [ci-cd]
Auditor run 3: [static-analysis-ingest]
```

### Complementary pair

Personas that share evidence but different lenses.

```text
Auditor run 1: [dependency-supply-chain, secrets-hygiene]
  boundary: manifests, lockfiles, .github/workflows, env templates

Auditor run 2: [ci-cd, secrets-hygiene]
  boundary: .github/workflows only
```

### Section + persona map

Coordinator builds from scope discovery:

```yaml
audit_runs:
  - id: run-1
    boundary: "Cargo.toml, Cargo.lock, Cargo.*.toml"
    personas: [dependency-supply-chain]
  - id: run-2
    boundary: ".github/workflows/"
    personas: [ci-cd, secrets-hygiene]
  - id: run-3
    boundary: "repo-wide ingest"
    personas: [static-analysis-ingest]
  - id: run-4
    boundary: "README.md, docs/"
    personas: [documentation-accuracy]
  - id: run-5
    boundary: "src/, crates/"
    personas: [architecture-boundaries, test-quality]
```

## Selecting personas

By name (1–3 per run) or by **class** — see [`auditors/persona-classes.md`](../../auditors/persona-classes.md):

```yaml
audit_runs:
  - boundary: ".github/workflows/"
    personas: [ci-cd, secrets-hygiene]
  - boundary: "compose/"
    classes: [infrastructure]  # expand via classes/infrastructure.md
```

## Spawn prompt template

```text
## Disposable auditor run: <run-id>

Repository: <owner/repo>
Boundary: <paths or scope>

Base: patterns/disposable-auditor/disposable-auditor.md
Personas: auditors/<persona>/persona.md (1–3)
Output: compact-auditor-result; tag persona + class on each finding
```

## Split vs combine decision

| Combine when | Split when |
|--------------|------------|
| same files, different check types | boundaries differ significantly |
| shared evidence gathering | persona would scan entire repo alone |
| ≤3 personas, related risk theme | one persona dominates runtime/cost |
| one workflow folder (ci + secrets) | findings would exceed one screenful |

## Anti-patterns

- all personas in one run → bloated context, shallow checks
- one persona per file → too many runs, redundant setup
- persona without boundary → unfocused repo-wide scan
