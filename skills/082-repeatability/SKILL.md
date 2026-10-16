---
name: repeatability
description: >-
  Checks reruns with held conditions when asked "repeat the same fixture", "keep setup unchanged", or "compare repeated outputs". Ask the user if same setup vs independent reconstruction is unclear. Not for independent reconstruction elsewhere (see replicability) or bounds on service variation (see predictability).
---

# Repeatability

## Definition and scope

Repeatability means a defined procedure produces sufficiently consistent results
when rerun by the same executor under held conditions. Specify the run boundary,
carried state, and comparison rule; distinguish independent reconstruction
(`replicability`) and operational outcome variation (`predictability`) from
repeated execution of this procedure in this setup.

## Use when / Don't use when

- Apply when rerunning an unchanged fixture gives conflicting answers.
- Apply when hidden state, time, or ordering changes between supposedly identical runs.
- Route reconstruction by another executor or environment to `replicability`.
- Route variation of a running service under an operating profile to `predictability`.
- Route a missing way to force a test branch to `testability`.

## Workflow

1. Clarify: Read the procedure, fixture loaders, state stores, runner settings,
   clock/random inputs, and prior run artifacts before choosing held conditions.
   Identify the executor and the exact action that starts and ends a run.
   If "it varies" does not identify a procedure or held setup, then Ask the user
   whether this is rerun consistency, service behavior, or independent reconstruction.

2. Specify: Record the executor, code and fixture revisions, initial state,
   permitted carry, controlled inputs, run count, and output comparison.
   If no rerun plan exists, then propose labeled illustrative defaults:
   3 sequential runs from the same recorded initial state with exact comparison
   of the required result; confirm with the user/stakeholder.
   Separate meaningful result fields from variable metadata before collecting runs.

3. Design/Implement: Read [rerun design](./references/design-guide.md) when
   deciding whether reset, isolation, or explicit nondeterministic inputs are needed.
   If a run consumes state that should restart, then make that initialization
   part of the procedure. If state is intended to carry, then record its next-run
   value rather than erasing it to obtain matching outputs.
   If result order is irrelevant by contract, then define a comparison that
   preserves multiplicity and required content instead of sorting away a defect.

4. Verify: Execute the predeclared rerun sequence and retain every result,
   failure, timeout, initial-state snapshot, and deviation from held conditions.
   If a claimed fixed input actually changes, then classify the sequence as a
   condition mismatch and rerun after repair; do not infer inherent randomness.
   Read [invoice rerun example](./references/worked-example.md) when diagnosing
   a nominally identical fixture whose hidden counter carries between runs.

5. Report: Return the run manifest, comparison outcomes, condition deviations,
   and supported scope of consistency.
   If the run set is small or the setup differs from production, then report that
   limit rather than claiming deterministic behavior in every environment.

## Specification patterns

- **Held setup:** Repeating `{procedure}` by `{same_executor}` for
  `{confirmed_run_count}` runs under `{held_setup_and_initial_state}` shall
  produce outputs satisfying `{comparison_rule_and_tolerance}`.
- **Carry policy:** Between runs of `{procedure}`, `{state_to_reset}` shall
  return to `{recorded_initial_values}` while `{intentional_carry}` follows
  `{declared_transition}`, verified by `{per_run_manifest}`.

For an absent run count, use the illustrative proposal in Specify and confirm
with the user/stakeholder; a chosen finite run set is evidence, not a universal guarantee.

## Rules of thumb

- Do define the reset boundary as part of the repeated procedure; matching fixture
  files do not make runs equivalent when a consumed counter carries invisibly.
- Do preserve intentional cross-run state in the rerun contract; resetting it
  just to force matching outputs tests a different procedure.
- Do name the executor and setup held across reruns; a fresh reconstruction by
  another team cannot establish this same-setup claim by substitution.

## Verification

Use rerun harness, state-snapshot, output-diff, and controlled-input categories.
Inspect starting state before each invocation, not only after a failure.
Record clock inputs, random-input control, dependency responses, and ordering
where they affect the required result.
Compare meaningful outputs with the predeclared equivalence rule and preserve
duplicates when order is ignored.
Do not remove a differing output field after observing it; decide whether it
belongs to the required repeated result before collecting runs.
Keep raw outputs, failed runs, timeouts, unfinished runs, and condition mismatches
visible in the run ledger; report the intended and actually completed run counts.
Do not exclude a failed run merely because a later rerun passes.
Distinguish observed consistency from an explanation of its cause.

## Done checklist

- [ ] Identify the procedure's run boundary and unchanged executor/setup.
- [ ] Capture fixture and implementation revisions with the rerun manifest.
- [ ] Inspect each run's starting state against the reset/carry contract.
- [ ] Fix the result fields and comparison rule before running the sequence.
- [ ] Retain every run outcome and any incomplete execution.
- [ ] Compare outputs without discarding meaningful order or multiplicity.
- [ ] Separate condition mismatches from observed result variation.
- [ ] Limit consistency claims to the actual rerun conditions and evidence.

## Failure modes

- Calling fixtures identical while leaving a consumed identifier counter unreset.
- Dropping failed runs and reporting only the successful rerun streak.
- Normalizing away a required output difference after seeing it.
- Resetting state the real procedure is required to carry.
- Calling another environment's successful reconstruction same-setup evidence.

## References

- Read [rerun design](./references/design-guide.md) when choosing reset boundaries,
  isolation, controlled inputs, and meaningful output comparison.
- Read [invoice rerun example](./references/worked-example.md) when separating
  a hidden-state mismatch from a claim about intrinsic nondeterminism.
