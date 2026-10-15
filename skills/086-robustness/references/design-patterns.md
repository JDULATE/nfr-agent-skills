# Bounded-response patterns

Ground every limit in the accepted response and legitimate-work contract.

## Admission before expansion

- Use when input structure, decoded size, or generated work can grow before validation.
- Trade-off: early limits can reject valid demanding cases; the user must confirm
  allowed boundaries rather than inheriting an arbitrary parser or device limit.
- Verify: exercise the actual boundary and inspect allocation/work before rejection;
  checking input length after expansion does not bound that expansion.

## Work and queue budgets

- Use when a rejected or stalled request can keep scheduling or consuming shared work.
- Trade-off: admission and cancellation may reduce accepted work; permitted response
  and cleanup must match the real task lifecycle and side-effect contract.
- Verify: inspect queued/running work and reservations across repeated requests,
  cancellation, timeout, and completion; correlate the response with work actually stopping.

## Partial-effect boundary

- Use when parsing, validation, and mutation occur in the same path.
- Trade-off: buffering validated work or reconciling partial effects adds lifecycle
  complexity. Do not assume rollback exists or can reverse external effects.
- Verify: fail after partial processing and inspect business state plus any external
  effect records; choose actual supported atomicity or reconciliation behavior explicitly.

## Unaffected-work isolation

- Use when adverse work shares pools, queues, or state with legitimate tasks.
- Trade-off: isolation/admission can reserve resources at the expense of throughput;
  rejecting everything would avoid stress while defeating the valid-work obligation.
- Verify: run a distinguishable valid control during exposure and after it ends;
  inspect its result and resource scope instead of relying on process health.

## Error and post-exposure cleanup

- Use when an error path retains handles, reservations, tasks, or mutated state.
- Trade-off: cleanup itself can fail or race with completion; choose ownership and
  reconciliation against actual lifecycle semantics rather than swallowing errors.
- Verify: trigger the error repeatedly, inspect retained work against baseline,
  and check the process resumes its declared envelope after exposure clears.
