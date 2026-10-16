# Batched lookup and bounded-page export

Use this synthetic fixture to inspect completed exports, not queue receipts.
Every numeric value, observation and target below is illustrative;
confirm with the user/stakeholder before adopting any requirement.

## Filled operation record

Worker profile export-slate runs one operation at a time on snapshot rev-amber.
Offer E001 through E100 at 600 ms intervals from time zero; observe for 60 seconds.
The source follows that schedule independently of responses. There are no retries,
background jobs or network errors in the direct/candidate runs.
E001 through E090 have 64 rows; E091 through E100 have 640 rows.
Required contents are ordered row identities from 1 through that export's row count.
The artifact is private until all rows are validated and published.
Queue acceptance takes 20 ms in both plans and is not the required completion.

Illustrative acceptance; confirm with the user/stakeholder:
require every offered export completed by run end, completed p95 at most 300 ms,
and peak worker memory at most 16 MiB. Define p95 as sorted rank ceil(0.95 * n).
Correct output count over the fixed observation window is the useful throughput.

## Before and remediation

The fixture's stage ledger assigns the following elapsed durations:

| Cohort / plan | Queue ms | Lookup ms | Serialize/publish ms | Completion ms |
| --- | ---: | ---: | ---: | ---: |
| Small / per-row lookup | 20 | 40 | 40 | 100 |
| Large / per-row lookup | 20 | 440 | 40 | 500 |
| Small / bounded batched lookup | 20 | 20 | 60 | 100 |
| Large / bounded batched lookup | 20 | 40 | 60 | 120 |

The candidate fetches each page's required fields together and streams that page
to a private artifact; final publication still requires every ordered row.
Base memory is 4.8 MiB; each buffered row occupies 0.1 MiB in this model.
Direct materialization therefore peaks at 11.2 or 68.8 MiB.
Candidate pages hold at most 32 rows, so peak modeled memory is 8 MiB.
No content is dropped; the larger serialization time is included above.

| Result | Before | After |
| --- | --- | --- |
| Completion set | All 100 correct | All 100 correct |
| Completed p95 | 500 ms: rank 95 is in the large cohort | 120 ms: rank 95 is in the large cohort |
| Useful throughput | 100 exports / 60 seconds | 100 exports / 60 seconds |
| Peak space | 68.8 MiB: fails proposed bound | 8 MiB: passes proposed bound |
| Pending/rejected/failed at run end | None | None |

This remedy changes the latency and space verdict, not the fixed-window completion
count. The supplied lookup ledger supports the modeled intervention; a real
critical-path investigation must establish those stage costs before choosing it.

## Mixed-outcome failing case

Keep the same arrivals, contents, profile and window. Complete E001 through E090
at 100 ms each, time out E091 through E098 at 500 ms without a completion record,
and reject E099 through E100 at admission. Disable retries for this case.
At run end: 90 correct, 8 timeout outcomes with completion unknown, 2 rejected.
Its completed p95 is 100 ms, but the explicit all-offered-complete rule fails.
Do not invent true completion times for the timed-out exports.

## Statistic counterexample

Illustrative sample calculation; confirm with the user/stakeholder:
an instance with 1 completed sample of 500 ms has p95 500 ms; another with 99
samples of 100 ms has p95 100 ms. Averaging those summaries gives 300 ms,
whereas the pooled rank rule gives 100 ms. Use the agreed eligible sample,
not an average of instance percentiles. No actual export or memory trial ran here.
