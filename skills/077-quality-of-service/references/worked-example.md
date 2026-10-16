# A failed batch deadline and a reserved dispatch

This is a finite, synthetic non-preemptive scheduler fixture.
All numeric inputs, targets and results below are illustrative examples;
confirm with the user/stakeholder before adopting them.

## Filled class and resource contract

At time zero, interactive jobs I1 through I8 and batch job B1 are eligible.
Trusted server policy assigns front-service to interactive and batch-service
to batch; request-supplied labels are ignored. All jobs remain admissible.
The only shared bottleneck is one worker. There is no downstream pool, network
wait, retry, extra arrival, cancellation or scheduler overhead in this model.
Each interactive job occupies it for 100 ms; B1 occupies it for 400 ms.
Every required result is exactly done: followed by its job identity.
Observe from time zero through 1400 ms with an initially empty completed ledger.

Illustrative per-class requirements; confirm with the user/stakeholder:
interactive completed p95 must be at most 1400 ms, and this eligible B1 must
complete within 600 ms of admission. Use sorted rank ceil(0.95 * n) for p95.
Require correct completion of the whole offered cohort by observation end.
This batch deadline is a finite progress rule, not a universal per-minute minimum.

## Before: strict interactive preference

Dispatch I1 through I8, then B1. Interactive completions occur at 100, 200,
300, 400, 500, 600, 700 and 800 ms; B1 starts at 800 and completes at 1200 ms.
Thus interactive p95 is 800 ms, but B1 fails its proposed progress deadline.
At that deadline B1 has not started; at observation end it has completed.
This finite delay is not a claim that batch can never run or that all failed
progress observations diagnose starvation.

## After: reserve the first eligible dispatch for batch

Use the approved opportunity sequence batch, interactive, repeated cyclically.
When a preferred queue is empty, borrow only under this fixture's finite-job rule.
No running task is preempted. B1 dispatches first and completes at 400 ms.
Interactive jobs then complete at 500, 600, 700, 800, 900, 1000, 1100 and 1200 ms.

| Independent check | Before | After |
| --- | --- | --- |
| Interactive p95 | 800 ms: passes | 1200 ms: passes |
| B1 progress | 1200 ms: fails | 400 ms: passes |
| Actual correct result identities | I1-I8 and B1 | Same exact cohort |
| Rejected/failed/unfinished at end | None | None |
| Worker service used | 1200 ms | 1200 ms |

The reservation trades interactive latency for batch progress within the stated
paired obligations. It does not add worker capacity or establish an unlimited
mixed-load guarantee. Longer noninterruptible borrowers or different arrivals
require another eligibility/capacity check.

## Engineering interpretation

The supplied dispatch trace supports this finite policy comparison; a real
zero-completion window without dispatch/service evidence would support only a
failed completion minimum. Verify actual results and trusted assignment as well
as class counters. No live scheduler, entitlement or response intervention ran here.
