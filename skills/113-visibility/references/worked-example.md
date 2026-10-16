# Export status visibility example

This is an illustrative scoped-view fixture, not an authorization or freshness standard.
All times, counters, and proposed budgets are illustrative examples;
confirm with the user/stakeholder before using them as project criteria.

## Filled view contract

| Field | Fixture value |
| --- | --- |
| Audience / requested subject | customer-fern / export-elm in team-fern |
| Supplied access policy | customer-fern may read team-fern exports only |
| Workflow point | customer opens export-elm detail |
| View clock | 200 ms on fixture-clock |
| Source clock | same fixture-clock |
| Freshness budget | 50 ms, illustrative example; confirm with the user/stakeholder |
| Requested source | export-elm, team-fern, writing, 3 of 8 chunks committed, observed at 100 ms |
| Unrelated source | export-birch, team-moss, completed, 8 of 8 chunks, observed at 190 ms |
| Projection order | observation revision, increasing within each export |
| Missing policy | unknown, never another export's row |
| Carried state | projections persist; rendering does not update their observation time |

## Failing view before remediation

The query selects the newest projection globally.
It returns export-birch and displays completed without subject or source time.
The audience sees a newer but unrelated result.

The supplied policy and subject key already distinguish the rows.
No new permission decision is required to identify this fixture failure.

## Remediation

Filter by the verified team scope and requested export identity.
At view time 200 ms, export-elm's observation age is 100 ms.
That exceeds the illustrative 50 ms budget; confirm with the user/stakeholder
before adopting that budget.

The view returns:
```text
subject = export-elm
state = last observed writing
progress = 3 of 8 committed chunks
observed_at = 100 ms
freshness = stale
```

The rendering is new, but the source observation remains old.

## Fresh, missing, and estimate probes

For the fresh probe, replace export-elm's source with revision leaf:
writing, 5 of 8 chunks committed, observed_at 180 ms.
At the same view time 200 ms its age is 20 ms, within the illustrative budget.
Show that observed state and time; do not claim the display caused more work to finish.

For the missing probe, remove export-elm while keeping export-birch.
Return export-elm unknown, with no progress counter; do not show completed.

For the estimate probe, keep the 5-of-8 source and add predicted finish=soon.
Changing that prediction to later must not change the observed committed counter.
Label the prediction separately.

For the terminal probe, publish a newer bloom revision for export-elm: completed,
8 of 8 chunks, observed_at 195 ms. Then deliver the older leaf revision again.
At view time 200 ms, retain bloom's completed projection across reloads.
The declared order is fern before leaf before bloom; arrival order cannot revive leaf.

## Requirement example and limits

At the export-detail workflow point, customer-fern shall see only export-elm's
projection with source time and explicit stale/unknown handling under the supplied policy.

The fixture checks status exposure, not the real exporter, cross-clock accuracy,
notification delivery, or the reason any export stopped progressing.
