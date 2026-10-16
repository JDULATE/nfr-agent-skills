---
name: quality-of-service
description: >-
  Defines differentiated treatment for explicit service classes sharing constrained resources when users say "protect interactive work from batch jobs", "give background jobs a minimum share", or "keep one tenant from starving another class". Binds trusted classification, admission, scheduling and per-class outcomes under contention. Not for one operation's envelope alone (see performance-efficiency-time-or-space-bounds), generic workload growth (see scalability), or permission to access data (see accessibility-access-control).
---
# Quality of Service

## Definition and scope

Quality of service means explicit service classes receive agreed treatment while
sharing constrained resources. Bind class identity, admission, scheduling and
per-class outcomes; distinguish one operation envelope
(`performance-efficiency-time-or-space-bounds`), growth behavior (`scalability`)
and action permission (`accessibility-access-control`).

## Use when / Don't use when

- Apply when interactive, background, tenant or other defined classes interfere
  and need different latency, progress, admission or rejection treatment.
- Route a single homogeneous workload's timing envelope to
  `performance-efficiency-time-or-space-bounds`.
- Ask the user whether a better tier means service treatment or permission to
  access an operation/data; scheduling class is not an authorization grant.

## Workflow

1. Clarify: Read classification, queues, schedulers, shared pools, admission code
   and service-policy docs before assigning priorities or shares.
   If callers can label their own privileged class, then identify the trusted
   entitlement/classification source rather than treating a request field as authority.

2. Specify: Record classes, trusted assignment, offered mix, shared bottleneck,
   per-class targets, rejection/progress rules, capacity assumptions and evidence.
   If the user asks to protect interactive work, then offer this class contract:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Classes: stakeholder-defined interactive and batch work with trusted assignment.
   Interactive trial: p95 completed elapsed time at most 300 ms in the agreed mixed load.
   Batch trial: at least 1 correct job completes per minute while its declared queue is eligible.
   Scope: explicit offered mix, resource cap, admitted load and measurement window.
   Accounting: per-class admitted/completed/rejected/unfinished work; no hidden lower-class loss.
   Constraints: permission, result correctness and declared capacity assumptions remain separate.
   Evidence: assignment decisions, queue/wait/service traces and per-class outcomes under contention.
   Status: proposed paired obligations, not a universal priority scheme or feasible-capacity proof.
   ```

   Ask at most three groups about classes/entitlements; workload/resource envelope
   and obligations for each class; and rejection, progress or acceptance constraints.
   Continue to a bounded scheduler/admission design with unresolved capacity visible.
   If no targets exist, then offer the illustrative paired trial and confirm
   with the user/stakeholder before accepting its class limits or progress window.

3. Design/Implement: Read [class-treatment practices](./references/design-patterns.md)
   when selecting admission, isolation, priority or minimum-progress handling.
   If strict priority starves a class with a positive progress obligation, then
   revise admission/scheduling or negotiate the conflicting contract instead of dropping that obligation.
   If classes share downstream pools, then inspect that contention too; separate
   ingress queues alone cannot establish differentiated end-to-end treatment.

4. Verify: Exercise the declared mix during contention, inspect trusted assignment
   and retain each class's completion, delay, rejects and unfinished work.
   If an aggregate pass hides a class failure, then fail that class contract;
   the favored class's success cannot compensate for an independently required minimum.

5. Report: Return class policies, implementation changes, resource/mix assumptions,
   per-class results, infeasible points and missing evidence.
   If a class was not offered eligible work during the run, then leave its progress
   guarantee unverified rather than calling an empty queue a successful fairness test.

## Specification patterns

- **Differentiated treatment:** Under `{mixed_workload_and_capacity}`, assign
  `{classes}` through `{trusted_classification}` and meet `{per_class_bounds}`,
  verified by `{class_queue_completion_rejection_and_wait_traces}`.
- **Minimum progress:** While `{class_eligible_and_contention_conditions}` hold,
  provide `{confirmed_progress_or_wait_rule}` with `{admission_and_rejection_policy}`,
  verified by `{contention_and_class_spoofing_cases}` without `{aggregate_masking}`.

Use the illustrative paired class trial if targets are absent; confirm with the
user/stakeholder. Ask the user how to resolve obligations that cannot coexist within available capacity.

## Rules of thumb

- Don't use an aggregate latency pass to accept every service class;
  one class can satisfy it while another violates its own declared treatment.
- Do test lower-class progress under sustained favored-class demand when that
  progress is required; an idle favored queue cannot expose starvation.
- Don't apply strict priority blindly when another class has a positive minimum;
  preserving the favored class alone can violate the joint service contract.
- Do derive class entitlement from the trusted policy source; a caller labeling
  itself urgent must not silently seize the protected resource treatment.
- Do inspect downstream shared pools after separating ingress queues;
  hidden recombination can erase the end-to-end differentiation the classes were promised.
- Do count admitted, rejected and unfinished work by class; rejecting one class
  without the agreed policy cannot become an apparent scheduling-quality improvement.

## Verification

Use mixed-class load trials, scheduler/admission integration and class-policy
inspection categories. Retain actual assignment, offered mix, queue/wait/service
outcomes, rejects and progress windows for each class. Exercise privileged-class
spoofing and lower-class eligibility. Record capacity assumptions and downstream
contention; a priority flag or an empty batch queue alone establishes no differentiated service contract.

## Done checklist

- [ ] Define trusted classes, entitlements and offered/admitted mixed workload.
- [ ] Record independent per-class bounds, minimums and rejection rules.
- [ ] Inspect classification against caller-controlled labels.
- [ ] Exercise sustained contention with eligible work in each claimed class.
- [ ] Verify downstream shared resources preserve the intended treatment.
- [ ] Retain per-class completion, wait, rejection and unfinished results.
- [ ] Check every class independently instead of compensating through an aggregate.
- [ ] Disclose infeasible capacity points and unoffered class-progress cases.

## Failure modes

- Passing aggregate latency while background or another tenant class starves.
- Letting callers self-assign a protected priority without trusted entitlement.
- Separating ingress queues but sharing an uncontrolled downstream bottleneck.
- Dropping a lower-class obligation to make the favored class look successful.
- Claiming a progress minimum when no eligible work was offered in that class.

## References

- Read [class-treatment practices](./references/design-patterns.md) when choosing
  classification, admission, isolation or a minimum-progress mechanism.
- Read [interactive-and-batch example](./references/worked-example.md) when a favored
  class passes its latency trial but the joint treatment contract still fails.
