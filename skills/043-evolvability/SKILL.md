---
name: evolvability
description: >-
  Plans successive changes with prior state and obligations carried forward when users say "will this migration block the next release", "plan the next few migrations", or "when can we remove the old bridge". Not for one code edit (see modifiability) or one capability refinement (see enhanceability).
---
# Evolvability

## Definition and scope

Evolvability means the system can accommodate a sequence of changing needs without
losing a workable path for subsequent changes. Connect design decisions, migrations,
retirement, and cumulative constraints across that sequence; distinguish the cost
of a particular edit (`modifiability`) and an isolated addition (`extendability`).

## Use when / Don't use when

- Apply when a roadmap, changing external dependency, or successive migration
  creates obligations that survive the first release.
- Examine whether a near-term change consumes the room needed by a later scenario.
- Route a plug-in point's immediate contract to `extensibility`.
- Route a standalone improvement to an existing result to `enhanceability`; revisit
  this skill when that improvement's persistent consequences affect later changes.

## Workflow

1. Clarify: Read architecture code, decision records, migration history, consumer
   lifecycles, and roadmap docs before describing an evolution path.
   Separate committed changes from speculative possibilities and list irreversible steps.
   If the horizon or likely change drivers are missing, then Ask the user for
   concrete scenarios instead of treating every imagined future as a requirement.

2. Specify: Select an ordered scenario set and record the starting state, retained
   contracts, migration obligations, retirement criteria, and cumulative change evidence.
   If the user requests an actionable plan, present this provisional itinerary:

   ```text
   Illustrative evolution itinerary; confirm with the user/stakeholder:
   Horizon: the stakeholder's named releases, not an assumed universal lifetime.
   Scenario target: rehearse 2 successive changes against retained intermediate state.
   Starting point: current code, stored data, consumers, and supported contracts.
   Constraints: preserve named consumers and data meaning until agreed retirement.
   Evidence: per-stage changes, coexistence checks, migration leftovers, later-change effort.
   Exit: remove temporary paths after their explicit consumer/data retirement evidence.
   Unresolved: scenario likelihood, cumulative effort bound, owners, irreversible decisions.
   ```

   Group the opening questions into at most three: which change drivers are credible;
   which state and consumers must survive; and what horizon, cost, or retirement
   decisions constrain the path. Move into scenario design without fabricating a roadmap.
   If no numeric scenario target is available, then propose the labeled rehearsal
   count above and confirm with the user/stakeholder; do not make it a universal minimum.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Use [evolution patterns](./references/design-patterns.md) when
   separating change boundaries, staging data transition, and retiring temporary paths.
   If a near-term shortcut blocks a committed later scenario, then compare its
   removal cost with an alternative now and expose that decision to the owner.
   If a future scenario is merely speculative, then retain an explicit decision
   point rather than building unrequested infrastructure for every possible future.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Apply the selected changes in order to the same evolving fixture,
   carrying data, configuration, and consumer versions forward between stages.
   If a later step only succeeds after recreating a clean system, then record the
   missing migration or retirement work instead of calling the sequence sustainable.

5. Report: Deliver the sequence, intermediate-state evidence, cumulative obligations,
   unresolved irreversible choices, and the triggers for revisiting the plan.
   If a scenario was not rehearsed or an owner cannot retire an old consumer, then
   mark that portion of the future path uncertain and name the evidence still needed.

## Specification patterns

- **Sequence:** The system shall admit `{ordered_change_scenarios}` from
  `{current_state}`, preserving `{retained_contracts_and_data_meanings}` at each
  intermediate stage, verified by `{sequential_migration_rehearsal}`.
- **Change budget:** Across `{planning_horizon}`, implementing `{scenario_sequence}`
  shall stay within `{confirmed_cumulative_effort_or_scope_bound}`, measured using
  `{consistent_change_cost_record}` including migration and temporary-path upkeep.
- **Retirement:** Temporary support for `{old_contract}` shall be removable after
  `{consumer_and_data_exit_conditions}`, demonstrated by `{retirement_and_replay_checks}`.

Apply the illustrative scenario count only after stakeholder confirmation. Keep effort,
horizon, and retirement conditions explicit when they cannot yet be quantified.

## Rules of thumb

- Do feed each later scenario the preceding scenario's persisted outputs and bridge
  obligations; clean snapshots erase the inherited constraints this path must accept.
- Do tie each bridge exit to the next scenario and the consumers it releases;
  don't price a later change as independent while earlier bridges still dictate its data form.
- Do exercise the named change boundary at successive stages; an abstraction that
  fits the first release but needs replacement for the next does not establish the path.
- Do test later scenarios against information discarded by earlier representation
  choices; rerouting to old code cannot reopen a future option the data no longer permits.
- Do charge bridge upkeep to every stage that still carries it and removal to its
  actual exit stage; resetting that ledger makes a costly sequence look sustainable.

## Verification

Use sequential migration rehearsals, consumer-coexistence matrices, decision review,
and change-impact analysis categories. Reconcile stage costs with the worked
ledger, including inherited upkeep and actual retirement. Compare
declared data meanings before and after each migration. Exercise retirement of an
old reader and the next planned change after retirement. Inspect shared temporary
paths, unsupported consumers, and irreversible writes. Report separate evidence
for a feasible rehearsal and for the unproven likelihood of the chosen roadmap.

## Done checklist

- [ ] Carry stage outputs and active consumer versions into each subsequent rehearsal.
- [ ] Exercise declared reader/writer combinations at intermediate stages.
- [ ] Test a later scenario against each earlier irreversible representation choice.
- [ ] Remove a bridge only after its declared consumer/data exit evidence is present.
- [ ] Reconcile cumulative cost with stage work, inherited upkeep, and actual retirement.
- [ ] Match every claimed stage to retained rehearsal evidence; flag the first gap.

## Failure modes

- Demonstrating unrelated clean-room changes and calling them an evolution sequence.
- Leaving every transitional reader or schema in place without an exit owner.
- Overbuilding for hypothetical needs while ignoring a committed migration constraint.
- Claiming reversibility after a new version has written incompatible persistent state.

## References

- Read [evolution patterns](./references/design-patterns.md) when planning change
  boundaries, coexistence, retirement, and irreversible transition decisions.
- Read [successive-change example](./references/worked-example.md) when checking
  retained-state changes and a cumulative ledger with inherited bridge costs.
