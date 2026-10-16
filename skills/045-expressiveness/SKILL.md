---
name: expressiveness
description: >-
  Adds missing distinctions to a notation when tickets say "this rule cannot say owner only", "we cannot express an explicit denial", or "different policies serialize identically". Not for shortening adequate notation (see conciseness) or setting precision alone (see formality).
---

# Expressiveness

## Definition and scope

Expressiveness means a notation or interface can directly represent the
distinctions and operations its users need. Check which different intentions
remain distinguishable after representation and interpretation.
Separate missing semantic capability from shortening adequate notation
(`conciseness`) and defining interpretation precision (`formality`).

## Use when / Don't use when

- Apply when different policy intentions collapse into the same representation,
  or a required restriction or explicit denial cannot be stated.
- Include domain meanings, serialization, and the interpreter that consumes them.
- Route verbose but adequate notation to `conciseness`.
- Route ambiguous interpretation of already available constructs to `formality`.
- Route broad abstraction coverage to `generality` when no missing distinction
  or operation has been identified.

## Workflow

1. Clarify: Read the notation/schema, parser, interpreter, serialization, and
   domain examples before proposing new constructs.
   Collect pairs of intentions that must mean different things.
   If "more expressive" identifies no missing meaning, then Ask the user which
   required intention cannot be represented by the current interface.

2. Specify: Record the intended distinctions, valid representations, evaluation
   meanings, incompatible combinations, and migration behavior for old forms.
   If no target is supplied, then propose a labeled illustrative default:
   each named contrasting intention has a distinct representation and the
   intended evaluation outcome; confirm with the user/stakeholder.
   Ask at most three questions covering domain distinctions, interpretation,
   and backward handling before changing the notation.

3. Design/Implement: Read [representation decisions](./references/design-guide.md)
   when selecting tagged constructs, explicit negative forms, or serialization.
   If multiple intentions serialize identically, then preserve their distinctions
   in the representation rather than inferring intent from external context.
   If a new construct has no agreed evaluation meaning, then leave it proposed
   instead of implementing an arbitrary interpreter rule.

4. Verify: Encode contrasting intentions, serialize/parse them, and inspect their
   resulting evaluations with distinguishing inputs.
   If the parser retains a tag but evaluation ignores it, then fail the missing-
   meaning requirement; syntactic variety alone is not expressiveness.

5. Report: Return the missing-distinction map, new construct meanings, contrasting
   evaluation evidence, and intentions still not representable.
   If only the requested cases are covered, then withhold claims of general
   language completeness or coverage of all future policies.

## Specification patterns

- **Distinction:** `{notation}` shall represent `{contrasting_intentions}`
  distinctly through `{serialization_and_parsing}`, producing
  `{different_required_evaluations}` on `{distinguishing_inputs}`.
- **Operation:** `{construct}` shall express `{required_operation_or_restriction}`
  under `{defined_semantics}`, rejecting `{unsupported_ambiguous_forms}`,
  verified by `{representation_to_evaluation_fixture}`.

Use the illustrative contrasting-intention proposal in Specify when numbers are
absent; confirm with the user/stakeholder rather than inventing a language score.

## Rules of thumb

- Preserve distinct intentions through serialization; extra syntax is useless
  if its meaning collapses onto the same stored form.
- Give a needed restriction an explicit representation instead of requiring
  callers to infer it from an omitted field with unrelated meanings.
- Keep explicit denial distinct from absence of a rule when later composition
  assigns them different effects; collapsing them loses an intended policy choice.

## Verification

Use contrastive domain fixtures, serialization round trips, and interpreter review.
Retain the intention, encoded form, parsed value, input context, and output.
Exercise both sides of a required distinction and unsupported tags.
Use inputs that distinguish the constructs' meanings; identical owner/non-owner
outcomes alone cannot establish the requested owner-only distinction.
Check old forms under the declared migration meaning rather than silently
reinterpreting them as new constructs.
Keep unsupported cases visible; do not add filler constructs to inflate coverage.
Test semantic preservation separately from shorter notation or nicer wording.

## Done checklist

- [ ] Identify the exact missing distinctions or operations.
- [ ] Define the semantics and unsupported combinations of each new construct.
- [ ] Preserve contrasting intentions through stored and parsed forms.
- [ ] Evaluate inputs that produce the required different outcomes.
- [ ] Check unknown constructs without inventing fallback meaning.
- [ ] Verify backward interpretation of existing forms where in scope.
- [ ] State remaining unrepresentable intentions and scope limits.

## Failure modes

- Adding keywords that the interpreter ignores.
- Encoding different intentions as the same object.
- Treating a shorter existing expression as new semantic capability.
- Giving an explicit denial the same effect as an absent rule without agreement.

## References

- Read [representation decisions](./references/design-guide.md) when selecting
  constructs that preserve required domain distinctions.
- Read [owner-policy example](./references/worked-example.md) when tracing
  contrasting intentions through notation and evaluation.
