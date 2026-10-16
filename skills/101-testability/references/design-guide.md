# Test seam decisions

Select seams for controllability and discriminating observations in tests.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A test sleeps and still misses the deadline branch. | Inject the time source at construction. The harness must supply realistic event ordering. | Supply before, equal, and after deadline values and inspect the actual decision. |
| A real dependency cannot reliably return the needed error. | Script its response adapter while retaining the caller's decision logic. Integration coverage remains separate. | Supply success and failure through the same caller and compare their effects. |
| The branch executes but tests see only a generic success response. | Return a stable semantic result or inspect an existing effect boundary. Additional API surface needs a defined consumer. | Check contrasting outcomes and show that a deliberately wrong result fails. |
| Tests assert every private call in order. | Observe the contract result and required side effects instead. Some internal traces will no longer be acceptance assertions. | Refactor incidental helpers without changing the contract and keep tests passing. |
| A test clock override arrives through a public query parameter. | Move the override into test-only construction. This removes runtime convenience. | Verify normal requests cannot set the clock and normal construction uses the real source. |

## Construction seam sketch

```text
build_handler(clock, transport, outcome_store):
  return handler_using_real_deadline_and_response_rules(
    clock, transport, outcome_store)

normal_handler = build_handler(real_clock, real_transport, real_store)
test_handler = build_handler(scripted_clock, scripted_transport, fixture_store)
```

Keep the deadline predicate and response interpretation in the handler.
Do not return a precomputed expected answer from the test constructor.

## Observation choices

Prefer a contract-level result and the effect that matters to the feature.
Use a read-only inspection seam when an existing effect has no suitable test view.
Avoid exposing unrelated private state just because it is available.

If a test can arrange a condition but cannot distinguish its wrong outcome,
control alone has not solved the testability problem.
If the seam changes production behavior, separate and verify that behavior change
rather than describing it as a harmless test convenience.
