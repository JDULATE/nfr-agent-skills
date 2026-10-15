---
name: conciseness
description: >-
  Removes unnecessary wording or representation while preserving required
  meaning when users say "cut repeated wording", "make this shorter without
  losing conditions", or "remove the redundant explanation". Checks retained
  propositions, exceptions, and obligation strength rather than length alone.
  Not for absent subject coverage (see comprehensiveness), visual character
  recognition (see legibility), or confusing reading structure alone (see
  readability).
---
# Conciseness

## Definition and scope

Conciseness means omitting unnecessary material while retaining intended meaning.
Remove repetition and avoidable representation cost against a preserved proposition
set; distinguish following structure (`readability`), conceptual explanation
(`comprehensibility`), and needed subject coverage (`comprehensiveness`).

## Use when / Don't use when

- Apply when a passage repeats the same obligation, buries a short result in
  unnecessary framing, or contains material the intended task does not need.
- Route a missing concept to `comprehensibility` instead of cutting it further.
- Route reducing architectural machinery to `simplicity`; fewer source characters
  alone cannot establish a simpler design or better runtime behavior.

## Workflow

1. Clarify: Read the surrounding code/text, caller contracts, glossary, docs,
   required topics, and use context before deciding which material is unnecessary.
   If audience-required meaning is unknown, then Ask the user what must remain
   rather than treating unfamiliar detail as disposable verbosity.

2. Specify: Inventory propositions, qualifiers, exceptions, external names, and
   required context; choose a representation count and a preservation check.
   If the user wants a shorter artifact, then offer this reduction record:

   ```text
   Illustrative reduction proposal; confirm with the user/stakeholder:
   Artifact: requested passage or representation with surrounding context recorded.
   Retained meaning: source-backed actors, obligations, scope, exceptions and references.
   Example target: 10% fewer whitespace-separated words for a prose passage.
   Decision: reduction is accepted only if retained propositions and required context survive.
   Scope: remove redundant framing/repeated claims; do not invent new abbreviations.
   Evidence: before/after count, proposition mapping, boundary-case meaning comparison.
   Open items: actual budget, indispensable context, public names, and artifact owner.
   ```

   Ask up to three questions about target audience/task; meaning and external
   constraints that must stay; and length measure or illustrative target changes.
   Proceed to a deletion/merge proposal before treating a reduction as accepted.
   If no number is supplied, then propose the labeled prose target only where
   applicable and confirm with the user/stakeholder; reject cuts that lose meaning.

3. Design/Implement: Read [reduction patterns](./references/design-patterns.md) when
   merging repeated claims, trimming framing, or preserving essential qualifiers.
   If repeated wording expresses different conditions or actors, then retain the
   distinction rather than merging by surface similarity.
   If a shorter name or extraction adds glossary lookup or cross-file chasing,
   then include that displaced reading cost instead of claiming a local length win.

4. Verify: Recount using the same procedure and map every retained proposition
   into the shortened artifact, including negative and boundary cases.
   If a cut removes an exception or strengthens an obligation, then restore the
   meaning even if that causes the candidate to miss the proposed length target.

5. Report: Return removed redundancy, preserved proposition evidence, count rule,
   before/after counts, and any additional context readers now need.
   If shorter text changes behavior or policy, then separate that change for
   review rather than reporting a successful conciseness-only edit.

## Specification patterns

- **Reduction:** `{artifact}` shall represent `{retained_propositions_and_context}`
  within `{confirmed_length_budget}` using `{counting_rule}`, verified by
  `{proposition_map_and_boundary_case_comparison}`.
- **Repetition:** `{repeated_claims}` shall be represented by `{shared_statement}`
  while preserving `{distinct_actors_conditions_and_exceptions}`, checked against
  `{source_obligation_inventory}` without `{new_external_lookup_burden}`.

Use the illustrative word-reduction target as an option, not a universal quality rule;
confirm with the user/stakeholder. Ask the user before dropping required context.

## Rules of thumb

- Do merge only claims with the same actor, condition, and obligation strength;
  similar wording can encode different duties that a shorter sentence would erase.
- Do remove framing that adds no proposition before cutting domain qualifiers;
  deleting the exception is a meaning change, not a concise expression of the rule.
- Do count displaced definitions and cross-references when shortening a passage;
  moving all necessary context elsewhere can hide rather than remove representation cost.
- Do preserve repeated material when separate use contexts genuinely need it;
  forcing a single distant statement can make an apparently shorter artifact incomplete.
- Don't use opaque abbreviations to meet a length target; decoding instructions
  and a new glossary entry can exceed the redundancy supposedly removed.
- Don't equate fewer code tokens with preserved semantics; a condensed expression
  that changes evaluation, exceptions, or observable effects is a different implementation.

## Verification

Use obligation/proposition mapping, consistent word counting, and boundary-case
review for prose; use focused behavioral comparisons for any code condensation.
Inspect dropped negation, quantifiers, actor scope, and changed reference targets.
Report count reduction separately from preserved meaning and audience interpretation;
none follows automatically from the others.

## Done checklist

- [ ] Recompute before/after length using the same stated counting rule.
- [ ] Map each retained actor, claim, qualifier, and exception into the candidate.
- [ ] Compare positive/negative boundary cases for unchanged obligation meaning.
- [ ] Check merged claims do not erase different actors or conditions.
- [ ] Account for new lookup context, abbreviation definitions, or reference jumps.
- [ ] Verify code behavior if the condensed artifact is executable.

## Failure modes

- Cutting the limiting clause while retaining an overbroad requirement.
- Counting text moved to a glossary as if its necessary reading cost disappeared.
- Merging look-alike statements that apply to different actors or conditions.
- Accepting a smaller representation that changes code or policy semantics.
- Reporting a percentage reduction from different before/after counting procedures.

## References

- Read [reduction patterns](./references/design-patterns.md) when selecting deletions,
  resolving repeated claims, or accounting for context moved elsewhere.
- Read [requirement compression example](./references/worked-example.md) when checking
  exact words, retained conditions, and concrete counterexamples after shortening.
