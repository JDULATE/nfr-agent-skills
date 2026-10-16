# Deadline test seam example

Treat all times, identifiers, and proposed outcomes as illustrative fixture values;
confirm with the user/stakeholder before using them as a project's contract.

## Filled behavior record

| Field | Fixture value |
| --- | --- |
| Entry / subject | attempt handler / attempt-fern |
| Initial store | attempt-fern pending; empty completion outbox |
| Time unit | milliseconds on one synthetic clock |
| Deadline | 120 |
| Deadline meaning | now at or after deadline returns timed_out before calling transport |
| Pre-deadline success | transport returns ok; store completed; emit completed(attempt-fern) |
| Pre-deadline failure | transport returns unavailable; store retry_pending; no completion event |
| Timeout result | store timed_out; no completion event |
| Carried state | the resulting store and outbox within a case; reset before the next case |
| Original construction | clock returns 100; transport returns ok; no injectable dependencies |
| Proposed construction | injected clock and response adapter; same decision rules |
| Observation | returned status, stored status, completion outbox |
| External request fields | attempt id only; no clock or test-mode field |

## Failing harness before remediation

The only available harness invokes the original construction.
It always sees completed, stored completed, and completed(attempt-fern).
Asking that harness to test the timeout branch cannot change its clock or
transport. A passing "no exception" assertion does not show timeout behavior.

This establishes a missing test capability in the fixture, not a production
deadline defect.

## Remediation

Pass the clock, transport, and store through construction while keeping:
```text
if clock.now() >= deadline:
  store.status = timed_out
else if transport.execute() == ok:
  store.status = completed
  outbox.append(completed(attempt_id))
else:
  store.status = retry_pending
return store.status
```

Use a fresh pending attempt-fern and empty outbox for every case.
| Case | Clock | Scripted response | Return / store | Outbox | Transport calls |
| --- | ---: | --- | --- | --- | ---: |
| before | 119 | ok | completed / completed | completed(attempt-fern) | 1 |
| endpoint | 120 | ok, not consumed | timed_out / timed_out | empty | 0 |
| after | 121 | ok, not consumed | timed_out / timed_out | empty | 0 |
| failure | 119 | unavailable | retry_pending / retry_pending | empty | 1 |

The after cases now force the previously inaccessible branch and distinguish
its effect from successful completion.

## Deliberately failing control

Change the predicate to strictly greater than the deadline.
At clock 120 the altered handler returns completed and emits a completion event.
The endpoint assertion must fail on status and outbox; a harness checking only
"handler returned" would miss this defect.

## Normal-path check

Construct with the original clock response 100 and original transport response ok.
The normal-path fixture still completes and emits completed(attempt-fern).
A request containing only attempt id cannot select a clock; reject or ignore
unsupported test fields according to the existing public-input contract.

## Requirement example and limits

The test harness shall force the deadline and response cases through the real
handler and distinguish their semantic statuses and completion effects without
sleeping. These constructed cases do not validate a live transport, actual wall
clock behavior, production persistence, or every possible response class.
