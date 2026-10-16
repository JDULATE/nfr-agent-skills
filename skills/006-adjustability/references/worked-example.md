# Worked example: saved cap versus applied cap

Suppose a fictional exporter already reads a batch cap and snapshots it at batch
start. Its worker arrangement stays unchanged. Read the loop and value-refresh
path to verify that this control really exists before proposing this adjustment.

Illustrative fixture values only: cap changes from 2 to 3 records for the next
batch, using input records A, B, C, D, E; confirm with the user/stakeholder.
These values are not a throughput recommendation or a universal valid range.

Propose: "Changing `{batch_cap}` to `{confirmed_records_per_batch}` shall affect
`{next_batch_start}`, retaining `{running_batch_rule}`, evidenced by
`{applied_value_and_emitted_membership}` under the unchanged worker arrangement."

| Fixture | Expected observation under the proposed semantics |
| --- | --- |
| Original cap applied | Emitted memberships `[A,B]`, `[C,D]`, `[E]` |
| New cap saved but reader not refreshed | Requested value changes; old emitted membership reveals non-application |
| New cap applied at the next batch boundary | Fresh replay emits `[A,B,C]`, `[D,E]` |
| Adjustment while a batch is already open | That batch keeps its recorded old cap; inspect later work separately |
| Former value restored | New work returns to the old membership after the same application boundary |

The numeric memberships above are illustrative consequences of the proposed caps;
confirm with the user/stakeholder. Keep fixture records unique so duplication or
omission does not masquerade as a batch-size effect.

An operator display showing only the saved request is insufficient. For this
sequential fixture, a loop-applied value readback paired with emitted membership
is enough; no revision system is required. If overlapping updates, repeated-value
history, or asynchronous consumers make change identity ambiguous, bind an applied
revision to the affected work rather than treating a requested revision as applied.
If an override wins or a process only loads the setting at
startup, report that application boundary rather than claiming immediate tuning.

Reject a known invalid cap using the inspected domain rule; do not invent which
values are invalid without checking it. Compare processing and memory observations
separately if a better operating outcome is requested. Different membership alone
proves application of this control, not improvement in performance.

Return requested/applied values, boundary cases, reversal, and unmeasured effects.
