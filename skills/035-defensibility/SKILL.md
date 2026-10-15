---
name: defensibility
description: >-
  Enables authorized operators to detect, contain, and contest active adversarial actions when users say "stop this compromised credential from continuing", "give responders a usable containment path", or "verify that incident controls actually cut off the attacker". Connects observed activity, scoped response authority, control effects, and preserved evidence. Not for design-time threat coordination alone (see security-control-and-security), normal outage restoration (see recoverability), or passive diagnosis alone (see observability).
---
# Defensibility

## Definition and scope

Defensibility means authorized operators can detect, contain and contest an active
adversarial action using available controls. Connect observations to scoped response
and verified effects; distinguish design-time threats (`security-control-and-security`),
passive state inference (`observability`) and normal restoration (`recoverability`).

## Use when / Don't use when

- Apply when responders lack usable controls, authority or evidence to interrupt
  an ongoing adversarial path and check whether it can continue.
- Route a planned feature threat model to `security-control-and-security`.
- Route an ordinary outage restore to `recoverability`; restored health does not
  establish that the adversarial capability has been removed.

## Workflow

1. Clarify: Read detection/control code, session/job lifecycles, response docs,
   operator permissions and observed activity before specifying containment.
   If actor, affected scope or response authority is uncertain, then Ask the user
   and distinguish a response design/rehearsal from an authorized operational action.

2. Specify: Bind adversarial activity, detection signal, response owner, permitted
   actions, affected capabilities, collateral constraints, evidence and reversal conditions.
   If the request is response tooling, then propose this control record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scope: stated adversarial capability, affected identities/resources and authorized controls.
   Observation: source signal correlated to the modeled activity; uncertainty retained.
   Trial: interrupt the scoped capability within 2 minutes of confirmed operator activation.
   Effects: inspect active sessions, queued/background work and alternate paths actually covered.
   Preservation: permitted unrelated work and necessary evidence remain within their constraints.
   Reversal: explicit owner and conditions; restored health alone does not clear containment.
   Status: isolated rehearsal proposal, not authorization to disrupt live systems.
   ```

   Ask at most three groups about activity and scope; response authority/actions
   and collateral limits; and activation, evidence, reversal or acceptance criteria.
   Continue to a scoped control/runbook design using the existing granted authority.
   If no target exists, then offer the illustrative containment trial and confirm
   with the user/stakeholder before adopting its timing or capability scope.

3. Design/Implement: Read [response-control practices](./references/design-patterns.md)
   when connecting signals, operator controls and effect verification.
   If revoking a credential leaves existing sessions or jobs active, then map
   those capabilities separately rather than calling the whole action path contained.
   If a response destroys necessary evidence or blocks unrelated essential work,
   then expose the conflict and design the permitted scoped alternative.

4. Verify: Rehearse detection, activation, scoped effect and attempted continuation
   with synthetic activity; retain valid-work controls and unresolved capabilities.
   If the control reports success but the adversarial effect continues, then
   classify containment as failed rather than accepting the control API receipt.

5. Report: Return signal/action/effect timelines, authorized scope, capabilities
   interrupted, remaining paths, collateral effects and reversal decisions.
   If only an alert was observed, then report detection without claiming containment;
   if work was merely restarted, distinguish restoration from removing adversarial access.

## Specification patterns

- **Containment:** After `{confirmed_activation_anchor}`, `{authorized_operator}`
  shall interrupt `{adversarial_capability}` within `{confirmed_interval}` using
  `{permitted_control}`, verified by `{continued_effect_and_valid_work_checks}`.
- **Contest and reversal:** During `{active_scenario}`, retain `{decision_and_effect_evidence}`,
  enforce `{scoped_response_constraints}`, and restore authority only under
  `{confirmed_clearance_rule}`, verified by `{remaining_path_and_reversal_trace}`.

Use the illustrative activation-to-containment trial when no deadline exists;
confirm with the user/stakeholder. Ask the user which capabilities and collateral effects are in scope.

## Rules of thumb

- Don't equate an alert with containment; inspect whether the adversary can still
  produce the protected effect after the response control reports completion.
- Do distinguish credential revocation, session interruption and queued-work
  cancellation; removing one capability does not establish that the others stopped.
- Do scope the response to the confirmed adversarial path and granted authority;
  stopping unrelated essential work can exceed the permitted containment contract.
- Do retain the activity and response evidence needed to evaluate the intervention;
  destroying it during cleanup can prevent checking what capability actually persisted.
- Don't release containment because a health probe is green; restored service
  does not show that the adversarial identity, session or alternate path is gone.
- Do verify reversal against its clearance conditions; reopening the capability
  before those conditions hold can undo the very containment being accepted.

## Verification

Use isolated adversarial-activity rehearsal, operator-control integration and
capability/effect inspection categories. Correlate signal, activation, control
receipt, actual effect and attempted continuation. Inspect sessions/jobs and
alternate paths within scope, valid-work impact, evidence preservation and reversal.
Record untested capabilities; a successful button click proves neither containment nor incident resolution.

## Done checklist

- [ ] Bound observed activity, affected capabilities and granted response authority.
- [ ] Correlate detection evidence to the modeled adversarial path.
- [ ] Rehearse activation and observe when the actual capability is interrupted.
- [ ] Inspect sessions, queues and alternate continuation paths in the claim.
- [ ] Check permitted unrelated work and necessary evidence survive the response.
- [ ] Distinguish detection, control receipt, containment and restored health.
- [ ] Verify clearance/reversal conditions and record residual capabilities.

## Failure modes

- Reporting an alert or successful control receipt as a contained adversary.
- Revoking a credential while existing sessions or queued jobs still act.
- Disrupting unrelated essential work outside the approved response scope.
- Destroying evidence before checking the continued-effect path.
- Reopening access because normal service returned without checking clearance.

## References

- Read [response-control practices](./references/design-patterns.md) when choosing
  a scoped intervention, capability checks or evidence-preserving reversal.
- Read [credential-containment example](./references/worked-example.md) when revoked
  login authority and already accepted background work need separate observations.
