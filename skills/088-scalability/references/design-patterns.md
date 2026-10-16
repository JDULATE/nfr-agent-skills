# Growth-curve decisions

Choose an intervention only after separating workload growth from resource changes.
A plateau alone does not identify a store, partition, coordinator or generator.

## Decision table

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Added workers wait on the same global coordinator | Partition coordination by an independent business key | Cross-key ordering or transactions may forbid that split | Compare fixed and added-worker curves; inspect same-key ordering and cross-key concurrency |
| A declared hot key fills one partition while others are idle | Split only work whose semantics permit smaller independent keys | Additional keys can change ordering or introduce merge work | Replay the same skew, compare the hot partition and retain the unsplittable case |
| Useful per-worker capacity rises with fewer repeated shared reads | Coalesce reads or reuse a versioned projection before adding workers | Retained state adds freshness and invalidation costs | Compare the growth series with and without reuse plus actual version/result checks |
| Demand bursts fill an unbounded queue before workers can recover | Bound admission and expose backpressure under the accepted service policy | Rejection/backpressure does not itself satisfy a no-loss growth promise | Keep every admitted/rejected unit visible and test queue drain after the burst |

## Partitioned-owner sketch

Pseudocode for a contract with ordering within a key and independence across keys.
Ask the user if cross-key ordering is required; then this split may be invalid.

~~~text
submit(work, ownership_epoch):
    key = business_partition_key(work)
    owner = owner_for(key, ownership_epoch)
    enqueue_in_key_order(owner, work)

commit(work, ownership_epoch):
    require_current_owner(work.key, ownership_epoch)
    apply_required_effect_once_under_confirmed_identity_rule(work)
~~~

The owner check and effect need real supported concurrency semantics.
During movement, prevent stale owners from committing and reconcile in-flight work.
A hash or more partitions does not supply those semantics.

## Series and cause checks

At each point fill offered demand, useful completions, rejects, backlog change,
duration, data/skew and actual resource amounts. Label fixed-resource and
added-resource series separately, including resource costs.
Exercise the generator beyond the requested points before blaming service capacity.
Use a coordination intervention only when source/trace evidence identifies it;
retain alternative causes as unknown when observations do not distinguish them.
Report tested ranges rather than linear or unlimited extrapolation.
