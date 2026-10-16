# Operation-envelope decisions

Choose from the measured critical path and the accepted completion/space limits.
A local timer, empty queue or fast successful subset is insufficient evidence.

## Decision table

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Independent per-row lookups dominate elapsed completion | Fetch the required projection in bounded batches | Larger batches retain more state and can delay first output | Compare full artifact completion, lookup count, exact rows and scoped peak space |
| Independent dependency waits are serial on the critical path | Overlap them with a bounded in-flight limit | More concurrency can increase contention or peak memory | Trace joined completion and cancellation; exercise the limit under the same offered work |
| Full result materialization breaches the space envelope | Stream ordered pages to a private artifact, then publish | Paging may add round trips; early partial publication can break the result contract | Inspect peak buffered rows, complete output and abort cleanup before publication |
| Queue delay dominates while service repeats avoidable work | Remove redundant service work before raising concurrency | A narrower stage may move the bottleneck rather than remove it | Compare arrival-to-result latency, backlog, useful throughput and space together |

## Bounded export sketch

Pseudocode; page_rows comes from a confirmed space budget. The page read must
honor that bound; slicing an already materialized full result does not.

~~~text
artifact = create_private_artifact()
try:
    for page in read_ordered_pages(query, page_rows):
        records = fetch_required_fields(page.identities)
        append_validated_rows(artifact, records)
    verify_complete_artifact(artifact)
    publish(artifact)
except failure:
    discard_private_artifact(artifact)
    report_failed_result(failure)
~~~

Measure through publication. If an independent dependency is overlapped, its
completion and failed outcome still belong to the same operation boundary.
Ask the user for data order, cancellation and partial-result policy where unknown.

## Outcome and statistic contract

Retain offered, admitted, completed, rejected, failed and pending work separately.
Predeclare eligibility, timeout/censoring treatment and the rank calculation.
A completed-only percentile cannot settle whether missing required exports pass.
Recompute the pooled statistic from eligible raw observations; averaging
per-instance percentiles is a different calculation.
Use a source that continues the agreed offered workload during slowdown.
Inspect peak space under that workload, not just a quiet single invocation.
