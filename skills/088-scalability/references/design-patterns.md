# Growth-curve practices

Vary a named demand axis and record the resource policy at every tested point.

## Workload axis and data distribution

- Use when users, arrivals, data size or tenants may mean different growth questions.
- Trade-off: holding dimensions fixed isolates an axis, while declared skew or
  mixed growth can reveal bottlenecks absent from a uniform synthetic workload.
- Verify: record each axis, held conditions, data size/distribution and hot partitions;
  do not infer active request capacity from an increased count of idle accounts.

## Fixed and added-resource series

- Use when a candidate can change workers, partitions or device capacity.
- Trade-off: extra resources may improve a point while hiding fixed-resource limits
  and costs; resource admission and improved useful service are separate observations.
- Verify: label each series and resource amount, compare useful outcomes and retain
  shared-state/coordination constraints instead of counting replicas as linear capacity.

## Saturation and generator probe

- Use when completed throughput plateaus or backlog/rejections rise.
- Trade-off: a generator or downstream test dependency can limit the observation;
  a flat completion curve alone does not identify which component saturated.
- Verify: retain offered/admitted/completed work, source capability, backlog and
  service bounds, then inspect the actual limiting path before assigning a cause.

## Tested-range and cost boundary

- Use when passing points are proposed as evidence for future growth.
- Trade-off: finite trials can locate supported points and failures but cannot
  establish unlimited capacity or constant marginal resource cost.
- Verify: preserve every tested point, resource policy, failed bound and duration;
  report untested ranges and avoid a fitted-line guarantee beyond observed conditions.
