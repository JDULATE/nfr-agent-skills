# Assurance practices

Use these practices for a declared reliance decision, not a universal quality score.

## Claim, assumption, and evidence ledger

- Use when the reliance claim spans distinct failure concerns.
- Trade-off: explicit subclaims reveal gaps but require narrower conclusions than
  a single green dashboard. Do not make the ledger a substitute for its evidence.
- Verify: for each subclaim record operating scope, source revision, supporting
  artifact, contrary observation, and what assumption the artifact cannot test.

## Counterexample challenge

- Use when incidents or known paths contradict a proposed reliance condition.
- Trade-off: treating a counterexample as blocking may delay a decision; ignoring
  it can leave the precise mission condition unsupported. Criticality needs an owner.
- Verify: reproduce or inspect the contrary path, resolve its relevance to the
  claimed context, and retain unsupported status until evidence or scope changes.

## Shared-provenance check

- Use when many reports appear to support the same subclaim.
- Trade-off: reusing evidence is useful, but multiple presentations of one trace
  do not exercise independent contexts or remove its shared assumptions.
- Verify: trace reports to underlying experiment, revision, environment, and
  workload; distinguish repeated summaries from genuinely different observations.

## Mitigation-conflict review

- Use when improving a local failure metric changes another reliance condition.
- Trade-off: blocking writes may protect a state rule while preventing the intended
  mission result. No aggregate score decides which condition may be relaxed.
- Verify: inspect each required subclaim after the proposed mitigation and record
  an owner decision for any relaxation; preserve nonnegotiable conditions separately.

## Concrete repository outputs

Produce a claim ledger and evidence index, plus only the authorized implementation
or checks needed for actual gaps. A dependable label, extra report, or rearranged
citation does not repair a missing behavioral premise. Ask the user for context
and criticality instead of presenting the local claim structure as a standard.
