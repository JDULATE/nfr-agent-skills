# Continuation patterns

Choose mechanisms only after declaring the fault and required continued result.

## Alternate path and shared-failure map

- Use when a component fault must leave a serving path available.
- Trade-off: another instance adds coordination and may still share storage,
  routing, credentials, or control services with the failed path.
- Verify: fail the modeled boundary, hold it failed, and route actual work through
  the alternate; inspect mandatory dependencies before calling it independent.

## Commit ownership during handoff

- Use when old and replacement workers might both complete accepted work.
- Trade-off: ownership checks or fencing can require an authoritative dependency;
  its failure behavior belongs in the model instead of being assumed reliable.
- Verify: overlap an old worker's delayed commit with replacement work and inspect
  the actual effect. Verify the old ownership cannot commit if the contract forbids it.

## Repeated-operation identity

- Use when handoff or retry can replay the same logical work.
- Trade-off: retaining identity requires a lifecycle and atomic effect decision;
  a retry flag or response cache alone may leave duplicate business effects.
- Verify: interrupt before and after commit, replay the operation identity, and
  inspect unique required results and conflicting payload behavior against the real contract.

## Accepted degraded result

- Use when the stakeholder permits narrower service during the modeled fault.
- Trade-off: a reduced result is valid only under that explicit contract; returning
  stale data or refusing writes may instead violate the required continued service.
- Verify: assert the actual accepted subset, freshness, state effects, and deadlines
  throughout exposure; retain failures for any result the contract still requires.

## Partition and return-to-normal boundaries

- Use when communication loss can leave ambiguous ownership or delayed work.
- Trade-off: proceeding, refusing work, and waiting can each affect continuation
  or state constraints; ask which obligations must hold rather than promising all outcomes.
- Verify: exercise the declared partition and reconnection trace, delayed messages,
  competing commits, and result reconciliation. Do not infer arbitrary partition
  coverage from a killed-process test or a successful final health probe.
