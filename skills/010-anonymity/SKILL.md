---
name: anonymity
description: >-
  Tests identity linkage when asked "can this export identify people", "check linked fake IDs", or "compare repeated releases". Ask the user which observer and linkage are in scope. Not for data purpose/lifecycle (see privacy), recipient permissions (see confidentiality), or actor attribution (see accountability).
---
# Anonymity

## Definition and scope

Anonymity means a subject cannot be identified within the explicitly stated
observer and linkage model. Test what that observer can see and combine; distinguish
approved personal-data handling (`privacy`), recipient disclosure permission
(`confidentiality`), and attribution to an actor (`accountability`).

## Use when / Don't use when

- Apply when a release, event stream, feedback channel, or transformed dataset
  carries a claim that its subjects cannot be identified by specified observers.
- Route handling purpose, consent, retention, and deletion to `privacy`.
- Route who may read identifiable material to `confidentiality`; restricting
  access can support the model but does not itself make an authorized reader unable to identify.

## Workflow

1. Clarify: Read release/serializer code, join keys, mapping stores, capture paths,
   repeated-release docs, and recipient context before choosing transformations.
   If the observer's auxiliary knowledge or desired unlinkability is unknown,
   then Ask the user; do not turn missing names into an anonymity guarantee.

2. Specify: Record subjects, observer capabilities, available outputs/auxiliary data,
   identity/linkage goal, mappings, repeated releases, utility constraints, and test limits.
   If the user requests an anonymity improvement, then offer this model record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scope: named release and intended recipient observer, not every possible observer.
   Inputs: direct fields, stable tokens, context/timing, joins, mapping access, and prior releases.
   Goal: prevent the confirmed subject-identity or cross-context linkage in that model.
   Trial gate: 0 successful named-identity links in the agreed synthetic linkage fixtures.
   Utility: stakeholder-confirmed output use; removing all content is not assumed acceptable.
   Copies: recipient-visible errors, URLs, logs, exports, and follow-up releases in scope.
   Evidence: attempted joins/inferences, remaining clues, transformation, and model exclusions.
   Limits: a fixture result is not proof of universal anonymity or legal status.
   ```

   Ask at most three groups about observer/subjects and linkage goal; auxiliary
   data, copies and repeated releases; and utility, transformation or acceptance limits.
   Continue to a scoped release design while unknown observer capabilities remain explicit.
   If no target exists, then propose the illustrative linkage-fixture gate and
   confirm with the user/stakeholder before adopting its attack/model scope.

3. Design/Implement: Read [observer-and-linkage practices](./references/design-patterns.md)
   when choosing field removal, scoped identifiers, grouping, or release restrictions.
   If the observer can join a replacement token to identity, then break that
   path or withdraw the claim; a new token spelling does not remove a usable mapping.
   If context or repeated output reconstructs identity, then revise the release
   granularity or scope against utility instead of checking each field in isolation.

4. Verify: Attempt the stated joins and inferences using only the observer's
   declared view, including prior releases and alternate capture/error paths.
   If a test cannot model relevant auxiliary knowledge, then record that limit;
   failed fixture linkage does not establish immunity to unknown information.

5. Report: Return the observer model, changed outputs/mappings, concrete linkage
   attempts, retained utility, remaining clues, and unsupported identity claims.
   If the only evidence is name removal or a hidden mapping table, then report
   that transformation without declaring the released subjects anonymous.

## Specification patterns

- **Observer unlinkability:** For `{release_and_subjects}`, prevent
  `{identity_or_cross_context_link}` by `{observer_with_declared_capabilities}`
  using `{available_outputs_and_auxiliary_data}`, assessed by `{confirmed_linkage_checks_and_limits}`.
- **Repeated output:** Across `{release_sequence}`, limit `{joinable_clues}`
  while preserving `{agreed_utility}`, verified through `{combined_view_inference_attempts}`
  with `{unmodeled_knowledge_and_copies}` disclosed.

Use the illustrative synthetic-linkage gate when no criterion exists; confirm
with the user/stakeholder. Ask the user before selecting a quantitative anonymity model or legal classification.

## Rules of thumb

- Don't equate a replacement identifier with unlinkability; an observer holding
  its mapping can still identify the subject even if the released name is absent.
- Do combine the observer's permitted auxiliary fields and releases during review;
  individually ordinary clues can jointly answer the exact identity question being claimed hidden.
- Do distinguish identity recovery from merely linking records to each other;
  a stable unnamed profile can violate a cross-context unlinkability goal without a recovered name.
- Don't hide an identifying mapping from the reviewer while leaving it reachable
  by the claimed observer; the model must describe access, not the demo's chosen screen.
- Do compare transformed outputs against the confirmed utility task; an empty
  release avoids links by abandoning the function, not by satisfying a useful anonymity contract.
- Do retain inference and repeated-release gaps in the claim; a clean synthetic
  join test cannot establish unlinkability against unspecified future auxiliary knowledge.

## Verification

Use data-flow/linkage review, synthetic join/inference attempts, and combined-release
inspection categories. Capture the exact recipient view, stable/contextual fields,
mapping access, previous outputs, and identity/linkage outcome. Inspect non-tabular
copies and timing/context where in scope. Record utility losses and unmodeled
knowledge; token removal and failed isolated joins are supporting evidence only.

## Done checklist

- [ ] Define subject, observer, identity/linkage goal, and available auxiliary knowledge.
- [ ] Trace release fields, stable tokens, mappings, and recipient-visible copies.
- [ ] Attempt declared identity joins and distinguish cross-context linkage outcomes.
- [ ] Review combined and repeated releases rather than isolated fields alone.
- [ ] Check the transformed output still supports the confirmed utility task.
- [ ] Retain unresolved clues, unmodeled knowledge, and evidence scope in the claim.
- [ ] Separate transformation observations from universal anonymity or legal conclusions.

## Failure modes

- Removing names while leaving an observer-accessible identity mapping.
- Keeping a stable token and assuming unnamed records cannot be linked.
- Testing individual fields but ignoring combined context and repeated output.
- Claiming anonymity because the reviewer did not open an accessible mapping path.
- Reporting a useful release when the transformation removed the required function.
- Generalizing a failed synthetic linkage attempt to all observers and knowledge.

## References

- Read [observer-and-linkage practices](./references/design-patterns.md) when defining
  model capabilities, selecting a transformation, or reviewing combined releases.
- Read [feedback-release example](./references/worked-example.md) when a removed name
  leaves an identity join and a stable-profile linkage that need different decisions.
