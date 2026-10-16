---
name: debuggability
description: >-
  Localizes a captured execution when asked "replay a parser crash", "trace this bad value", or "inspect a failing input". Before routing debugging, Ask the user: one execution, wider causes, or missing test controls? Not for system-wide cause or change-impact analysis (see analyzability) or adding test seams (see testability).
---

# Debuggability

## Definition and scope

Debuggability means a particular failing execution can be reproduced or inspected
well enough to locate its defect. Connect the captured input and state to the
first meaningful divergence; distinguish system-level cause and impact analysis
(`analyzability`) and general test seams (`testability`) from this execution's
localization path.

## Use when / Don't use when

- Apply when an input crashes a parser but the stack ends after the wrong value was chosen.
- Apply when a defect cannot be isolated from a failing trace or captured state.
- Route consumer/dependency impact across the system to `analyzability`.
- Route missing runtime signals for state inference to `observability`.
- Route general branch-control capability without a particular failure to `testability`.

## Workflow

1. Clarify: Read the failing path, input contract, source/build mapping, tests,
   and available execution artifacts before adding diagnostics.
   Identify the actual symptom and expected result from an authoritative contract.
   If the failure cannot be tied to an input and revision, then Ask the user for
   the smallest available capture and keep localization provisional.

2. Specify: Record the input, initial state, revision, environment dependencies,
   expected result, observed failure, and localization evidence sought.
   If no debugging criterion is given, then propose labeled illustrative defaults:
   reproduce the named failure and identify the earliest value/branch divergence
   supported by an inspectable capture; confirm with the user/stakeholder.
   Treat a missing reproducer as an explicit limitation, not permission to invent one.

3. Design/Implement: Read [localization design](./references/design-guide.md)
   when choosing replay, capture points, or source mapping.
   If the exception sees an already corrupted value, then inspect the value's
   selection boundary. If input reduction changes the symptom, then restore the
   required trigger rather than reporting an unrelated smaller failure.
   Keep temporary diagnostic changes scoped to the failing path.

4. Verify: Replay the capture and compare actual versus expected values at the
   suspected boundary. Test a minimal corrective change and neighboring inputs.
   If the capture cannot distinguish alternative explanations, then collect a
   discriminating value before claiming a located defect.
   Preserve failed attempts, source revisions, and any environment substitutions.
   Read [parser localization example](./references/worked-example.md) when
   separating a conversion exception from the earlier field-selection defect.

5. Report: Return the reproducer or inspection record, first supported divergence,
   corrective experiment, and unresolved replay dependencies.
   If only a workaround removes the visible error, then report that limitation
   instead of declaring the underlying defect localized.

## Specification patterns

- **Localization:** For `{failing_input_and_revision}`, the debugging procedure
  shall expose `{expected_and_actual_values}` at `{candidate_boundary}`,
  sufficient to distinguish `{competing_local_explanations}`.
- **Replay:** The captured `{input_and_initial_state}` shall reproduce
  `{named_symptom}` under `{recorded_dependencies}`; unavailable dependencies
  shall be identified as `{replay_limits}`.

Use the illustrative localization criterion in Specify when no timing target
exists and confirm with the user/stakeholder; do not invent a universal time-to-debug promise.

## Rules of thumb

- Do inspect the value before the operation that finally throws; a late exception
  can identify the symptom while hiding an earlier selection defect.
- Don't suppress the exception and call the execution understood; preserve a
  supported explanation of where the expected path first diverges.
- Do map captured stack locations to the source revision that produced them;
  a nearby line in another build is not a localized expression.

## Verification

Use deterministic replay where supported, debugger inspection, targeted capture,
and focused regression categories.
Retain the original failure while reducing the input, and compare the symptom
rather than merely checking that some exception still occurs.
Record substituted dependencies and temporary instrumentation because either
can change the observed path.
Inspect the candidate value immediately before conversion or mutation.
Use a corrective experiment to test the proposed localization, then replay a
nearby valid and invalid input.
A passing patch supports the stated local explanation only within its checked scope.

## Done checklist

- [ ] Tie the symptom to a captured input and implementation revision.
- [ ] State the expected result independently of the failing expression.
- [ ] Reproduce or explicitly bound the inspectable failing execution.
- [ ] Compare expected and actual values at the suspected divergence.
- [ ] Map trace locations to the matching source artifact.
- [ ] Exercise a corrective experiment and neighboring inputs.
- [ ] Report replay substitutions and remaining localization uncertainty.

## Failure modes

- Treating the final thrown exception as proof of the original defect.
- Reducing the input until a different bug replaces the original symptom.
- Reading a stack trace against mismatched source.
- Returning a default value that hides the error without explaining the path.

## References

- Read [localization design](./references/design-guide.md) when selecting
  replay dependencies, capture points, and source correspondence.
- Read [parser localization example](./references/worked-example.md) when
  tracing a particular conversion failure back to the value-selection boundary.
