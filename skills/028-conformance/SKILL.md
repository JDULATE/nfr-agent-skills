---
name: conformance
description: >-
  Checks chosen rules when asked "validate our schema", "reject invalid field names", or "show violated rules". Ask the user whether rules are already selected if unstated. Not for choosing a convention (see standardizability-standardization-standard).
---

# Conformance

## Definition and scope

Conformance means an artifact or behavior meets a rule set already selected for
its context. Identify the authoritative rules, their applicability, and the
evidence needed to check each one.
Separate checking selected rules from adopting a convention
(`standardizability-standardization-standard`) and general behavior against a
functional specification (`correctness`).

## Use when / Don't use when

- Apply when a schema, naming convention, or other supplied rule set needs an
  artifact-level pass/fail result with rule-specific findings.
- Require the actual rule text and selected revision; a familiar label alone
  does not establish obligations.
- Route choosing or negotiating the common convention to
  `standardizability-standardization-standard`.
- Route a functional branch result against its behavioral specification to
  `correctness`; keep overlapping acceptance questions explicit.

## Workflow

1. Clarify: Read the artifact, selected schema or policy text, validator
   configuration, exception records, and repository guidance before specifying.
   Map each requested check to an actual rule.
   If only an external label or unsupplied rule set is named, then Ask the user
   for the applicable source text and omit unsupported claims.

2. Specify: Record rule-set identity and revision, applicability predicates,
   check procedures, accepted exceptions, and the scope of the conclusion.
   If no target is supplied, then propose a labeled illustrative default:
   every applicable supplied local rule checked, with unchecked rules reported
   as unknown rather than passed; confirm with the user/stakeholder.
   Ask at most three questions about the rule source, artifact scope, and
   applicability or exception authority before making a practical checker change.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [rule-check decisions](./references/design-guide.md)
   when adding schema gates, naming checks, or rule-result attribution.
   If a rule is mechanically checkable, then implement the stated predicate
   without broadening or weakening it.
   If a rule needs judgment or its applicability is unresolved, then preserve an
   explicit manual or unknown result instead of inventing an automated pass.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Exercise violating and satisfying artifacts for each implemented
   predicate and inspect their rule identifiers and evidence locations.
   If a checker exits successfully while omitting an applicable rule, then
   report partial checking rather than whole-rule-set conformance.

5. Report: Return the selected rule revision, per-rule results, artifact revision,
   accepted exceptions, and checks still requiring judgment.
   If evidence covers only a local schema and naming convention, then limit the
   conclusion to those rules; do not imply legal compliance or certification.

## Specification patterns

- **Rule satisfaction:** For `{artifact_revision}`, every applicable rule in
  `{selected_rule_set_revision}` shall meet `{rule_specific_predicate}`,
  verified by `{check_and_evidence_location}`.
- **Check coverage:** `{checker}` shall report `{pass_fail_unknown_not_applicable}`
  for `{enumerated_rules}`, attributing `{exceptions_and_unchecked_rules}`
  without presenting them as ordinary passes.

Use the illustrative local-rule proposal in Specify when targets are missing;
confirm with the user/stakeholder and do not select a new rule set silently.

## Rules of thumb

- Check the original artifact before applying schema defaults; inserting a
  required field produces a changed artifact, not proof that the original conformed.
- Keep not-applicable and unchecked distinct from passed; an empty check set
  cannot establish that an artifact satisfies the selected rules.
- Attribute a finding to the rule's actual predicate and artifact location;
  a generic "invalid" message cannot establish which obligation was violated.
- Keep an accepted exception visible beside the unmet rule; a waiver is not
  evidence that the artifact satisfied that rule.

## Verification

Use schema validation, predicate fixtures, and rule-to-check coverage review.
Include accepted and rejected boundary forms from the supplied rule text.
Inspect the loaded rule revision rather than only the configured filename.
Pin that revision in the result; an older-schema pass does not cover changed rules.
Record unchecked predicates and reasons, including required human judgment.
Retain original artifact and finding locations so results can be reproduced.
Verify that exception scope matches the artifact and rule it names.
Do not treat a tool's successful exit as evidence for rules it cannot inspect.
Use external standard claims only when the allowlist and supplied source support
their exact applicability; this skill supplies no legal conclusion.

## Done checklist

- [ ] Identify the actual selected rule text and revision.
- [ ] Resolve applicability for the artifact scope.
- [ ] Map each applicable rule to a check or explicit unknown result.
- [ ] Exercise satisfying and violating artifacts for implemented predicates.
- [ ] Inspect finding rule identifiers and artifact locations.
- [ ] Attribute exceptions without turning violations into passes.
- [ ] Bound the conclusion to checked rules and retained artifact evidence.

## Failure modes

- Claiming conformance from a rule-set name without inspecting its contents.
- Using a pass from a different rule revision.
- Counting unchecked or inapplicable rules as successful checks.
- Treating an approved exception as proof of rule satisfaction.
- Implying external certification from a local checker result.

## References

- Read [rule-check decisions](./references/design-guide.md) when mapping selected
  rules to executable checks and qualified results.
- Read [event-envelope example](./references/worked-example.md) when reporting
  schema and naming findings without choosing a new convention.
