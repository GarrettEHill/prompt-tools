# Env / Compose / CI Drift Adapter

```yaml
sources:
  env_example: .env.example
  compose_files: [docker-compose.yml]
  ci_workflows: [.github/workflows/*.yml]
drift_rules:
  - name: missing_env_in_example
  - name: compose_service_env_mismatch
  - name: ci_runtime_not_in_matrix
```
