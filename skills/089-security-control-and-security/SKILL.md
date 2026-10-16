---
name: security-control-and-security
description: >-
  Designs controls against adversary paths when tickets say "how could an attacker abuse this feature", "where should we block this attack", or "the normal route is fixed but retries bypass it". Not for disclosure alone (see confidentiality), alteration alone (see integrity), or incident containment (see defensibility).
---
# Security/Control and Security

## Definition and scope

Security/control and security means addressing explicit adversaries, protected
assets, and controls against misuse. Coordinate trust boundaries and causal attack
paths; distinguish isolated disclosure (`confidentiality`), alteration (`integrity`),
personal-data lifecycle (`privacy`), and active defensive response (`defensibility`).

## Use when / Don't use when

- Apply when a feature/integration needs a threat model, controls against specified
  misuse, or a review of how attacker-controlled inputs can reach protected effects.
- Route a single disclosure or alteration property to `confidentiality` or `integrity`.
- Route an ongoing adversarial event needing operator containment to `defensibility`;
  writing a design model is not an incident response action.

## Workflow

1. Clarify: Read relevant code, entrypoints, identity/config paths, data-flow docs,
   dependency manifests, and prior security decisions before naming threats.
   If asset ownership, attacker capability, or review scope is unclear, then Ask
   the user; do not assume that every endpoint or external system is an authorized target.

2. Specify: Connect asset, adversary capability, entrypoint, trust crossing,
   misuse consequence, preventive/detective controls, evidence, and residual exposure.
   If the request is a practical security review, then offer this threat/control record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scope: requested repository feature and authorized synthetic/local validation paths.
   Adversary: stakeholder-confirmed capabilities, controlled inputs, and existing access.
   Path: entrypoint -> trust boundary -> asset-affecting operation -> misuse consequence.
   Trial gate: 0 successful modeled misuse paths in the agreed negative scenarios.
   Controls: exact enforcement/observation point, assumptions, bypasses, and normal-use constraints.
   Evidence: source trace, positive/negative effects, control failures, and coverage limits.
   Residual: unmodeled capabilities and unverified components remain explicit owner decisions.
   Status: proposed bounded threat review, not a guarantee that the system is secure.
   ```

   Ask at most three groups about assets/adversary and scope; misuse consequences
   and existing controls; and permitted validation, residual decisions, or criteria.
   Continue to repository analysis and isolated test design using confirmed scope.
   If no target exists, then offer the illustrative modeled-path gate and confirm
   with the user/stakeholder before treating it as acceptance or broadening validation.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [threat-path practices](./references/design-patterns.md)
   when selecting control placement, trust decisions, or evidence for a misuse path.
   If attacker-controlled data becomes a trusted identity, command, destination,
   or policy decision, then enforce the confirmed boundary before the protected effect.
   If a proposed control only logs misuse, then state its detection role and
   verify the prevention claim separately; an alert cannot undo an already completed effect.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Exercise modeled misuse and valid-use controls within the authorized
   test boundary; inspect actual asset effects and control behavior, not only tool labels.
   If a scanner or dependency report flags an item without a demonstrated relevant
   path, then retain it as evidence to investigate rather than inventing exploitability.

5. Report: Return the threat/control map, changed implementation/tests, observed
   effects, control assumptions, excluded paths, and residual decision owners.
   If only selected scenarios were examined, then limit the conclusion to them;
   no clean tool result establishes universal security or compliance.

## Specification patterns

- **Misuse control:** For `{asset}` against `{adversary_capabilities}`, constrain
  `{entrypoint_and_trust_crossing}` with `{confirmed_control}`, preventing
  `{misuse_effect}` as verified by `{negative_path_and_valid_use_effect_checks}`.
- **Detection boundary:** For `{modeled_event}`, expose `{required_evidence}` to
  `{authorized_responder}` under `{confirmed_detection_rule}`, verified by
  `{event_to_observation_trace}` while `{preventive_claims_and_residual_effects}` remain separate.

Use the illustrative modeled-misuse gate if no criterion is supplied; confirm
with the user/stakeholder. Ask the user for selected standards/source requirements;
record supplied policy labels without claiming external obligations from memory.

## Rules of thumb

- Do trace each proposed control to an adversary-controlled step and protected
  effect; a list of security features does not establish that the misuse path is interrupted.
- Don't promote caller-supplied identity, scope, destination, or policy labels into
  trusted authority without the confirmed boundary check; a plausible format is not that authority.
- Do inspect alternate entrypoints and control-failure behavior for the same asset;
  an attacker path left outside the control can defeat the modeled prevention claim.
- Don't report logging or alerting as prevention after the protected effect happened;
  separate evidence for detection from evidence that the adversary could not perform it.
- Do preserve legitimate-use controls alongside misuse scenarios; disabling the
  protected capability can stop the attack by abandoning the accepted product requirement.
- Don't turn an empty scan report into a secure-system verdict; validate the
  modeled asset/path claims and retain unsupported attacker capabilities as explicit limits.

## Verification

Use trust-boundary source review, isolated misuse-path integration, dependency
inventory analysis, and asset-effect inspection categories. Record attacker control,
preconditions, protected action, actual effect, control result, and valid-use outcome.
Inspect failure/bypass paths and distinguish tool findings, demonstrated relevant
paths, detected events, and prevented effects. No unexecuted test or unresolved finding is a pass.

## Done checklist

- [ ] Define assets, adversary capabilities, ownership, and authorized review/test scope.
- [ ] Trace modeled entrypoints and trust crossings to protected effects.
- [ ] Map each preventive/detective control to its actual decision or observation point.
- [ ] Exercise the agreed misuse paths and inspect actual asset effects.
- [ ] Check alternate entrypoints and control-failure outcomes for those claims.
- [ ] Verify legitimate-use controls preserve required behavior.
- [ ] Separate scanner findings, detection evidence, and prevention results.
- [ ] Assign owners to residual paths, unmodeled capabilities, and validation gaps.

## Failure modes

- Producing a control checklist with no adversary-to-asset path or evidence.
- Trusting a caller's identity/scope field because its syntax is valid.
- Closing a normal route while the same protected effect remains reachable elsewhere.
- Calling a recorded misuse event proof the effect was prevented.
- Disabling the feature or passing a scan and declaring broad security.

## References

- Read [threat-path practices](./references/design-patterns.md) when mapping adversary
  control, enforcing trust boundaries, or separating prevention from detection.
- Read [integration-destination example](./references/worked-example.md) when a
  caller-controlled destination reaches protected export effects through multiple paths.
