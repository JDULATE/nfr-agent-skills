# Failure-occurrence practices

Declare required behavior and operational exposure before interpreting failure evidence.

## Event and affected-operation ledger

- Use when retries, cascades, or incident summaries can distort occurrence counts.
- Trade-off: a single causal incident may affect many operations; counting every
  symptom as another event can also misrepresent the agreed failure unit.
- Verify: retain event identity, affected work, required-result violation, original
  and retry outcomes, and the explicit deduplication rule. Do not silently swap units.

## Continuous trial and reset boundary

- Use when the requirement concerns an uninterrupted operating interval.
- Trade-off: restarting can restore service and allow investigation, but the new
  state is a different trial boundary rather than evidence of prior continuity.
- Verify: record start/end and reset reason; include the failed interval and its
  observation coverage instead of reporting only the post-restart clean segment.

## Sustained state progression

- Use when repeated use changes queues, handles, caches, reservations, or lifecycle state.
- Trade-off: long trials consume resources and still exercise only their selected
  profile; short freshly initialized checks may never reach the implicated state.
- Verify: replay the source-backed progression, inspect invariants and required
  outcomes during it, and retain state at the first violation for reproduction.

## Profile and inference boundary

- Use when a clean test is proposed as evidence for broader operating reliability.
- Trade-off: a controlled profile is repeatable but can omit actual workload,
  environment, and dependency variation. Idle observation is not exercised work.
- Verify: compare the claimed context with actual exposure and coverage; state
  what was not tested. Do not infer a production probability without an agreed model.
