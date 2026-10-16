---
name: measurability
description: >-
  Defines a property's measurement procedure when tickets say "what exactly are we counting", "these dashboards use different units", or "how do we measure queue delay". Not for inferring hidden runtime state (see observability) or selecting acceptance evidence (see verifiability).
---

# Measurability

## Definition and scope

Measurability means a property can be expressed through a defined observation
procedure with interpretable units and results. Establish what is measured and
whether its instrument can distinguish the needed values; separate that task
from diagnosing hidden state (`observability`) and selecting evidence for a
requirement's acceptance (`verifiability`).

## Use when / Don't use when

- Apply when teams cannot define what a dashboard number actually counts.
- Apply when unit labels, observation boundaries, or instrument resolution conflict.
- Route explaining why a runtime condition occurred to `observability`.
- Route choosing proof, inspection, or tests for an acceptance claim to `verifiability`.
- Route an already defined operation's speed objective to
  `performance-efficiency-time-or-space-bounds`.

## Workflow

1. Clarify: Read existing queries, event producers, schemas, clock sources, and
   metric documentation before defining a new number. Identify the intended
   property and the decision a measurement must support.
   If the user asks for "better numbers" without a property or decision, then
   Ask the user what observable distinction the result must make.

2. Specify: Record the measured property, entity, start/end observations, unit,
   eligible population, aggregation, resolution, missing-data policy, and owner.
   If no measurement contract exists, then propose labeled illustrative defaults
   for the requested property: discovered entity and event boundaries, explicit
   output units, and separate unresolved observations; confirm with the user/stakeholder.
   For queue delay, propose paired admission/start events and milliseconds;
   for another property with unknown boundaries or units, Ask the user.
   Do not invent a queue-delay acceptance target from that metric definition.

3. Design/Implement: Read [measurement design](./references/design-guide.md)
   when repairing observation boundaries, dimensional meaning, or resolution.
   If producers emit different units, then convert at an explicit boundary and
   retain source units. If a required event is unavailable, then add a supported
   observation or label the proposed proxy rather than silently renaming it.
   If a known input change is smaller than the instrument can resolve, then
   revise the instrument or narrow the decision it can support.

4. Verify: Recompute the measure from a fixture with known event pairs, a unit
   conversion, and an unresolved observation. Preserve raw samples, exclusions,
   pairing failures, and unfinished work outside the completed-value summary.
   If the procedure disagrees with the fixture or masks needed distinctions,
   then report it unsuitable for that decision even if a dashboard renders.
   Read [queue-delay example](./references/worked-example.md) for filled inputs.

5. Report: Return the measurement record, instrument changes, fixture results,
   supported distinctions, and missing coverage.
   If only a proxy or coarse instrument is available, then report its limits
   beside the result and keep the intended property unmeasured where appropriate.

## Specification patterns

- **Operational definition:** For `{property_and_entity}`, compute
  `{formula}` from `{observation_boundaries}` in `{unit}` over
  `{eligible_population}`, using `{aggregation_and_missing_data_policy}`.
- **Instrument fitness:** The measurement procedure shall distinguish
  `{decision_relevant_input_difference}` under `{collection_conditions}`,
  verified using `{known_input_fixture}` with `{confirmed_resolution}`.
- **Interpretation:** The reported measure shall retain `{source_unit_and_lineage}`
  and expose `{unresolved_observations}` separately from `{computed_results}`.

For an unspecified resolution, propose an illustrative instrument choice from
the discovered event source and confirm with the user/stakeholder.
Use a known-input test before claiming that its resolution is sufficient.

## Rules of thumb

- Do name the observed construct precisely: creation-to-start job age is not
  admission-to-start queue residence merely because both are durations.
- Don't turn ordered status labels into equally spaced quantities unless that
  spacing has a defined interpretation for the chosen measurement.
- Do use a known expected reading to judge whether the instrument can measure the
  chosen property; failed calibration is a method gap, not a system diagnosis.
- Do keep measurement fitness separate from the property's acceptance threshold;
  defining a queue-delay measure does not select an acceptable queue-delay budget.

## Verification

Use event-capture, query review, unit-conversion, and known-input calibration
categories. Recompute paired observations independently of the dashboard query.
Inspect entity identity and producer clock domains before subtracting timestamps.
Test a mixed-unit fixture and an input difference near collection resolution.
Check units in the value-producing expression, not just the dashboard label.
Distinguish a recorded zero from a value below the instrument's resolution;
the latter cannot establish absence of the measured phenomenon.
Report numerator, denominator, raw samples, predeclared exclusions, and unresolved
or censored observations where those are part of the chosen measure.
Keep incomplete work visible; excluding it from a completed-pair duration is not
evidence that it had zero delay.
Separate instrument overhead or missing events from the property's actual value.
A defined measure does not, by itself, diagnose why the measured value occurred.

## Done checklist

- [ ] Name the property, measured entity, and intended decision.
- [ ] Locate the actual observation boundaries and their clock domains.
- [ ] Recompute the expression with its source and output units.
- [ ] State population, aggregation, exclusions, and missing-data handling.
- [ ] Recover known values from the calibration fixture.
- [ ] Check whether the instrument resolves the intended decision difference.
- [ ] Expose unresolved pairs beside the computed result.
- [ ] Distinguish direct measurement from a proposed proxy in the report.

## Failure modes

- Reporting job age under a queue-residence label.
- Subtracting timestamps from unrelated clock domains without a mapping.
- Mixing seconds and milliseconds while averaging apparently comparable values.
- Publishing a precise-looking zero from an instrument too coarse to detect the effect.
- Treating absent end events as completed work with zero duration.

## References

- Read [measurement design](./references/design-guide.md) when choosing the
  observation boundary, unit conversion, or resolution intervention.
- Read [queue-delay example](./references/worked-example.md) when validating a
  metric definition against filled event pairs and incomplete work.
