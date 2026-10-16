---
name: adjustability
description: >-
  Tunes existing controls when asked "lower this threshold", "change the polling interval", or "adjust batch size". Ask the user if tuning vs new options is unclear. Not for defining options (see configurability) or switching arrangements (see reconfigurability).
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
   If no runtime setting surface exists, then first read `configurability`'s
   `skills/027-configurability/references/design-patterns.md` from the repo root.
   Settle where the value lives and who may change it under `configurability`,
   then apply `adjustability` to when and how a new value affects work.
   If the control changes the arrangement, then separate that transition under
   `reconfigurability` rather than treating it as a simple operating adjustment.

2. Specify: Record units, valid domain, requested/effective values, scope,
   application boundary, desired effect, resource trade-offs, and reversal.
   If the user wants a practical change, then show one consolidated block to the
   user BEFORE any implementation, including code, configuration, or scaffolding.
   Label every decision as a proposal; fill it from the request and inspected code:

   ```text
   Labeled illustrative defaults; confirm with the user/stakeholder:
   Proposal - control/scope: the requested parameter; keep the arrangement unchanged.
   Proposal - valid domain: inspected legal values; otherwise unresolved, ask below.
   Proposal - units: the consumer's existing units; resolve with the domain if unknown.
   Proposal - default: retain the current constant until a valid change is supplied.
   Proposal - application: snapshot at the next agreed point of use/work-unit start.
   Proposal - running work: retain its captured value; settle any unstated semantics.
   Proposal - interface: reuse the existing invocation path or an in-process setter.
   Proposal - persistence: process memory, resetting to the default on restart,
     unless persistence is already requested or an existing source is retained.
   Proposal - who may change it: the existing authorized caller; add no new roles.
   Proposal - rollback: reapply the former valid value at the same boundary;
     completed effects and already captured work are not undone by a value reset.
   Proposal - evidence: consumer-applied value and affected work; revision only if needed.
   Proposal - trade-off: check resource effects separately; promise no speed gain.
   Proposal - offered extensions: authentication, persistence, a new server,
     or response headers require the user's yes before being added.
   ```

   Ask at most three questions, only for a valid domain (including unknown units)
   and running-work semantics that the user did not state and inspected code
   cannot establish. Do not invent these or implement while they are unresolved.
   Use labeled proposals for defaultable decisions instead of asking about each.
   Show the settled consolidated block before implementing the authorized minimum;
   do not turn the block into a blanket approval request for ordinary scoped work.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [tuning patterns](./references/design-patterns.md) when
   tracing value precedence, work boundaries, reversal, or exposing a hardcoded value.
   Build the smallest version: a setting read at the point of use, with the
   retained default, domain validation, and the agreed running-work boundary.
   Reuse existing access controls. Offer added authentication, persistence, a new
   server, or response headers as extensions; obtain the user's yes unless already
   explicitly authorized. Do not add a network endpoint to create a local setter.
   If a consumer caches the old value, then use its agreed refresh event and
   inspect the consumer's applied value, rather than only the saved request.
   If sequential application in one consumer is unambiguous, then an applied-value
   readback plus a behavior probe is enough; do not add revision machinery.
   If asynchronous consumers, overlapping updates, repeated values, or partial
   application require distinguishing which change reached which work, then bind
   an applied revision to each consumer/work snapshot. A requested revision alone
   is not applied evidence; use `reconfigurability` when ownership or arrangement moves.
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

Treat the consolidated defaults as proposals; confirm with the user/stakeholder.
Ask the user for any unresolved valid domain or running-work semantics.

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
reversal through the actual reader. Compare emitted work with its applied value;
include an applied revision only when change identity is needed. Inspect
pending-versus-effective mismatches rather than taking a
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
  precedence, application boundaries, reversal, or making a constant runtime-changeable.
- Read [batch-control example](./references/worked-example.md) when distinguishing
  saved and applied values with concrete emitted membership.
