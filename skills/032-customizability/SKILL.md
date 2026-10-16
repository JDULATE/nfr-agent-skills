---
name: customizability
description: >-
  Supports user-authored behavior or presentation when tickets say "let users write report templates", "customers need their own rules", or "allow custom output layouts". Not for built-in choices (see configurability), fitting a work context (see tailorability), or plugin admission (see extensibility).
---
# Customizability

## Definition and scope

Customizability means stakeholders can introduce their own behavior or presentation
beyond selecting built-in choices. Define the authored artifact, available inputs,
execution boundary, and accepted result; separate settings (`configurability`),
contextual fitting (`tailorability`), and existing-hook admission (`extensibility`).

## Use when / Don't use when

- Apply when a stakeholder must author a template, rule, or other bounded artifact
  whose result is not a fixed built-in preset.
- Route choosing a supplied preset to `configurability` or contextual fitting to
  `tailorability`; a renamed built-in result is not stakeholder-defined behavior.
- Route a missing core seam to `extendability`; the authoring capability may need
  that foundation before its user-defined behavior can be accepted.

## Workflow

1. Clarify: Inspect customization loaders, rendering/rule code, input contracts,
   authoring docs, existing hooks, and examples before proposing user-defined behavior.
   If the request only selects predefined results, then Ask the user whether
   `configurability` or `tailorability` is the actual acceptance question.

2. Specify: Name the author, artifact form, exposed data, permitted operations,
   result oracle, storage/revision selection, invalid-artifact behavior, and host limits.
   If the request is practical customization, then propose this authoring record:

   ```text
   Illustrative authoring defaults; confirm with the user/stakeholder:
   Scope: 1 user-defined artifact demonstrating a result absent from built-in presets.
   Form: inspected supported artifact grammar; absent grammar stays a design decision.
   Inputs/authority: explicitly approved public fields and operations, not private state.
   Selection: recorded artifact revision invoked through the normal feature path.
   Acceptance: concrete authored input and expected result plus an invalid artifact case.
   Limits: host changes disclosed separately; no claim of arbitrary code execution support.
   Owner/open: feature owner; authoring rights, grammar, data scope, revision behavior.
   ```

   Ask up to three questions: who authors what new result; which inputs/operations
   are allowed; and which artifact lifecycle or invalid-result behavior is accepted.
   Proceed to an authoring-boundary design without assuming a plugin contract exists.
   If no scope is supplied, then propose the illustrative artifact above and confirm
   with the user/stakeholder before adopting its form or coverage.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [authoring patterns](./references/design-patterns.md) when
   separating authored artifacts from built-ins and defining revision/validation behavior.
   If the required data is not in the public authoring contract, then obtain a
   contract decision rather than reaching into private host state for this customer.
   If authors need a newly built hook, then expose that core work separately;
   do not claim a hardcoded customer branch proves stakeholder authoring works.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Supply an independently edited artifact through the normal selection
   path; compare its result with the authored expectation and rejected-artifact cases.
   If only a developer-modified built-in produces the result, then leave the
   stakeholder customization claim unverified until the authoring path is exercised.

5. Report: Return the artifact/revision, invoked inputs, produced result, enforced
   boundary, host changes, and unsupported authoring operations.
   If the example uses invented grammar, then label it hypothetical and avoid
   asserting compatibility with an actual template or rule engine.

## Specification patterns

- **Authorship:** `{stakeholder}` shall provide `{authored_artifact}` through
  `{authoring_and_selection_boundary}` to produce `{accepted_custom_result}` from
  `{declared_inputs}`, verified by `{independent_edit_and_normal_invocation}`.
- **Boundary:** For `{invalid_or_unsupported_artifact}`, `{host}` shall perform
  `{confirmed_failure_behavior}` without `{unapproved_operations}`, evidenced by
  `{negative_authoring_fixture}` under `{recorded_artifact_revision}`.
- **Revision:** Invoking `{artifact_identity}` shall use `{agreed_revision_rule}`
  for `{work_scope}`, checked by `{save_select_and_invoke_trace}`.

The illustrative artifact count is a starting scope, not arbitrary customization;
confirm with the user/stakeholder. Ask the user for missing grammar or authority decisions.

## Rules of thumb

- Do prove a result derives from stakeholder-authored content; adding a developer
  preset with a customer label cannot establish user-defined behavior.
- Do supply author-visible inputs explicitly; a custom result requiring private
  host fields demonstrates a missing authoring capability, not a successful customization.
- Do separate host admission changes from the authored artifact; a per-customer
  source fork can conceal that stakeholders still cannot introduce their own behavior.
- Do trace save, selection, and invocation to the same artifact revision; previewing
  an edited draft while normal execution uses a built-in leaves the customization unproved.
- Don't silently drop unsupported authored expressions to obtain a plausible result;
  a partly ignored artifact cannot be accepted as the stakeholder's intended behavior.

## Verification

Use authoring-contract tests, independent-artifact fixtures, and normal-path result
comparison. Exercise a new authored result, unsupported input/operation, invalid
artifact, and revision change. Inspect fallback-to-built-in events and saved-but-unused
artifacts. Successful editor preview alone is not proof of normal feature customization.

## Done checklist

- [ ] Produce a non-preset result from independently authored content.
- [ ] Invoke the saved artifact through normal feature selection, not preview alone.
- [ ] Match selected revision, exposed input, and expected custom result.
- [ ] Reject an unsupported expression or operation under the accepted policy.
- [ ] Exercise invalid syntax without silently substituting a built-in result.
- [ ] Compare host/core changes with the claimed author-owned addition surface.

## Failure modes

- Relabeling built-in presets and calling that stakeholder authorship.
- Passing preview while normal invocations still choose the old artifact.
- Reading private host fields that ordinary authors cannot access.
- Ignoring part of an artifact and accepting the remaining plausible output.

## References

- Read [authoring patterns](./references/design-patterns.md) when defining artifact
  inputs, revision selection, validation, and the host/custom boundary.
- Read [layout example](./references/worked-example.md) when testing a concrete
  authored result without implying support for an unverified template engine.
