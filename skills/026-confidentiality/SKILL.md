---
name: confidentiality
description: >-
  Restricts disclosure to authorized recipients when tickets say "the API leaks internal notes", "a cache shows another team's data", or "errors expose private fields". Not for purpose and retention (see privacy), identity linkage (see anonymity), or alteration protection (see integrity).
---
# Confidentiality

## Definition and scope

Confidentiality means protected information is disclosed only to recipients
permitted by the agreed policy. Follow information through every in-scope output;
distinguish permitted handling purpose/lifecycle (`privacy`), identity unlinkability
(`anonymity`), alteration control (`integrity`), and action authorization (`accessibility-access-control`).

## Use when / Don't use when

- Apply to private-field leaks, cross-scope responses, exports, shared caches,
  logs/errors, previews, or other paths through which a recipient may learn protected data.
- Route broader personal-data collection and retention decisions to `privacy`.
- Route non-reading action permission policy to `accessibility-access-control`;
  authorizing an operation does not automatically permit every response field.

## Workflow

1. Clarify: Read query/serializer code, field policies, caches, exports, error/log
   paths, and recipient docs before specifying a disclosure boundary.
   If recipient or field classification is unclear, then Ask the user rather
   than deriving permission from an existing payload or a successful login.

2. Specify: Record information classes, recipients/roles, object scope, permitted
   field views, channels/copies, policy transitions, and allowed/forbidden evidence.
   If the user wants a leak fix, then propose this disclosure record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Boundary: named protected fields and actual recipient/object scope under existing policy.
   Channels: normal responses, exports, previews, errors, logs, caches, and background delivery.
   Trial gate: 0 protected-field disclosures to forbidden recipients in the agreed scenarios.
   Allowed controls: confirm permitted recipients still receive their approved field subset.
   State changes: account for scope/permission changes and cached or delayed output.
   Observation: recipient-visible payload/content, not only the source query or UI mask.
   Evidence: synthetic markers, emitted/received views, cache keys/state, and policy decision.
   Status: proposed scoped boundary; no purpose approval, anonymity, or compliance inferred.
   ```

   Ask at most three groups about protected fields/recipients; copies, object
   scope and policy changes; and utility, evidence or proposed acceptance cases.
   Continue to a payload/cache/path design without silently choosing unknown field policy.
   If no criterion exists, then offer the illustrative disclosure gate and confirm
   with the user/stakeholder before accepting its recipient/channel scope.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [disclosure-boundary practices](./references/design-patterns.md)
   when narrowing views, isolating cache entries, or filtering alternate output.
   If a recipient needs only a subset, then construct its approved view before
   emission; masking the display cannot retract fields already sent to that recipient.
   If cache reuse crosses permitted scopes, then align reuse with the disclosure
   policy or avoid that reuse; a correct origin check does not protect an unsafe cached view.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Send synthetic protected markers through allowed and forbidden paths,
   inspect actual recipients, and exercise changed permissions and delayed copies.
   If a forbidden marker reaches any in-scope recipient-visible path, then retain
   the disclosure counterexample even when the normal page no longer displays it.

5. Report: Return the field/recipient matrix, changed output paths, allowed-control
   results, forbidden disclosure checks, and unobserved destinations/copies.
   If a third-party or log destination cannot be inspected, then limit the claim
   to verified channels rather than asserting no information escaped anywhere.

## Specification patterns

- **Recipient view:** For `{information_and_object_scope}`, emit only
  `{approved_fields}` to `{permitted_recipients}` through `{channels}`, verified
  by `{recipient_view_and_negative_marker_checks}` under `{policy_states}`.
- **Cached/delayed copy:** After `{permission_or_scope_change}`, prevent
  `{forbidden_disclosure}` from `{cached_queued_export_or_log_paths}`, verified
  by `{cross_scope_and_transition_retrieval_checks}` under `{confirmed_copy_policy}`.

Use the illustrative forbidden-disclosure gate if no target exists; confirm with
the user/stakeholder. Ask the user which channels and recipients belong in the claim.

## Rules of thumb

- Don't send a protected field and rely on display masking; the recipient may
  already learn it from the emitted payload before the page chooses to hide it.
- Do apply the field/recipient boundary to error and diagnostic output too;
  fixing the success response does not close a disclosure through its failure path.
- Do scope cached views by their actual permitted recipients and object context;
  a cache hit must not bypass the origin path's narrower disclosure decision.
- Don't require identity unlinkability to accept an approved identifiable view;
  a permitted recipient may learn a name while the separate anonymity claim remains false.
- Do separate a permitted field view from permission to collect or retain its data;
  the disclosure gate can pass while purpose and lifecycle approval remain unresolved.
- Do inspect delayed/export copies after policy changes; a narrowed live response
  cannot establish that an older queued or stored view respects the new boundary.

## Verification

Use recipient-payload capture, negative marker tests, cache isolation review,
and alternate-path integration categories. Vary recipient, object/team scope,
field class, normal/error route, and policy state. Inspect source emission and
received content, including logs, exports, previews, and delayed work. Keep allowed
views functional and mark unobservable destinations; a hidden UI field is not a negative disclosure test.

## Done checklist

- [ ] Resolve protected fields, permitted recipients, object scopes, and policy states.
- [ ] Map normal and alternate output paths, including caches and delayed copies.
- [ ] Inspect emitted and received forbidden-marker absence at the actual recipient boundary.
- [ ] Verify positive-control recipients receive only their useful approved subset.
- [ ] Exercise cross-scope cache reuse and normal/error output differences.
- [ ] Inspect permission changes against stored, queued, and export views.
- [ ] Limit disclosure claims to observed channels and record unverified destinations.

## Failure modes

- Hiding a field in the interface while returning it in the response.
- Correcting origin authorization but sharing its cached view across forbidden scopes.
- Redacting success output while errors or logs emit the same protected value.
- Equating login or encrypted transport with recipient permission for all fields.
- Stopping all output and calling the required approved view preserved.

## References

- Read [disclosure-boundary practices](./references/design-patterns.md) when choosing
  serializers, cache reuse, error filtering, or delayed-copy handling.
- Read [cross-team export example](./references/worked-example.md) when an allowed
  operation still exposes fields through a response, cache, or error to the wrong recipient.
