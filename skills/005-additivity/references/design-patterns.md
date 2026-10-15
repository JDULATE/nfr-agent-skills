# Combination and attribution patterns

Use these as engineering choices under the repository's local additivity meaning.
Get the metric owner's aggregation rule before claiming that effects should add.

## Baseline-relative contribution ledger

- **Use when:** Isolated measurements include an unchanged base outcome. Store
  the baseline and each increment's difference rather than adding complete totals.
- **Trade-off:** Drift in the baseline invalidates a comparison unless it is modeled
  explicitly; keeping an old convenient baseline can create a false interaction.
- **How to verify:** Re-measure the base under matched conditions, reconstruct the
  combined expectation, and compare it with the independently observed combination.

## Overlap identity and allocation

- **Use when:** Different increments can affect the same member or unit of work.
  Use stable contribution identity and an owner-approved union or allocation rule.
- **Trade-off:** Deduplication can suppress legitimately distinct work if identity
  is too broad; attribution can become arbitrary when shared effects have no owner.
- **How to verify:** Construct overlapping sets and repeated deliveries. Compare
  the actual member ledger with the intended unique or allocated contributions.

## Interaction residual

- **Use when:** The combined outcome may differ from the aggregation of isolated
  contributions. Preserve expected, observed, and their signed difference.
- **Trade-off:** Measurement noise or a resource ceiling can resemble interaction;
  do not infer its cause solely from the difference's sign.
- **How to verify:** Hold inputs and measurement procedure steady, reverse the
  combination order, and vary the suspected shared limit in a controlled fixture.

## Requirement record

Capture the increments, baseline, metric and units, conditions, aggregation
operation, identity/overlap policy, supported orders, tolerance, and evidence owner.
As an illustrative example only, propose an absolute residual target of 0;
confirm with the user/stakeholder. Obtain a different bound where counting or
measurement is approximate; the illustration does not set a universal tolerance.

## Review checks and anti-patterns

- Reject a sum of percentage improvements without an explicit common quantity.
- Reject union size calculated from isolated counts when overlap is unexamined.
- Mark a comparison inconclusive if isolated and combined workloads differ.
- Preserve an unexpected interaction rather than renaming it an individual gain.
- Record whether repeated delivery means repeated effect or the same effect replayed.

## Noisy contribution measurements

- **Use when:** Run-to-run variation could conceal interaction in the combined result.
- **Trade-off:** More repeats cost time; unstable conditions still cannot be repaired
  by averaging unmatched runs. Ask the user for the repetition/stopping plan and
  uncertainty rule before observing whether a candidate passes.
- **How to verify:** Reuse a frozen input set and measurement duration within each
  block. Measure the baseline, each isolated increment, and the combination in
  that block; rotate or randomize run order under the recorded plan to expose drift.
  For a sum rule with increments A and B, calculate each block's expectation as
  baseline + (A result - baseline) + (B result - baseline), then retain its residual.
  Repeat matched blocks rather than pooling unrelated isolated and combined means.
  Keep raw measurements, order, environmental changes, residual range, and the
  owner-selected summary/uncertainty method. Compare the supported uncertainty
  range with the confirmed tolerance under the chosen decision rule; if it crosses
  that boundary, report inconclusive rather than selecting favorable repeats.
  If drift prevents matched comparison, stabilize conditions or redesign the
  experiment before making a preserved-contribution claim.
