---
name: adjustability
description: >-
  Designs bounded tuning of an existing operating parameter when users say
  "tune the batch size", "change the polling interval", or "adjust this
  operating threshold". Keeps the operating arrangement fixed and checks the
  applied value and its effects. Not for defining the menu of settings (see
  configurability) or moving to a different operating arrangement (see
  reconfigurability).
---
# Adjustability

## Definition and scope

Adjustability means tuning an existing operating parameter within the same
arrangement. Specify its effective value, application event, and resulting work;
distinguish the settings menu (`configurability`), a changed arrangement
(`reconfigurability`), and alternative task routes (`flexibility`).

## Use when / Don't use when

- Apply when an existing control needs a new value and evidence of when that
  value takes effect in the current operating arrangement.
- Route designing valid settings and combinations to `configurability`.
- Route changed pipeline topology or placement to `reconfigurability`, even
  when a numeric setting initiates that transition.

## Workflow

1. Clarify: Inspect operating code, the parameter reader, effective-value caches,
   configuration docs, and current work traces before specifying a tuning change.
   If the control changes the arrangement, then separate that transition under
   `reconfigurability` rather than treating it as a simple operating adjustment.

2. Specify: Record units, valid domain, requested/effective values, scope,
   application boundary, desired effect, resource trade-offs, and reversal.
   If the user wants an immediate adjustment, then offer this tuning card:

   ```text
   Illustrative tuning proposal; confirm with the user/stakeholder:
   Control: inspected existing batch cap, in records, within its supported domain.
   Example target: cap of 3 records only if valid for the current implementation.
   Application: next new batch; running work retains its recorded applied cap.
   Arrangement: unchanged workers, placement, and task route.
   Evidence: requested/effective values and emitted batch membership.
   Trade-off: measure resource effects separately; no assumed speed gain.
   Open/owner: valid range, application event, effect bound, existing operator.
   ```

   Ask up to three questions: which control and effect; where/when it applies;
   and which limits or running-work rules may change. Proceed to a tuning design
   using inspected semantics while unconfirmed values remain proposals.
   If a target is absent, then offer the illustrative cap only where relevant
   and confirm with the user/stakeholder before adopting it.

3. Design/Implement: Read [tuning patterns](./references/design-patterns.md) when
   tracing value precedence, work boundaries, or reversal.
   If a consumer caches the old value, then use the agreed refresh/application
   event and expose the applied revision instead of merely saving the setting.
   If the desired effect is unmeasured, then plan controlled trials before
   promising improvement or changing a production operating value.

4. Verify: Exercise valid, rejected, boundary, and reversed adjustments with
   the arrangement held fixed; match applied values to the affected work.
   If a saved value changes but emitted work does not, then trace the actual
   reader and application event before calling that control adjustable.

5. Report: Show requested/applied values, affected work, observed effects,
   invalid-input handling, reversal evidence, and held conditions.
   If workload or topology changed during comparison, then separate that delta
   instead of attributing its result to tuning this parameter.

## Specification patterns

- **Application:** Changing `{existing_parameter}` to `{confirmed_value_and_unit}`
  shall apply at `{work_boundary}` for `{scope}`, verified by
  `{effective_value_and_behavior_trace}` with `{arrangement}` unchanged.
- **Running work:** Work started before `{adjustment_event}` shall follow
  `{agreed_value_application_rule}`, checked by `{boundary_work_fixture}`.
- **Effect:** Under `{held_inputs}`, tuning `{parameter}` shall yield
  `{accepted_operating_effect}` within `{confirmed_bound}`, measured by
  `{controlled_trial}` with `{reversal_behavior}` verified separately.

The illustrative cap is a starting example, not a universal batch size;
confirm with the user/stakeholder. Ask the user for the applicable control and domain.

## Rules of thumb

- Do trace the applied value at the consuming loop; a writable settings record
  does not establish that the running operation can be tuned through it.
- Do bind each affected work unit to its applied value; mid-batch rereads can
  make a tuning result uninterpretable even though each read is individually valid.
- Do keep arrangement identity fixed in trials; adding workers with a cap change
  prevents attributing the observed effect to that cap.
- Do reconcile requested and applied units before comparing tuning trials; an
  implicit conversion can make a control-effect claim describe a different adjustment.
- Do reverse at the agreed application boundary; restoring a settings file
  does not show when newly admitted work returns to its former operating value.
- Don't declare a value better from its requested setting alone; correlate
  applied value with desired effect and expose compensating resource changes.

## Verification

Use controlled-parameter trials, effective-value inspection, and work-boundary
checks. Exercise invalid values, deferred application, scope overrides, and
reversal through the actual reader. Compare emitted work with its applied value
and revision. Inspect pending-versus-effective mismatches rather than taking a
stable settings display as evidence that consumers refreshed their values.

## Done checklist

- [ ] Trace an adjustment into the consumer's applied value and unit.
- [ ] Reject an out-of-domain value without silent substitution.
- [ ] Compare work begun before and after the application event.
- [ ] Check caches/overrides cannot target an unintended scope.
- [ ] Reproduce the desired effect with workload and arrangement held constant.
- [ ] Reverse the value and observe the next affected work unit.
- [ ] Compare resource effects against the accepted trade-off boundary.

## Failure modes

- Saving a setting that the operating consumer never rereads.
- Applying a value to part of a batch but attributing the whole batch to it.
- Calling a topology transition tuning because a numeric control triggers it.
- Claiming improvement that a changed workload actually explains.
- Restoring a file without verifying the old value becomes effective again.

## References

- Read [tuning patterns](./references/design-patterns.md) when tracing units,
  precedence, application boundaries, or adjustment reversal.
- Read [batch-control example](./references/worked-example.md) when distinguishing
  saved and applied values with concrete emitted membership.
