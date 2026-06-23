# Classification Outcomes

| Outcome | Next step |
|---------|-----------|
| ready for implementation | hand off to [`disposable-worker`](../disposable-worker/) |
| false positive | hand off to [`false-positive-adjudication`](../../primitives/false-positive-adjudication/) |
| blocked | return blocker to coordinator |
| too broad | hand off to [`work-item-decomposition`](../work-item-decomposition/) |
