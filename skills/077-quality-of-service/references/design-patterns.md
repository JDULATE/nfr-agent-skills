# Class-treatment practices

Choose treatment for trusted classes under a declared contention/capacity envelope.

## Trusted class assignment

- Use when request labels or tenant metadata select a privileged service class.
- Trade-off: classification needs maintained entitlement rules and a trusted source;
  a scheduling label must not become a new permission to access an asset.
- Verify: exercise legitimate assignment and forged/cross-scope labels, inspecting
  the actual resulting queue/treatment rather than the submitted field alone.

## Admission and scheduling obligations

- Use when different classes need independent delay, progress or rejection rules.
- Trade-off: strict priority can protect favored work while defeating a lower
  class's positive progress promise; capacity may make the proposed joint contract infeasible.
- Verify: offer eligible work in all claimed classes through sustained contention,
  recording scheduling, waits, completions, rejects and failed minimums separately.

## Shared-resource isolation

- Use when separate queues converge on a pool, store or downstream dependency.
- Trade-off: reservation or isolation can reduce sharing efficiency while improving
  class-specific treatment; ingress separation alone can leave downstream contention unchanged.
- Verify: trace each class across the shared bottleneck and inspect actual result
  latency/progress under the same mixed workload and resource cap.

## Per-class accounting and eligibility

- Use when an aggregate result might hide a rejected, idle or starved class.
- Trade-off: detailed accounting costs measurement work but preserves independently
  required obligations; a class with no eligible demand cannot demonstrate progress.
- Verify: retain offered, admitted, completed, rejected and unfinished work plus
  eligibility intervals; do not compensate a failed class with another's good result.
