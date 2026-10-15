---
name: stability
description: >-
  Bounds drift and oscillation within a stated operating envelope when users say "stop this control from flapping", "the behavior drifts even with steady inputs", or "keep repeated adjustments from oscillating". Separates settling, held conditions, directional drift, and recurring reversals. Not for failure occurrence alone (see reliability), general outcome variation (see predictability), or one operation's timing bound (see performance-efficiency-time-or-space-bounds).
---
# Stability

## Definition and scope

Stability means behavior avoids unacceptable drift or oscillation within a
stated operating envelope. Separate expected transitions and settling from
persistent trends or reversals; distinguish failure occurrence (`reliability`),
general outcome variation (`predictability`), and ordinary timing targets
(`performance-efficiency-time-or-space-bounds`).

## Use when / Don't use when

- Apply when modes flap, a feedback adjustment repeatedly reverses, or behavior
  drifts while relevant inputs and environmental conditions are held within scope.
- Route noisy response-time distributions without a drift/control question to `predictability`.
- Route crashes under ordinary workload to `reliability` and sustained resource
  containment under adverse traffic to `robustness` when those are the actual outcomes.

## Workflow

1. Clarify: Read feedback/control code, scheduling and measurement windows,
   configuration docs, time-series evidence, and operating-envelope assumptions first.
   If the apparent drift coincides with changed demand or environment, then
   separate that response from unexplained behavior under held conditions.

2. Specify: Choose observed variable/mode, inputs, operating envelope, sampling,
   initial conditions, settling rule, trend/reversal criteria, and required responsiveness.
   If the user wants a flapping fix, then offer this behavior-trace record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Variable/context: named control output and documented operating envelope.
   Trace: input, measured signal, chosen action/mode, time, and measurement freshness.
   Trial: after agreed settling, no further mode reversals during 10 minutes of held-input observation.
   Held conditions: recorded workload/environment bands; changed conditions are separate cases.
   Design limits: retain required response to genuine changes; freezing the output is not acceptance.
   Evidence: baseline/candidate traces, transition counts, directional drift, and missed responses.
   Unknowns: settling/bands and acceptable response delay remain stakeholder choices.
   ```

   Ask at most three groups about the drifting/flapping variable and inputs;
   envelope/settling/allowed change; and response obligations or proposed criteria.
   Continue to a bounded control/measurement design with unknown limits visible.
   If no target exists, then propose the illustrative held-input trial and confirm
   with the user/stakeholder before adopting its duration or no-reversal criterion.

3. Design/Implement: Read [drift-and-oscillation practices](./references/design-patterns.md)
   when choosing transition bands, dwell, measurement alignment, or feedback checks.
   If noise around a boundary drives reversals, then evaluate explicit transition
   rules against genuine-change response rather than hiding the reversals in an average.
   If control actions alter the measured input, then trace that feedback path
   before adding another independent controller that could amplify the oscillation.

4. Verify: Record held-condition and deliberate-change traces with the same
   sampling and initial-state rules; inspect post-settling drift, reversals, and response.
   If apparent calm comes from disabled control or missing samples, then reject
   that stability claim and retain the responsiveness or observation failure.

5. Report: Return the envelope, changed control/measurement rules, complete
   traces, settling/transient exclusions, and remaining drift or missed-response cases.
   If only averages or a short unsampled interval are available, then leave the
   claimed bound unverified rather than calling a smooth dashboard stable behavior.

## Specification patterns

- **Held-condition behavior:** Under `{input_and_environment_envelope}`, after
  `{confirmed_settling_rule}`, keep `{variable_or_mode}` within `{confirmed_drift_and_reversal_limits}`
  over `{observation_window}`, verified by `{aligned_input_output_action_trace}`.
- **Responsive stability:** For `{declared_input_change}`, achieve `{required_response}`
  within `{confirmed_response_condition}` while respecting `{oscillation_or_drift_bounds}`,
  verified by `{changed_condition_trace_and_control_state_checks}`.

Use the illustrative held-input trial when no bound exists; confirm with the
user/stakeholder. Ask the user for settling, sampling, and responsiveness rather than prescribing universal thresholds.

## Rules of thumb

- Don't average away alternating control states; a quiet mean can conceal the
  repeated reversals that the mode-stability requirement actually forbids.
- Do separate genuine input changes from held-condition drift; responding to
  changing demand is not itself evidence that a controller is unstable.
- Do evaluate a transition band or dwell rule against missed genuine changes;
  a frozen or sluggish output can stop flapping while failing the required response.
- Do align input, action, and observation windows before attributing oscillation;
  stale measurements can make a justified response look like self-generated reversal.
- Do trace coupled feedback decisions together; independently reasonable controllers
  can reverse each other's actions and defeat the declared steady operating behavior.
- Don't exclude unsettled intervals after seeing the candidate trace; the agreed
  settling rule must determine which reversals count toward the accepted bound.

## Verification

Use time-aligned trace analysis, controlled held/changed-input trials, and feedback
state inspection categories. Retain mode transitions and directional trends,
not only means. Check measurement freshness, sampling gaps, input/environment
bands, initial conditions, and required response. Inspect coupled controllers;
fewer transitions alone can conceal an unresponsive system rather than establish acceptable stability.

## Done checklist

- [ ] Record variable/mode, envelope, initial state, sampling, and settling rules.
- [ ] Align input, measured signal, action, and output timestamps in retained traces.
- [ ] Inspect post-settling drift and reversal counts under held conditions.
- [ ] Test genuine input changes against the required response obligation.
- [ ] Check that missing samples or disabled control did not manufacture apparent calm.
- [ ] Inspect coupled feedback paths and their combined action trace.
- [ ] Disclose changed conditions and exclusions before claiming the agreed bound.

## Failure modes

- Reporting a smooth average while the actual mode repeatedly reverses.
- Calling justified response to changing demand unexplained drift.
- Preventing oscillation by disabling necessary response to real changes.
- Comparing misaligned input and action windows as if they describe one control decision.
- Choosing settling exclusions after inspecting unfavorable reversals.

## References

- Read [drift-and-oscillation practices](./references/design-patterns.md) when changing
  transition logic, sampling, or interacting feedback decisions.
- Read [queue-mode example](./references/worked-example.md) when tracing flapping
  under steady demand without accepting a frozen control as the fix.
