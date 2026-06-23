# Code Quality / Lint Sweep — Stack Examples

## Rust

- **Discover:** `cargo clippy --workspace --all-targets --all-features -- -D warnings`
- **Item:** one clippy lint + one crate/module
- **Validate:** `cargo clippy -p <crate>`; `cargo test -p <crate>`

## Node

- **Discover:** `npm run lint`
- **Item:** one eslint rule + one package/directory
- **Validate:** `npm run lint`; `npm test`

## Python

- **Discover:** `ruff check .`
- **Item:** one ruff rule + one package/path
- **Validate:** `ruff check path/`; `pytest path/`

## Shell / Actions

- **Discover:** `shellcheck scripts/*`; `actionlint`
- **Item:** one script or workflow file
- **Validate:** re-run shellcheck/actionlint on changed files

## Disputed findings

Route to [`primitives/false-positive-adjudication`](../../primitives/false-positive-adjudication/).
