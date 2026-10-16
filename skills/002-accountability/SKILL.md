---
name: accountability
description: >-
  Attributes actions when asked "retain the approving user", "tag delegated work", or "link actions to logins". Before routing an investigation, Ask the user: actor identity, audit evidence, or artifact history? Not for evidence sufficiency (see auditability), artifact links (see traceability), or hiding identity (see anonymity).
---
# Accountability

## Definition and scope

Accountability means system actions can be attributed to an appropriate actor
under the agreed identity model. Distinguish the initiating principal, delegated
executor, and observed outcome; separate independent examination (`auditability`),
artifact relationships (`traceability`), and identity hiding (`anonymity`).

## Use when / Don't use when

- Apply when shared identities, background jobs, delegation, or missing actor
  context prevent attributing a consequential action to its supported principal.
- Route evidence retrieval for an examiner's question to `auditability`.
- Route a requirement-to-test history to `traceability`; a linked commit does not
  by itself establish who initiated a runtime action.

## Workflow

1. Clarify: Read identity and action code, delegation/job paths, identity-provider
   docs, and event records before specifying attribution.
   If credentials are shared or the identity source cannot identify a person,
   then Ask the user what principal can honestly be attributed instead of inventing a human actor.

2. Specify: Bind action, initiating/executing principals, trusted identity source,
   delegation, resource, time/order, result, evidence boundary, and ambiguity policy.
   If the user wants an attribution fix, then propose this record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Unit: named consequential action with operation identity and observed outcome.
   Actors: trusted initiating principal and executor; preserve delegation separately.
   Trial gate: 0 falsely attributed actions in the agreed direct/delegated/unknown cases.
   Evidence: trusted identity assertion, action/resource, attempt/result, and correlation.
   Unknowns: distinguish shared principal, missing origin, and failed identity propagation.
   Data: retain only approved identity/evidence fields; never copy bearer secrets into records.
   Status: proposed attribution scope, not proof of the human behind a credential.
   ```

   Ask at most three groups about actions/identity model; delegation and ambiguity;
   and evidence access, lifetime or acceptance cases. Continue to a scoped event design.
   If no criterion exists, then offer the illustrative false-attribution gate and
   confirm with the user/stakeholder before adopting its identity/scenario limits.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [attribution practices](./references/design-patterns.md)
   when binding identity at entry, propagating delegation, or recording outcomes.
   If a job changes executor, then carry the validated origin and delegation
   separately; do not replace responsibility with the last service account name.
   If a caller supplies an actor label, then distinguish it from trusted identity
   before recording it as attribution evidence.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Exercise direct, delegated, shared, unknown-origin, and failed-action
   traces; compare identity assertions with actual action/effect records.
   If origin is lost, then retain unknown attribution and the broken boundary
   rather than backfilling a plausible user from timing or a nearby request.

5. Report: Return the identity/action model, propagated fields, tested attribution,
   unknown/shared cases, and limits of what the source can establish.
   If evidence identifies only a credential or service, then state that scope;
   do not turn the record into proof of human intent or legal responsibility.

## Specification patterns

- **Action attribution:** For `{action_and_resource}`, record `{trusted_initiator}`,
  `{executor_and_delegation}`, and `{observed_outcome}` under `{identity_model}`,
  verified by `{direct_delegated_and_unknown_origin_cases}`.
- **Attribution limits:** When `{identity_evidence_is_shared_or_missing}`, retain
  `{honest_principal_or_unknown_status}` without `{unsupported_human_assignment}`,
  verified by `{identity_boundary_and_result_comparison}`.

Use the illustrative attribution gate when no measure exists; confirm with the
user/stakeholder. Ask the user which identity claims the available source can support.

## Rules of thumb

- Do retain initiating principal and executor separately across delegation;
  a service account completing the work does not identify who requested it.
- Don't turn a caller-supplied actor string into trusted attribution; bind the
  recorded principal to the actual validated identity context at the action boundary.
- Do preserve unknown or shared identity honestly; choosing a likely human can
  produce a more readable record while falsely assigning responsibility.
- Do separate attempted, authorized, and completed actions; an identity on the
  request does not establish that the actor caused the final business effect.
- Don't retain bearer credentials merely to identify the actor later; use the
  approved non-secret identity/evidence reference and its access/lifetime policy.

## Verification

Use identity-boundary review, delegated-action integration, and action/result
correlation categories. Compare origin, executor, delegation, resource, operation
identity and outcome across queues and retries. Inject missing/untrusted actor
context and retain unknowns. Inspect attribution evidence for unnecessary secrets;
a successful login or a timestamp-nearby request alone is not runtime responsibility evidence.

## Done checklist

- [ ] Define attributable principal and limits of person/service identity evidence.
- [ ] Bind action records to trusted identity rather than caller labels.
- [ ] Preserve origin, executor and delegation across job handoffs.
- [ ] Distinguish attempts, authorization and observed effects in attribution records.
- [ ] Exercise shared, missing and forged-origin cases without false human assignment.
- [ ] Inspect retained identity fields, secret exclusion and evidence access/lifetime.
- [ ] Report broken identity propagation and unsupported responsibility claims.

## Failure modes

- Recording only the final service identity for a delegated user action.
- Trusting an actor name supplied in request content.
- Guessing a person when the supported identity is shared or unknown.
- Treating an attempted action record as proof of a completed business effect.
- Storing live credentials to make identity records seem more convincing.

## References

- Read [attribution practices](./references/design-patterns.md) when choosing trusted
  identity bindings, delegation fields or honest unknown-actor handling.
- Read [delegated-approval example](./references/worked-example.md) when the initiator
  and worker differ and a failed attempt must not become a completed approval.
