# Variation decisions

Use the source-backed exceptional path, not a smooth mean, to choose a change.
Ask whether the user wants a spread rule or an absolute tail-latency deadline;
a percentile complaint can mean either and may need both.

## Decision table

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A periodic full cleanup sweep aligns with rare pauses | Replace the sweep with bounded incremental cleanup | Steady work can increase and expired state can persist until visited | Trace work per task, cleanup backlog, raw range and the independent deadline |
| Cold initialization is the only slow branch and readiness can wait | Complete that initialization before accepting the scoped task class | Startup takes longer and moves work; it does not erase startup obligations | Test cold startup separately and every accepted task's grouped completion range |
| Retry count varies within equivalent tasks | Bound total retry work under the accepted response/result policy | Some tasks may fail rather than finish after a long retry tail | Keep failed/pending tasks visible; test both the range claim and required result policy |
| Cache eviction triggers repeated full rebuilds | Rebuild in bounded chunks or prebuild before the affected task class | Memory and freshness constraints can rule out prebuilding | Exercise eviction/rebuild states and inspect worst task work, spread and content |

## Incremental-cleanup sketch

Pseudocode; state is shared with normal cleanup ownership, not a private counter
reset on every request. cleanup_quota is a confirmed work limit, not a time guarantee.

~~~text
handle(task, cleanup_state, cleanup_quota):
    result = produce_required_result(task)
    examined = take_next_entries(cleanup_state.cursor, cleanup_quota)
    for entry in examined:
        remove_if_expired(entry)
    cleanup_state.cursor = successor_of_last_examined(examined)
    return result
~~~

Compare the full observed task range before and after; include cleanup time.
If arrival of cleanup work outpaces that quota, then expose the growing backlog
rather than claiming the incremental design is complete.

## Conditional and finite evidence

Use predeclared groups for meaningful input, warm-state and load differences.
Do not split groups merely to exclude an inconvenient branch from its promise.
Retain extremes, timeout cutoffs, pending and missing work with the observation
window. A smaller completed-only range supplies no value for an unknown completion.
Verify the absolute deadline and required output independently. Finite traces
cannot establish that future outliers are impossible or that a control loop is stable.
