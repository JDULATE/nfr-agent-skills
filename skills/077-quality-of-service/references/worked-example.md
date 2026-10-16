# Interactive latency with starved batch work

The fictional scheduler shares a constrained worker pool between trusted
interactive and batch classes. The batch queue remains eligible during the trial.

## Illustrative class contract and trace

Illustrative targets and observations; confirm with the user/stakeholder:
Require interactive p95 at most 300 ms and at least 1 correct batch job per minute.

| Class | Observed result under contention | Proposed obligation |
| --- | --- | --- |
| Interactive | p95 200 ms | Timing passes in this fixture |
| Batch | 0 jobs completed in an eligible minute | Positive progress fails |

The joint class contract fails even though interactive timing looks favorable.
The fixture supplies no general feasibility claim for these example targets.

## Carried classification and resource state

A caller's urgent label is not authoritative. Retain the actual trusted assignment,
class queue eligibility, worker cap, offered mix and downstream waits.
A candidate may revise scheduling or admission to preserve both obligations under
the confirmed envelope; no mechanism is assumed to satisfy them without a trial.

If separate ingress queues recombine at an unconstrained downstream pool, inspect
that pool before declaring differentiation. If no eligible batch work was offered,
the minimum-progress case remains unverified rather than automatically passing.

## Verification boundary

Check per-class rejects and unfinished work alongside completions. Preserve
legitimate classification and the lower-class obligation; do not rename dropped
batch work into an exclusion after seeing the failed trace.
No scheduler run, priority entitlement or measured service guarantee exists here.
