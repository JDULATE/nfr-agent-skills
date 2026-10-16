---
name: safety
description: >-
  Prevents named harm when tickets say "do not delete records that are on hold", "can stopping this action cause harm", or "the safety check is only in the UI". Not for adversary controls (see security-control-and-security), usable service time (see availability), or generic bad-input handling (see robustness).
---
# Safety

## Definition and scope

Safety means controlling identified paths to harm in the intended context.
Connect stakeholder-defined harmful outcomes to unsafe actions, conditions, and
constraints; distinguish adversarial misuse (`security-control-and-security`),
service readiness (`availability`), and controlled adverse behavior without a
harm claim (`robustness`).

## Use when / Don't use when

- Apply when a wrong, missing, late, or unintended action can cause a specified
  harmful consequence rather than merely a generic error or outage.
- Ask the user who or what can be harmed, which conditions make the action unsafe,
  and which domain policies or responsible reviewers govern the decision.
- Route adversary-centered control design to `security-control-and-security`;
  include that concern when misuse can also trigger the identified harm.

## Workflow

1. Clarify: Read action-producing code, control/config paths, system-context docs,
   incident scenarios, and existing hazard/constraint records before specifying.
   If the harmful outcome or operational boundary is missing, then Ask the user;
   do not invent a safe state, acceptable severity, or universal shutdown policy.

2. Specify: Record harm, hazard conditions, unsafe action/omission/timing, causal
   path, prevention/mitigation constraints, owner, evidence, and residual exposure.
   If the user requests a practical prevention change, then propose this hazard record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Harm/context: stakeholder-supplied loss and affected people/assets in the named use.
   Causal path: hazardous conditions -> unsafe command/omission/timing -> harmful outcome.
   Constraint: confirmed permitted action and required state evidence at its commitment point.
   Trial gate: 0 prohibited actions in the agreed hazardous-condition scenarios.
   Unknown state: explicit unresolved-action policy; neither stop nor continue is assumed safe.
   Controls: enforcement owner, alternate entrypoints, bypass conditions, and residual paths.
   Evidence: synthetic scenario trace, actual effect, control decision, and constraint mapping.
   Status: engineering proposal, not a certification or an accepted residual-risk decision.
   ```

   Ask at most three groups about harm/context and causal conditions; required
   safe behavior including uncertainty and omission; and controls, review authority,
   and permitted verification boundaries. Proceed to analysis and a reversible design.
   If no criterion exists, then offer the illustrative prohibited-action gate and
   confirm with the user/stakeholder before using its scenario scope for acceptance.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [harm-control practices](./references/design-patterns.md)
   when locating a decision gate, defining unknown-state behavior, or checking bypasses.
   If a constraint exists only in a user-interface prompt, then inspect other
   action paths and enforce the confirmed constraint at the actual effect boundary.
   If delaying or blocking the action could cause another harm, then expose that
   competing path and seek the responsible decision instead of choosing blanket refusal.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Exercise agreed synthetic hazard scenarios and boundary/timing paths
   in an authorized controlled environment; inspect actual effects, not only warnings.
   If a control prevents the named action but another entrypoint bypasses it,
   then leave that hazard path uncontrolled and retain the counterexample.

5. Report: Return the harm/constraint map, implemented gates, scenario results,
   bypasses, assumptions, competing harms, and residual-decision owners.
   If evidence covers only selected paths, then state those limits and leave
   broader safety and residual-risk acceptance to the responsible stakeholder.

## Specification patterns

- **Unsafe-action prevention:** Under `{hazardous_conditions}`, `{effect_boundary}`
  shall prevent `{prohibited_action}` and perform `{confirmed_alternative}`,
  verified by `{causal_scenario_and_actual_effect_checks}`.
- **Uncertainty/timing:** When `{required_state_evidence}` is `{missing_stale_or_changed}`,
  apply `{stakeholder_confirmed_action_policy}` before `{commitment_point}`,
  verified through `{unknown_delayed_and_racing_state_traces}` with `{residual_paths}` recorded.

Use the illustrative scenario gate if no criterion exists; confirm with the
user/stakeholder. Ask the user for domain constraints and acceptable residual exposure;
record supplied policy labels without asserting external obligations or certification.

## Rules of thumb

- Do judge the control against the harmful outcome's causal path, not an error
  count; a quiet system can still issue the action that makes the situation hazardous.
- Don't assume stopping is the safe response; an omitted or late action may be
  the path to harm, so the required uncertain-state behavior needs its own justification.
- Do enforce a confirmed hazard constraint at the point that commits the effect;
  a warning screen cannot protect the same action reached through another entrypoint.
- Do inspect whether required state evidence changes before commitment; a safe
  earlier decision cannot justify an unsafe action after its hazard conditions change.
- Don't accept failover or recovery as a harm-control substitute unless it breaks
  the identified causal path; restored service can still produce the harmful action.
- Do retain competing harmful consequences and control bypasses as unresolved
  paths; a favorable primary scenario does not authorize accepting their residual exposure.

## Verification

Use hazard-path review, constraint-to-code tracing, synthetic scenario tests,
and effect-boundary inspection categories. Exercise wrong, absent, stale, late,
and changed inputs where they affect the named hazard. Inspect alternate command
paths, bypass behavior, control failures, and actual final effects. Reconcile
prevention with required action/omission constraints; warnings alone are not prevention evidence.

## Done checklist

- [ ] Ground each harm and hazardous condition in stakeholder/context evidence.
- [ ] Trace unsafe action, omission, or timing to the harmful consequence.
- [ ] Map constraints to the actual effect boundary and enforcing owner.
- [ ] Record justified behavior when required state evidence is missing or stale.
- [ ] Exercise changed-state and timing paths before action commitment.
- [ ] Inspect alternate entrypoints and control-bypass outcomes.
- [ ] Observe actual prohibited/permitted effects, including control failure cases.
- [ ] Retain competing harms, untested paths, and residual-decision ownership.

## Failure modes

- Calling a low error rate evidence that a hazardous command cannot occur.
- Installing a warning while alternate action paths bypass the constraint.
- Treating every shutdown as safe without considering omission or timing harms.
- Reusing an earlier authorization after the hazardous state has changed.
- Claiming broad safety or certification from a few passing scenario tests.

## References

- Read [harm-control practices](./references/design-patterns.md) when defining
  unsafe actions, effect-boundary enforcement, or uncertain-state alternatives.
- Read [retained-record cleanup example](./references/worked-example.md) when a
  stakeholder-defined harmful loss needs causal controls and actual-effect evidence.
