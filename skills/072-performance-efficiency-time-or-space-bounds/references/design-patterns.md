# Operation-envelope practices

Define the result, offered workload and measurement boundaries before optimizing.

## Required-result timing boundary

- Use when acceptance, queueing and business completion occur at different points.
- Trade-off: narrower timers can isolate a component but cannot establish an
  end-to-end deadline if they omit queued or downstream required work.
- Verify: trace start, admission, queue, service and actual result; label local
  timings separately and retain the complete requested journey boundary.

## Offered-load and unfinished-work ledger

- Use when slowdown can reduce arrivals or leave work pending at test end.
- Trade-off: a controlled arrival source and backlog observations add work, but
  completed-only measurements may hide rejected or never-finished demand.
- Verify: retain offered/admitted/completed/rejected/failed/pending counts, source
  capacity and timestamps. Do not report a timeout cutoff as observed true completion time.

## Statistic and sample method

- Use when a percentile or other summary is an acceptance metric.
- Trade-off: summaries help compare runs but hide individual outcomes and depend
  on eligibility/rank rules; per-instance summaries are not the pooled raw sample.
- Verify: declare the calculation, retain raw outcomes and recompute it over the
  agreed set. Report missing/censored work and whether it prevents a justified pass.

## Critical-path and data-work change

- Use when queries, repeated work, dependencies or serialization occupy measured time.
- Trade-off: moving work, reusing results or increasing concurrency can affect
  freshness, correctness, contention and resource consumption.
- Verify: compare required outputs and complete latency under declared input mix,
  warm state and workload; a shortened local stage alone is not whole-operation evidence.

## Space boundary under concurrency

- Use when data size, queued work or simultaneous requests can increase retained space.
- Trade-off: buffering may improve throughput while worsening peak space; process,
  container, device and whole-task scopes answer different questions.
- Verify: inspect peak retained space with the actual data/concurrency envelope,
  while recording timing and result constraints rather than testing a quiet tiny call only.
