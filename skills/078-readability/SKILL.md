---
name: readability
description: >-
  Improves and checks how readers follow text or code when users say "make this
  code easier to read", "clarify these variable names", "break up this dense
  paragraph", or "reduce nesting". Not for visual character recognition (see
  legibility) or missing conceptual explanations (see comprehensibility).
status: draft
---
# Readability

## Definition and scope

Make existing meaning easier for the intended reader to follow through naming,
ordering, grouping, and locally visible control flow while preserving its substance.
Separate these reading decisions from visual symbol recognition (`legibility`),
explaining a missing concept (`comprehensibility`), and removing unnecessary words
for their own sake (`conciseness`).

## Use when / Don't use when

- Apply when readers lose track of a value's meaning, must mentally unpack a
  dense expression, or struggle to follow the order of an existing explanation.
- Include code, requirements, and prose only after identifying the intended
  audience and the actual passage or path they need to follow.
- Route font recognition or display contrast to `legibility`; route absent domain
  explanations to `comprehensibility` or `understandability` as appropriate.
- Route a wrong computation to `correctness`; do not treat a semantic change as
  a readability-only rewrite or use a shorter diff as its acceptance evidence.

## Workflow

1. Clarify: Read the surrounding source, public contracts, glossary, style rules,
   tests, or adjacent documentation before specifying a rewrite.
   Identify intended readers, reading tasks, and the statements whose meaning must stay.
   If audience, authoritative meaning, or external name compatibility is unclear,
   then Ask the user before renaming or reorganizing that material.

2. Specify: Choose questions a reader should answer, an evidence-backed answer
   key, and the reading conditions; distinguish correct explanation from speed.
   Identify preserved behavior, obligations, public names, and observable ordering.
   If no threshold is given, then propose the illustrative reading task below and
   confirm with the user/stakeholder before using it as an acceptance gate.

3. Design/Implement: Replace ambiguous local names with domain terms, expose
   intermediate meanings, and arrange conditions or sentences in reading order.
   Keep related reasoning close enough to follow without unnecessary jumps.
   If an extraction, guard clause, or reordered sentence changes evaluation order,
   side effects, exception behavior, or obligation strength, then separate that
   change for explicit review instead of presenting it as a readability edit.

4. Verify: Compare the rewrite against the preserved contract and run relevant
   behavior checks for code or an obligation-by-obligation comparison for prose.
   Ask intended readers to answer the specified questions using the agreed material.
   If readers answer incorrectly or no representative reader is available, then
   report the misunderstanding or mark the reading claim unverified and revise as needed.

5. Report: Show the before/after reading obstacle, the preserved meaning checks,
   and the reader answers with timing only under the agreed protocol.
   If formatting or a complexity score is the only evidence, then report that
   limited evidence and do not claim that readers understood the rewrite better.

## Specification patterns

Tie each pattern to the specific artifact and audience; avoid universal style limits.

- **Code reading:** For `{function_or_path}`, `{intended_reader}` shall correctly
  explain `{value_meanings_branch_outcomes_and_order}` under `{reading_conditions}`
  within `{confirmed_reading_budget}`, scored against `{source_grounded_answer_key}`
  while `{behavior_and_public_contract}` remains unchanged.
- **Prose reading:** For `{passage}`, `{target_audience}` shall identify
  `{actor_required_action_condition_and_exception}` using `{allowed_context}`,
  meeting `{confirmed_answer_and_time_criteria}` against `{reviewed_answer_key}`
  with every original obligation, qualifier, and cross-reference preserved.
- **Name clarity:** For `{ambiguous_local_symbols}`, readers shall associate each
  with `{agreed_domain_meaning}` in `{task_and_scope}`, verified by
  `{reader_explanation_check}` without changing `{external_names_or_data_keys}`.

Illustrative example only: propose a 2-minute reading budget for `{scoped_task}`
with the required answers correct; confirm with the user/stakeholder.
Ask the user to confirm the questions, answer key, reader familiarity, available
context, and handling of incorrect answers before accepting that budget.

## Rules of thumb

- Do name a local value for its domain meaning or unit; don't shorten it merely
  to match an abbreviation that the intended reader does not already use.
- Do expose a meaningful intermediate result when it removes mental unpacking;
  don't introduce a chain of aliases that makes readers chase the same value.
- Do flatten nesting only when the resulting exit order and side effects stay
  intact; don't move a guard ahead of work whose execution is part of the contract.
- Do keep a condition and its consequence visibly connected; don't scatter a
  short explanation across helpers or references just to reduce local line count.
- Do preserve external field names and keyword-call contracts when renaming locals;
  don't silently rename serialized keys or a public parameter for aesthetic consistency.
- Do retain an obligation's actor, condition, exception, and strength when splitting
  a sentence; don't turn a conditional requirement into an unconditional instruction.
- Don't replace a domain-specific expression with a supposedly simpler synonym
  until the intended readers confirm that it carries the same meaning.

## Verification

Use source comparison, behavioral regression, and reader-task review categories.
For code, inspect side-effect order, exceptions, boundary inputs, public signatures,
and serialized keys; use existing focused tests rather than equating a formatter
pass with meaning preservation. For prose, map each original obligation and
qualifier to its new location and inspect cross-references after reordering.
Record readers' answers before giving hints, including incorrect interpretations
and places they backtracked. Compare equivalent reading conditions; treat speed,
formatter results, and static complexity signals as supporting evidence only.

## Done checklist

- [ ] Identify the audience, artifact, and concrete reading obstacle.
- [ ] Ground reading questions and an answer key in the original authoritative material.
- [ ] Agree the reading context, correctness criteria, and any timing budget.
- [ ] Trace original behavior or prose obligations to the rewritten form.
- [ ] Inspect external names, evaluation order, side effects, and exceptions where applicable.
- [ ] Run focused behavior checks or complete the prose obligation comparison.
- [ ] Record unaided reader answers or explicitly mark reader verification unavailable.
- [ ] Report semantic concerns separately from presentation improvements and tool scores.

## Failure modes

- Shortening names while increasing the glossary knowledge needed to read them.
- Extracting tiny helpers that force readers to jump away from a coherent condition.
- Flattening code by moving a side effect or changing which exception appears first.
- Splitting a requirement while dropping its actor, qualifier, or exception.
- Treating faster reading, fewer lines, or a formatter pass as proof of correct understanding.

## References

- Read [reading review protocol](./references/reading-review-protocol.md) when choosing
  audience tasks, preserving meaning, or interpreting reader and static-tool evidence.
- Read [calculation worked example](./references/calculation-example.md) when exposing
  intermediate meaning without renaming an external contract or changing arithmetic.
