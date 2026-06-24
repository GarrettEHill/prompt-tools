# Deprecation Enforcer

Find deprecated API/symbol usages; queue removals; verify zero usages before deleting exports.

Specialization of migration-sweep.

## Steps

1. Scan for deprecation markers (@deprecated, feature flags, docs)
2. Queue usage removal units
3. Verify empty usage set
4. Remove export in final unit after validation

See [`deprecation-adapter-template.md`](deprecation-adapter-template.md).
