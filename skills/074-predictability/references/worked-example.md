# Incremental cleanup narrows a task range

This is a deterministic synthetic work model, not measured latency.
All numeric inputs, observations and targets are illustrative examples;
confirm with the user/stakeholder before treating them as requirements.

## Filled conditions and rule

- Tasks T01 through T20 arrive at one-second intervals on serial profile task-slate.
  Each has identical payload amber and must return exactly accepted:amber.
- No cold initialization, cache misses, retries, network waits or other tasks
  occur. All tasks belong to one accepted condition group; none are excluded.
- Base task work takes 100 ms. Cleanup begins with exactly 140 expired entries,
  visits them in index order, costs 5 ms per entry and gains no new entries.
- Window: from the first arrival through the final result. Every task finishes;
  missing, rejected and timed-out counts are zero in these modeled runs.
- Proposed limits: observed max-minus-min at most 50 ms and every completion
  within 300 ms of its arrival. These limits are illustrative;
  confirm with the user/stakeholder.

## Before and after the change

Before: task T03 performs the full expired-entry sweep; all others do base work.
Its trace contains 800 ms for T03 and 100 ms for every other named task.
The cleanup cursor reaches the end at T03; no cleanup backlog remains afterward.

After: every task advances the shared cleanup cursor by at most 7 entries.
Each task takes 100 + 7 * 5 = 135 ms; cursor progression is 7, 14, ... , 140.
After T20 every expired entry is removed; no new work was silently deferred
beyond the observation window.

| Plan | Completion sequence definition | Range ms | Deadline verdict | Cleanup end state |
| --- | --- | ---: | --- | --- |
| Full sweep | T03 = 800; all others = 100 | 700 | T03 fails | All expired entries removed |
| Incremental | T01 through T20 = 135 each | 0 | All pass | Same entries removed by T20 |
| Pad full-sweep results | Every task waits until 900 ms before returning | 0 | All fail | Original sweep still finishes at T03 |

All numeric comparisons remain illustrative; confirm with the user/stakeholder.
The padding control preserves contents and performs the original cleanup, but
a narrow range cannot waive the independent absolute deadline.
The mean of both the full-sweep and incremental plans is 135 ms; an unchanged
mean therefore does not imply unchanged variation.

## Supported cause and limits

The supplied per-entry costs and cursor positions establish the modeled sweep
contribution. They do not prove that cleanup causes pauses in an unseen repository.
No condition-group field or pending case is left implicit in this fixture.
A real run with unfinished tasks cannot substitute these complete observations.
If new expiry work appears, measure its arrival and drain rates; this finite
cohort supplies no sustained cleanup-capacity or future no-outlier guarantee.
