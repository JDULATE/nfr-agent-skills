---
name: comprehensibility
description: >-
  Clarifies the meaning of a particular explanation for its intended audience
  when users say "explain what this requirement means", "people misinterpret
  this message", or "clarify who can do what in this paragraph". Tests
  interpretation against source-grounded scenarios. Not for following
  code/text structure alone (see readability), a whole-system mental model
  (see understandability), or current interface state cues (see
  self-descriptiveness).
---
# Comprehensibility

## Definition and scope

Comprehensibility means a particular explanation conveys its intended meaning to
its audience. Clarify concepts, actors, conditions, and implications against an
authoritative source; distinguish reading structure (`readability`), a whole-system
model (`understandability`), and in-context state cues (`self-descriptiveness`).

## Use when / Don't use when

- Apply when people draw the wrong conclusion from a message, requirement, or
  explanation even though they can recognize and read its words.
- Route unnecessary repetition to `conciseness` and absent topic coverage to
  `comprehensiveness`; more or fewer words alone cannot establish correct interpretation.
- Route a visual symbol-recognition problem to `legibility`.

## Workflow

1. Clarify: Read the relevant code, contracts, policy docs, glossary, and surrounding
   explanation before deciding what the artifact should mean.
   If sources disagree on behavior or obligation, then Ask the user which meaning
   is authoritative; do not fix that conflict by inventing a confident explanation.

2. Specify: Identify the passage, audience knowledge, intended propositions,
   misinterpretations, allowed context, scenario questions, and source-grounded answers.
   If the request is practical clarification, then propose this interpretation record:

   ```text
   Illustrative interpretation trial; confirm with the user/stakeholder:
   Artifact/audience: requested explanation and its documented intended readers.
   Meaning: source-backed actors, actions, conditions, exceptions and domain terms.
   Example bound: 0 incorrect interpretations on the agreed scenario questions.
   Probe: paraphrase the rule, apply an included case, reject an excluded case.
   Rewrite: resolve the observed conceptual gap; preserve the source behavior/obligation.
   Evidence: source-to-proposition map, scenario answers without hints, remaining confusion.
   Open items: authoritative meaning, reader prerequisites, accepted questions and owner.
   ```

   Ask at most three groups: audience and misunderstanding; source meaning and
   retained obligations; and allowed context or proposed trial needing revision.
   Proceed to a scoped explanation alternative while disputed meaning stays open.
   If no acceptance bound exists, then offer the illustrative question-bound above
   and confirm with the user/stakeholder before treating it as an agreed reader criterion.

3. Design/Implement: Read [interpretation patterns](./references/design-patterns.md)
   when resolving ambiguous actors, domain concepts, or implied permissions.
   If a reader lacks a concept, then explain it with a source-backed distinction
   rather than merely replacing a word with a shorter synonym.
   If examples imply a broader rule than the source permits, then add a contrasting
   excluded case and rewrite the scope instead of expanding the underlying requirement.

4. Verify: Compare each intended proposition with the revised explanation and ask
   intended readers to interpret new positive/negative scenarios without coaching.
   If answers are wrong, then localize the inferred actor, condition, or concept
   that failed; do not count fluent reading or agreement with the author as comprehension.

5. Report: Return the original misunderstanding, meaning changes in the explanation,
   source preservation checks, reader answers, and remaining conceptual gaps.
   If no representative reader attempted the questions, then label interpretation
   outcomes unverified rather than using the agent's own paraphrase as audience evidence.

## Specification patterns

- **Interpretation:** For `{explanation_and_audience}`, readers shall infer
  `{source_backed_propositions}` under `{allowed_context}`, meeting
  `{confirmed_answer_criterion}` against `{positive_and_negative_scenario_key}`.
- **Boundary:** After reading `{message}`, readers shall distinguish
  `{included_case}` from `{excluded_case}` using `{explicit_condition_or_concept}`,
  verified by `{unaided_case_answers}` with `{original_obligations}` preserved.

Treat the illustrative error bound as a proposed task criterion;
confirm with the user/stakeholder. Ask the user for missing audience or policy meaning.

## Rules of thumb

- Do bind ambiguous pronouns to the actual actor and object; an explanation that
  reads smoothly but assigns permission to the wrong role remains misunderstood.
- Do define an unfamiliar domain distinction where this audience needs it;
  replacing the term with a familiar but different concept creates false understanding.
- Do contrast an excluded case when examples could imply an unrestricted rule;
  positive examples alone can teach permissions the explanation was meant to limit.
- Do distinguish a causal condition from mere event order; after an event does
  not mean because of that event unless the source establishes that implication.
- Don't repair a missing concept by formatting or renaming alone; check which
  inference the reader can now make that the original explanation failed to support.

## Verification

Use proposition/source review, contrast-case interpretation, and audience paraphrase
checks. Preserve actor, scope, exception, and obligation strength while resolving
ambiguous concepts. Record unprompted answers and wrong implications; separate
recognition/reading effort from the semantic inference this skill accepts.
Use fresh equivalent scenarios where repeat exposure could supply the answer.

## Done checklist

- [ ] Trace each intended proposition to its authoritative behavior or policy source.
- [ ] Resolve conflicting source meanings or retain them as explicit open decisions.
- [ ] Compare role, condition, exception, and obligation meaning before/after rewriting.
- [ ] Exercise an included and excluded scenario against the reviewed answer key.
- [ ] Check that any new definition preserves the source's domain distinction.
- [ ] Capture unaided audience interpretations or mark that evidence unavailable.
- [ ] Reconcile remaining wrong answers with the specific inference still unsupported.

## Failure modes

- Substituting an easy synonym that changes a domain concept.
- Treating familiar words as evidence that readers inferred the intended rule.
- Teaching an unrestricted permission through positive examples alone.
- Using the author's coached paraphrase as proof of reader understanding.

## References

- Read [interpretation patterns](./references/design-patterns.md) when choosing
  source-backed propositions, concept contrasts, or unaided scenario questions.
- Read [visibility explanation example](./references/worked-example.md) when mapping
  concrete role/state cases to a clearer explanation without changing permissions.
