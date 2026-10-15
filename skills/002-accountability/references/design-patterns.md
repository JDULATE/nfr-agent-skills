# Attribution practices

Choose an identity model the actual source can support; do not invent human responsibility.

## Trusted actor binding

- Use when a request includes actor labels or identity arrives through another component.
- Trade-off: retaining claimed and validated identity separately adds fields;
  copying claims into the trusted actor position can falsely attribute the action.
- Verify: vary untrusted actor content while holding validated identity fixed and
  inspect the principal actually bound at the action/effect boundary.

## Delegation and executor chain

- Use when jobs or services act on behalf of another principal.
- Trade-off: propagated identity can become stale or lost; delegation lifetime and
  evidence access must follow the supplied authority/data policy.
- Verify: trace initiating principal, delegated authority, executor and operation
  identity across each handoff; leave missing origin unknown instead of inferring it.

## Attempt, decision and effect correlation

- Use when accepted requests can fail, retry or complete asynchronously.
- Trade-off: more precise outcome states require correlation and lifecycle handling;
  a request log alone cannot establish that its attributed actor caused the effect.
- Verify: compare attempts, authorization decisions, executor work and final state;
  preserve retries and ambiguous outcomes without replacing the original identity.

## Honest identity limits

- Use when shared credentials, service accounts or missing origin constrain attribution.
- Trade-off: an unknown/shared principal is less satisfying than a named person,
  but the evidence may support no stronger statement.
- Verify: inspect what the identity source actually asserts and exclude bearer
  secrets; document evidence lifetime/access and unsupported human-intent conclusions.
