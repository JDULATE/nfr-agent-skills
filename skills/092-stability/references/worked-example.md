# Queue-mode flapping under held demand

The fictional controller selects `economy` or `burst` mode. Offered demand is
held constant, but its sampled signal moves around the current transition boundary.
Required response to a genuinely sustained higher demand remains part of the contract.

## Input and carried control state

| Trace input | Current simple rule | Candidate transition-band rule |
| --- | --- | --- |
| Near-boundary below signal | economy | Retain initial economy while inside band |
| Near-boundary above signal | burst | Retain economy while still inside band |
| Near-boundary below again | economy, reversal retained | Retain economy; inspect actual action trace |
| Genuine sustained signal above enter boundary | burst | Enter burst within confirmed response limit |
| Sustained signal below exit boundary | economy | Exit burst under confirmed transition rule |

The candidate is a proposed explicit state rule, not a proven control guarantee.
Ask for enter/exit conditions, settling, permitted delay, and the actual measured
signal. Do not infer boundaries from the symbolic labels in this example.

## Requirement trial

Illustrative observation horizon; confirm with the user/stakeholder:
After the agreed settling rule, require no further reversals during a 10-minute
held-input trial, while separately meeting the confirmed genuine-change response.
This is not a universal no-reversal rule for every useful controller.

## Interpretation and rejection

Keep full input/signal/action traces. An average mode value can appear unchanged
while the current rule repeatedly flips, so it cannot substantiate this trial.
A candidate that always stays in economy also produces no reversals but fails
the sustained-higher-demand response. Missing samples create an observation gap,
not evidence of calm behavior. No actual control trial was run for this illustration.
