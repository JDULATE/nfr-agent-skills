# Variation practices

Choose the conditional variation question and keep absolute service constraints separate.

## Conditional observation groups

- Use when input size, warm state, demand or environment differ between samples.
- Trade-off: grouping makes causes clearer but very narrow groups can conceal
  the broader conditions the stakeholder actually needs covered.
- Verify: retain group membership, eligibility and raw outcomes; declare which
  differences are intentional conditions rather than deleting unfavorable samples.

## Extremes and censored work

- Use when rare pauses or unfinished tasks matter to the variation promise.
- Trade-off: finite extrema depend on observed coverage; missing or timed-out
  outcomes can leave the whole set's range unestablished.
- Verify: retain actual extremes, timeout cutoffs, pending/missing samples and
  window scope. Never substitute an unknown completion with a conveniently short value.

## Exceptional work path

- Use when uncommon cache misses, dependencies, retries or cleanup cause surprise.
- Trade-off: optimizing the usual path can improve central timing without changing
  the exceptional branch; bounding that branch can trade resource or absolute delay.
- Verify: correlate raw slow cases with actual execution paths and compare the
  same condition groups after the change, including preserved result correctness.

## Variation versus absolute deadline

- Use when a candidate produces a narrower but slower distribution.
- Trade-off: a controlled spread may aid predictability while violating another
  task's required deadline; neither metric automatically compensates for the other.
- Verify: evaluate both confirmed rules independently with unchanged eligibility;
  report finite observations without inferring the absence of all future outliers.
