---
name: agility
description: >-
  Handles reprioritized delivery when users say "the roadmap changed again", "swap in this urgent feature", or "feedback changed what we should ship". Not for progressing one unchanged request (see changeability) or reducing code-edit effort (see modifiability).
---
# Agility

## Definition and scope

Agility means the delivery process can respond to changed priorities while retaining
agreed constraints. Evaluate reprioritization and displaced commitments; distinguish
one request's lifecycle (`changeability`), implementation impact (`modifiability`),
and accommodating changed operating conditions (`adaptability`).

## Use when / Don't use when

- Apply when feedback changes what should be delivered next and that decision
  needs an inspectable path through revised planning to accepted delivery.
- Route an unchanged request stuck at a handoff to `changeability`.
- Route faster implementation of one edit to `modifiability`; faster completion
  alone does not establish response to a changed priority.

## Workflow

1. Clarify: Read delivery docs, backlog history, release code/configuration,
   acceptance gates, and decision records before specifying responsiveness.
   If no priority actually changed, then Ask the user whether the problem is an
   individual stuck request or implementation effort instead of reprioritization.

2. Specify: Set priority-event evidence, response endpoints, elapsed-time rules,
   retained gates, displaced-work treatment, and a delivery decision owner.
   If the user wants practical process improvement, then propose this record:

   ```text
   Illustrative replanning record; confirm with the user/stakeholder:
   Trigger: recorded stakeholder decision changing ordered delivery priorities.
   Example bound: accepted revised plan within 2 working days of that event.
   Clock: stakeholder working calendar; waits remain visible, not silently removed.
   Constraints: existing acceptance, release, and decision-authority gates.
   Consequences: paused commitments, preserved artifacts, owners, restart conditions.
   Delivery evidence: accepted new-priority outcome, separate from plan response timing.
   Open decisions: calendar, timing, scope, displaced-work acceptance, owner approval.
   ```

   Ask at most three question groups: changed priority; retained/displaced
   commitments; and response endpoints, calendar, or defaults needing revision.
   Proceed to a reversible plan alternative without approving commitments yourself.
   If no target is supplied, then offer the illustrative planning bound above
   and confirm with the user/stakeholder; do not imply that it commits delivery time.

3. Design/Implement: Read [response patterns](./references/design-patterns.md) when
   slicing an urgent outcome or preserving interrupted work.
   If an urgent slice bypasses a retained gate, then revise its scope or obtain
   the owner's explicit constraint decision rather than calling the omission agility.
   If the new order blocks another commitment, then expose its displaced result,
   restart condition, and owner before presenting the revised plan as feasible.

4. Verify: Replay a priority event through plan revision and a scoped delivery
   rehearsal; compare commitments and gate evidence before and after the event.
   If only backlog ordering changed, then leave delivery responsiveness unverified
   until the new slice crosses its accepted outcome boundary.

5. Report: Return event-to-plan timing, later delivery evidence, waits,
   constraints retained, and interruption or displaced-work consequences.
   If waiting or unfinished work was excluded, then disclose that boundary and
   withhold a broader claim about delivery response.

## Specification patterns

- **Replan:** After `{priority_event}`, `{process}` shall produce
  `{accepted_revised_plan}` within `{confirmed_response_bound}` under `{calendar}`,
  retaining `{delivery_constraints}` and naming `{displaced_commitments}`.
- **Delivery:** The reprioritized `{outcome_slice}` shall reach `{accepted_endpoint}`
  by `{confirmed_commitment}`, evidenced by `{gate_and_result_records}` including
  `{waiting_time_rule}` from `{decision_event}`.
- **Interruption:** Pausing `{displaced_work}` shall retain `{restart_artifacts}`
  under `{restart_condition}`, verified by `{resume_rehearsal}`.

Use the illustrative planning bound only as an initial proposal;
confirm with the user/stakeholder. Ask the user before assuming a working calendar.

## Rules of thumb

- Do compare the plan before and after a priority event; finishing work already
  first in the queue cannot demonstrate response to changed priorities.
- Do slice by an accepted outcome of the new priority; smaller tickets without
  a deliverable result can improve planning statistics while leaving that priority unmet.
- Do carry displaced commitments into the revision; deleting them makes a
  reprioritization look cheap by erasing the work it interrupted.
- Do replay the new-priority slice against the prior plan's retained gates; faster
  response bought by deleting a gate changes the constraint, not delivery responsiveness.
- Do charge dependency waits to the changed priority's elapsed timeline; pausing
  its clock while another owner is needed conceals the bottleneck being assessed.

## Verification

Use event-history review, plan-difference analysis, and delivery rehearsal.
Follow the same changed priority from decision through accepted outcome; preserve
waits, rejected plans, paused artifacts, and gate results. Rehearse restarting
interrupted work without rebuilding unrecorded decisions. Observe priority churn
and unfinished urgent slices alongside response timing; a short plan interval
cannot establish that the new priority was actually delivered.

## Done checklist

- [ ] Match the priority event to a demonstrably revised order or scope.
- [ ] Recompute planning response under the agreed calendar and waiting rule.
- [ ] Trace the urgent slice to its accepted outcome rather than ticket closure.
- [ ] Inspect retained gate evidence on the revised delivery path.
- [ ] Reconcile displaced commitments with artifacts and restart conditions.
- [ ] Resume paused work or mark that preservation claim untested.

## Failure modes

- Measuring unchanged queue throughput as response to reprioritization.
- Stopping response timing while a dependency blocks the new priority.
- Delivering an urgent slice by silently dropping a retained gate.
- Erasing interrupted commitments to hide their cost.

## References

- Read [response patterns](./references/design-patterns.md) when selecting priority
  events, outcome slices, or displaced-work decisions.
- Read [replanning example](./references/worked-example.md) when distinguishing
  an accepted revised plan from verified delivery of its new priority.
