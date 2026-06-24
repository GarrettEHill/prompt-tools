# License Policy Template

Configure before running license-policy-gate.

```yaml
policy:
  allowed:
    - MIT
    - Apache-2.0
    - BSD-2-Clause
    - BSD-3-Clause
    - ISC
  denied:
    - GPL-3.0
    - AGPL-3.0
    - SSPL-1.0
  review_required:
    - LGPL-2.1
    - LGPL-3.0
    - MPL-2.0
  unknown_action: block | review
exceptions: []
```

Human review required for `review_required` and unknown licenses.
