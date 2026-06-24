# Migration Worker

One migration unit per worker.

1. Apply scoped migration change
2. Run validation ladder for unit scope
3. Open PR or return compact result
4. Roll back unit on validation failure
