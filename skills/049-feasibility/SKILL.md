---
name: feasibility
description: >-
  Checks a delivery candidate when asked "try the offline renderer", "test dependency access", or "probe this design". Before routing build concerns, Ask the user: technical constraints, budget, or continued worth? Not for budget fit alone (see affordability) or ongoing worth (see viability).
---

# Feasibility

## Definition and scope

Feasibility means a proposed solution can be delivered within explicit technical,
organizational, and resource constraints. Evaluate a concrete delivery candidate
with evidence for its dependencies and hardest assumptions.
Separate initial achievability from budget fit alone (`affordability`) and
continued value after delivery (`viability`).

## Use when / Don't use when

- Apply when a plan relies on an inaccessible service, unproven capability,
  missing prerequisite, or capacity assumption that can block delivery.
- Include repository probes, dependency/configuration changes, bounded delivery
  alternatives, and evidence needed before committing to a candidate.
- Route a monetary cap comparison alone to `affordability`.
- Route renewing an already delivered offering over time to `viability`.
- Route whether an available capability fits a user's task to `suitability`
  when delivery under constraints is not the question.

## Workflow

1. Clarify: Read the implementation, build/deployment paths, environment
   constraints, dependency contracts, and delivery assumptions before specifying.
   Identify hard constraints and the people or artifacts needed to satisfy them.
   If a constraint or prerequisite is unknown, then Ask the user rather than
   interpreting missing evidence as permission or availability.

2. Specify: Record the required deliverable, candidate plan, constraints,
   dependency ownership, effort/capacity assumptions, and go/no-go evidence.
   If no threshold exists, then propose a labeled illustrative default:
   prove the candidate's blocking capability in the required environment and
   account for unresolved delivery work; confirm with the user/stakeholder.
   Ask at most three questions about deliverable scope, hard constraints,
   and available prerequisites/capacity before designing a probe.

3. Design/Implement: Read [delivery-candidate decisions](./references/design-guide.md)
   when selecting a constrained prototype or alternate delivery path.
   If a required service cannot be used in the target environment, then test a
   permitted alternative against the same deliverable instead of weakening the constraint.
   If a spike succeeds but production integration work remains, then keep that
   work in the candidate plan rather than equating the spike with delivery.

4. Verify: Run the blocking probe under the actual declared constraints and
   reconcile remaining tasks, prerequisites, and available capacity.
   Retain failures, incomplete probes, and unsupported environment assumptions.
   If a hard constraint is violated or unresolved, then report the candidate
   as blocked or conditional rather than unqualified feasible.

5. Report: Return the candidate comparison, probe outputs, constraint ledger,
   remaining delivery work, and decisions required to proceed.
   If only a synthetic environment was exercised, then state that limit;
   do not turn a fixture success into a project deadline promise.

## Specification patterns

- **Candidate delivery:** `{candidate}` shall deliver `{required_result}`
  within `{technical_organizational_and_resource_constraints}`, supported by
  `{blocking_probe_and_remaining_work_evidence}`.
- **Decision gate:** Proceeding with `{delivery_plan}` shall require
  `{named_prerequisites_and_probe_results}`; unresolved `{hard_constraint}`
  shall remain `{conditional_or_blocked_decision}`.

Use the illustrative blocking-probe proposal in Specify when no numeric budget
is provided; confirm with the user/stakeholder before accepting a delivery claim.

## Rules of thumb

- Keep hard environment constraints in the candidate comparison; a successful
  remote call is irrelevant when delivery must work with external networking disabled.
- Charge unimplemented integration and prerequisite work to the proposed delivery
  path even after a spike passes; the probe is evidence, not the finished deliverable.
- Check that dependent prerequisites and delivery capacity share a usable window;
  separately available components and staff do not establish an executable delivery path.

## Verification

Use constrained prototypes, dependency inspection, and delivery-work review.
Capture required inputs, environment restrictions, actual outputs, and missing
prerequisites beside each candidate.
Run the same deliverable case through alternatives so scope changes stay visible.
Exercise the potentially blocking required output, not an easier placeholder.
Distinguish completed work, estimates, and owner commitments.
Check that capacity assumptions describe the actual delivery window and people.
Do not convert a task count into a calendar estimate without supplied support.
Keep conditional evidence separate from a confirmed go decision.

## Done checklist

- [ ] Define the deliverable and hard constraints.
- [ ] Identify dependencies and their actual availability.
- [ ] Choose a probe for a potentially blocking capability.
- [ ] Run it in the declared constrained environment.
- [ ] Compare candidate outputs with the unchanged deliverable.
- [ ] Account for remaining integration and prerequisite work.
- [ ] Reconcile capacity assumptions with the candidate plan.
- [ ] Report blocked, conditional, and confirmed evidence distinctly.

## Failure modes

- Calling a cheap option feasible despite an inaccessible required dependency.
- Testing a placeholder and claiming the hard capability is proven.
- Treating a successful spike as completed production integration.
- Relaxing a hard environment constraint without stakeholder agreement.

## References

- Read [delivery-candidate decisions](./references/design-guide.md) when choosing
  a constrained probe and an alternate delivery path.
- Read [offline renderer example](./references/worked-example.md) when separating
  capability evidence from the work still needed to deliver it.
