---
name: sustainability
description: >-
  Connects resource and lifecycle choices to an explicit environmental or long-term stewardship objective when users say "reduce energy for this workload", "extend the useful life of these devices", or "show the lifecycle tradeoffs of this optimization". Names functional output, system boundary, horizon and measurement or evidence limits. Not for resource cost per operation alone (see efficiency-device-efficiency), financial cost alone (see affordability), or continued business value alone (see viability).
---
# Sustainability

## Definition and scope

Sustainability means resource and lifecycle choices address an explicitly chosen
environmental or long-term stewardship objective. Define functional output,
system/lifecycle boundary and horizon; distinguish device resource ratios
(`efficiency-device-efficiency`), financial constraints (`affordability`) and
continued stakeholder value (`viability`).

## Use when / Don't use when

- Apply when the stakeholder selects energy use, device service life, lifecycle
  impact or another explicit stewardship outcome as the acceptance objective.
- Ask the user what sustainability means for this project; do not assume a
  particular environmental metric or that newer hardware is the desired outcome.
- Route CPU/bytes per operation alone to `efficiency-device-efficiency` and
  cost reduction alone to `affordability`.

## Workflow

1. Clarify: Read workload/resource code, device/lifecycle docs, retained measurement
   evidence and stakeholder objectives before proposing a stewardship change.
   If the objective, boundary or source of impact data is unknown, then Ask the
   user; resource savings alone do not establish environmental or lifecycle benefit.

2. Specify: Record stewardship objective, functional output/quality, boundary,
   horizon, measured/proxy data, allocation, exclusions and lifecycle tradeoffs.
   If the user wants an energy improvement, then propose this bounded record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Objective: lower measured operational energy per correct useful output in the named boundary.
   Trial target: 10% lower metered energy per output against the confirmed baseline.
   Functional unit: unchanged useful task/quality and required service conditions.
   Scope/horizon: declared device/process/system boundary and comparison period, including idle allocation.
   Evidence: measured energy, useful outputs, conditions, data provenance and uncertainty.
   Lifecycle: acquisition/replacement/retirement impacts reported unknown or separately supported.
   Limits: no emissions or total-lifecycle conversion inferred from CPU, price or a device label.
   ```

   Ask at most three groups about objective/output; boundary, horizon and available
   evidence; and target, device-life or service tradeoffs. Continue to options tied to that objective.
   If no numeric criterion exists for the chosen energy objective, then offer the
   illustrative trial and confirm with the user/stakeholder before adopting it.
   If the chosen objective is device life instead, then specify usable-service
   and retirement evidence with the user rather than imposing the energy target.

3. Design/Implement: Read [stewardship-evidence practices](./references/design-patterns.md)
   when reducing measured work, extending useful operation or comparing lifecycle boundaries.
   If a local saving shifts work to another device/location/time, then retain
   that displacement and boundary difference instead of claiming a whole-system benefit.
   If a proposed replacement changes lifecycle burdens outside available evidence,
   then report the tradeoff as unknown rather than declaring a net environmental improvement.

4. Verify: Compare the selected objective against equivalent useful output and
   conditions, retaining measured/proxy distinctions, scope and lifecycle exclusions.
   If only a resource counter or assumed conversion is available, then report
   that proxy and missing evidence instead of inventing measured energy or emissions.

5. Report: Return objective-specific results, source/provenance, useful-output
   checks, allocation, displaced effects, horizon and unresolved lifecycle costs.
   If only operational energy was assessed, then limit the conclusion to that
   boundary; no total environmental or long-term stewardship verdict follows automatically.

## Specification patterns

- **Operational objective:** For `{functional_output_and_quality}` over `{horizon}`,
  meet `{confirmed_stewardship_metric_and_target}` within `{system_boundary}`,
  verified by `{measured_or_explicit_proxy_evidence_and_allocation}`.
- **Device-life decision:** Preserve `{required_useful_service}` through
  `{confirmed_service_life_condition}` under `{maintenance_and_resource_constraints}`,
  comparing `{supported_lifecycle_effects}` with `{explicit_unknowns_and_exclusions}`.

Use the illustrative energy trial only when energy is the chosen objective;
confirm with the user/stakeholder. Ask the user for supported impact factors before making any conversion claim.

## Rules of thumb

- Don't equate lower CPU, a smaller bill or newer hardware with environmental
  improvement; each can change without establishing the chosen stewardship objective.
- Do keep useful output and quality fixed in the comparison; stopping required
  service can reduce measured energy while defeating the agreed functional unit.
- Do include idle/shared-device allocation and displaced work within the declared
  boundary; moving consumption outside a narrow counter is not a whole-system saving.
- Don't convert energy to emissions using an invented factor; source, location,
  period and boundary limits must support that distinct claim or remain unknown.
- Do separate operational savings from acquisition/replacement/retirement effects;
  a lower running measurement cannot settle an unmeasured lifecycle tradeoff.
- Do test service adequacy when extending device life; retaining unusable equipment
  does not meet a stewardship objective defined around continued useful service.

## Verification

Use metered-resource comparison, lifecycle-boundary review and useful-service
validation categories. Retain objective, units, source/provenance, measured/proxy
status, scope, horizon, allocation, useful results and excluded effects. Inspect
service-life conditions and displacement. Report unsupported factors or lifecycle
stages explicitly; an operational ratio or purchasing label alone establishes no total impact result.

## Done checklist

- [ ] Confirm the stewardship objective rather than assuming energy, money or carbon.
- [ ] Define equivalent useful output, quality, service constraints and horizon.
- [ ] Record system/lifecycle boundary, allocation and displaced work.
- [ ] Distinguish measured evidence, proxies, supplied factors and unknown effects.
- [ ] Verify the selected objective and preserved useful-service conditions.
- [ ] Inspect device-life/replacement tradeoffs and lifecycle exclusions separately.
- [ ] Limit conclusions to supported units, scope and provenance without invented conversions.

## Failure modes

- Calling a CPU or cost reduction measured environmental improvement.
- Reducing consumption by abandoning required output or quality.
- Hiding idle allocation or shifted work outside the compared boundary.
- Inventing an emissions factor or total-lifecycle score from incomplete data.
- Keeping devices longer without checking continued useful service.

## References

- Read [stewardship-evidence practices](./references/design-patterns.md) when choosing
  boundaries, evidence, functional units or operational-versus-lifecycle comparisons.
- Read [report-energy example](./references/worked-example.md) when a measured
  operational improvement still leaves replacement and total impact unresolved.
