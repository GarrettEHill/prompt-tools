# Validation Ladder — Stack Examples

## Rust

1. `cargo test -p <crate> <test_name>`
2. `cargo test -p <crate>`
3. `cargo fmt --check`; `cargo test --workspace --locked`; `cargo clippy --workspace --all-targets --all-features -- -D warnings`
4. GitHub required checks; Sonar quality gate

## Node / TypeScript

1. `npm test -- <path-or-pattern>`
2. `npm test --workspaces --if-present` (affected package)
3. `npm run lint`; `npm test`; `npm run build`
4. GitHub required checks

## Python

1. `pytest path/to/test_file.py::test_name`
2. `pytest path/to/module`
3. `ruff check .`; `pytest`; `mypy` (if used)
4. GitHub required checks

## Go

1. `go test ./path/... -run TestName`
2. `go test ./path/...`
3. `go test ./...`; `golangci-lint run`
4. GitHub required checks

## GitHub-checks-only repo

1. Inspect failing annotation or log excerpt
2. Re-run affected workflow/job if possible
3. Run any documented local equivalent
4. Wait for required GitHub checks on the PR branch
