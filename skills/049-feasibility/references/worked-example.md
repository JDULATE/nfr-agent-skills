# Delivering a renderer in an offline environment

This synthetic constraint set, work estimates, and acceptance defaults are
illustrative; confirm with the user/stakeholder before adopting them.

## Filled delivery record

| Input | Value |
| --- | --- |
| Deliverable | render the supplied invoice template into local text output |
| Template and data | "invoice:{id}:{total_minor}", id=cedar, total_minor=1000 |
| Required output | invoice:cedar:1000 |
| Target environment | fixture runner with external networking disabled |
| Permitted dependencies | supplied local text renderer; external calls forbidden |
| Candidate remote | send template/data to remote rendering stub |
| Candidate local | use the supplied local renderer then write the output |
| Initial output state | absent |
| Available delivery capacity | 3 fixture work slots in window amber |
| Dependency availability | supplied local renderer is available during window amber |
| Local remaining tasks | bind renderer=1, connect writer=1, acceptance check=1 |
| Prerequisite owner | renderer maintainer role supplies the local renderer in the fixture |
| Delivery owner | application maintainer role |

All amounts and work slots are illustrative;
confirm with the user/stakeholder. Slots are not a calendar-duration estimate.

## Before: unsupported delivery path

The remote candidate invokes the external rendering stub.
The environment returns ExternalNetworkForbidden and output remains absent.
A favorable cost estimate would not repair this hard-constraint failure.

## Blocking probe and remediation

Run the supplied local renderer under the same network restriction.
Input is the filled template/data, not a simplified placeholder.
Probe output is invoice:cedar:1000 with no external invocation.
The local candidate therefore has capability evidence for this named case.

The probe alone does not finish delivery.
Its work ledger still includes binding, writer connection, and acceptance check.

## After candidate evidence

Complete those declared fixture tasks and reset output to absent.
The composed local path runs with external networking disabled:

```text
render result = invoice:cedar:1000
written output = invoice:cedar:1000
external call trace = []
task ledger = [bind done, writer done, acceptance done]
work model = 1 + 1 + 1 = 3 slots
capacity comparison = fits the illustrative 3-slot assumption
```

The candidate is supported under the filled assumptions.
No real delivery date or staff productivity is inferred.

## Failing alternate and missing-prerequisite controls

A placeholder renderer returns invoice:cedar without the total.
It meets the offline constraint but fails the unchanged deliverable.

If the local renderer is not actually supplied, mark that prerequisite unresolved.
The earlier fixture probe cannot establish its availability in a real project;
the decision remains conditional rather than assuming a replacement dependency.

If the local renderer is available only in later window birch while delivery
capacity and the required handoff remain in amber, the candidate is blocked
for amber. Independent availability does not establish a usable common window.

## Limits

Only the supplied template, local environment model, and work assumptions are
covered. Additional templates, packaging, real capacity, and production readiness
need project evidence before a delivery commitment.
