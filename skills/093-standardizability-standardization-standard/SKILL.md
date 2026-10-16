---
name: standardizability-standardization-standard
description: >-
  Selects conventions when asked "adopt an event format", "publish naming rules", or "agree on field names". Before routing standardization, Ask the user: choose a rule, enforce an existing rule, or align peers? Not for checking already selected rules (see conformance).
---

# Standardizability/Standardization/Standard

## Definition and scope

Use this skill to select and adopt an agreed common convention for repository
artifacts or interfaces. Treat that meaning as a proposed repository convention,
not a claim that the catalogue's slash terms have a universal definition.
Separate adopting a convention from checking an already chosen rule
(`conformance`) and making peers look alike (`uniformity`).

## Use when / Don't use when

- Apply when teams need a shared event format or naming convention and must
  resolve competing local choices before adoption can proceed.
- State which artifacts adopt the convention, which semantics it expresses,
  and how legacy exceptions are handled.
- Route checking a supplied rule set to `conformance`.
- Route purely cosmetic consistency across peers to `uniformity`; agreeing on
  field names does not by itself establish exchange meaning.

## Workflow

1. Clarify: Read competing schemas, event producers, consumers, naming guidance,
   mappings, and ownership docs before specifying a common convention.
   Identify why the differences matter and which consumers rely on them.
   If a convention has already been selected and only checking remains, then
   route that acceptance question to `conformance`.

2. Specify: Record candidate conventions, required meanings, selection authority,
   adopted scope, exception ownership, and the migration boundary.
   If no adoption target exists, then propose a labeled illustrative default:
   a reviewed local event vocabulary for the named producers with explicit
   legacy mappings and exceptions; confirm with the user/stakeholder.
   Ask at most three questions on shared meaning, decision authority, and adoption
   scope; keep an unapproved proposal distinct from a binding convention.

3. Design/Implement: Read [adoption decisions](./references/design-guide.md)
   when choosing a canonical vocabulary, mapping boundary, or exception register.
   If candidate fields have different meanings, then resolve those meanings
   before choosing a common name.
   If changing legacy output would break a consumer, then place a declared
   translation at its boundary or keep a scoped exception pending migration.

4. Verify: Trace representative producer outputs into the adopted vocabulary,
   compare required meanings, and inspect named legacy mappings and exceptions.
   If only a style document changed, then report a proposed convention rather
   than completed adoption by the affected producers.

5. Report: Deliver the selected convention, decision rationale, owner, adoption
   evidence, legacy treatment, and unresolved scope.
   If no stakeholder has approved the choice, then label it proposed; do not
   describe a repository-local decision as an external standard or certification.

## Specification patterns

- **Selection:** For `{artifact_scope}`, `{decision_owner}` shall select
  `{common_convention}` against `{required_meanings_and_constraints}`, producing
  `{approved_definition_and_candidate_rationale}`.
- **Adoption:** `{named_producers}` shall emit `{selected_fields_and_meanings}`
  through `{adoption_boundary}`, preserving `{legacy_obligations}` through
  `{explicit_mappings_or_exceptions}`, verified by `{before_after_fixtures}`.

Use the illustrative scoped-adoption default in Specify when goals lack numbers;
confirm with the user/stakeholder instead of inventing a universal adoption rate.

## Rules of thumb

- Resolve semantic conflicts before declaring field names canonical; choosing
  a spelling cannot reconcile candidates that encode different concepts.
- Give a selected convention an adoption scope and decision owner; a shared-looking
  schema copied between teams is not evidence of an agreed common contract.
- Keep legacy mappings and exceptions attached to the adopted convention;
  silently leaving producers on different meanings defeats the adoption claim.
- Separate selection rationale from rule-check results; a passing checker cannot
  establish why this convention, rather than another, should be adopted.

## Verification

Use candidate-schema comparison, producer fixture inspection, mapping tests,
and adoption-scope review.
Check that the selected fields express the required meanings without collisions.
Inspect actual emitted artifacts, not just documentation or type declarations.
Exercise a legacy consumer through its declared mapping.
Record unresolved producers and rejected candidates with reasons.
Use rule-checking tools only against the selected local convention; a validator
pass supplies evidence of implementation, not stakeholder agreement.
Do not cite an external standard unless its allowed source and applicability
have been confirmed under the repository allowlist.

## Done checklist

- [ ] Inventory the competing conventions and affected consumers.
- [ ] Record the shared meanings the selected vocabulary must express.
- [ ] Attribute the selection decision and its approval state.
- [ ] Inspect adopted output from each named in-scope producer.
- [ ] Check legacy mapping without changing the old consumer's obligation.
- [ ] Identify exceptions with owners and migration conditions.
- [ ] Distinguish proposed adoption from implemented and approved adoption.

## Failure modes

- Renaming unlike concepts identically and calling the result standardized.
- Treating an unapproved document as an adopted common convention.
- Declaring all producers migrated while a legacy producer is silently exempt.
- Reporting conformance results as proof that the selection decision was correct.

## References

- Read [adoption decisions](./references/design-guide.md) when resolving competing
  vocabularies and choosing an adoption boundary.
- Read [event convention example](./references/worked-example.md) when recording
  a local naming decision, producer change, and legacy-consumer mapping.
