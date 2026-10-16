---
name: readability
description: >-
  Improves code and text reading flow when tickets say "rename these confusing variables", "this function is buried in nesting", or "reorder this paragraph so it flows". Not for character recognition (see legibility) or explaining missing concepts (see comprehensibility).
status: draft
---
# Readability

## Definition and scope

Readability means readers can follow the meaning of code or text without unnecessary
effort. Improve naming, ordering, grouping, and locally visible control flow while
preserving the substance. Separate this work from visual symbol recognition
(`legibility`), explaining a missing concept (`comprehensibility`), and removing
unnecessary words for their own sake (`conciseness`).

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
   If the request is for an improvement, then use the fast path below; otherwise
   Ask the user for unclear audience, meaning, or public-name constraints before
   accepting a formal reading requirement.

2. Specify: Choose questions a reader should answer, an evidence-backed answer
   key, and the reading conditions; distinguish correct explanation from speed.
   Identify preserved behavior, obligations, public names, and observable ordering.
   If a formal threshold is missing, then propose the illustrative reading task
   below and confirm with the user/stakeholder before using it as an acceptance gate.
   For an improvement request, propose the complete reading record in one block:

   ```text
   Illustrative defaults — confirm with the user/stakeholder:
   Artifact/revision: requested passage or function and its current revision.
   Audience/context: documented readers with the existing surrounding source or glossary.
   Task: explain value meanings and branch outcomes, or actor/action/condition/exception.
   Answer key: existing code, tests, or approved prose; resolve contradictions explicitly.
   Acceptance: required answers correct within an illustrative 2-minute reading budget.
   Preservation: unchanged behavior, obligation strength, public names, and data keys.
   Design scope: local naming and grouping; no new behavior or required domain concepts.
   Verification: focused regression or obligation mapping plus unaided reader questions.
   Evidence/owner: before/after diff, preservation results, reader answers, artifact owner.
   Limitations: absent reader evidence remains unverified; static scores are supporting only.
   Status: design assumptions; timing and audience acceptance await confirmation.
   ```

   Ask at most three questions total: who must read this and for which task;
   which meanings or external names must stay fixed; and which reading context,
   budget, or illustrative defaults should change. Proceed to reversible design
   using available answers while others are pending.
   If the authoritative meaning conflicts across sources, then show the conflict
   and alternative wording or code rather than silently choosing new behavior.

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

For a missing reading budget, use the illustrative task default in Specify and
confirm with the user/stakeholder. Ground the answer key and audience in the
artifact's context before using timing as an acceptance condition.

## Rules of thumb

- Do name a local value for its domain meaning or unit; don't shorten it merely
  to match an abbreviation that the intended reader does not already use.
- Do expose a meaningful intermediate result when it removes mental unpacking;
  don't introduce a chain of aliases that makes readers chase the same value.
- Do use guard clauses when they let intended readers trace branch outcomes with
  less backtracking; preserve effect and exit order, and keep the nesting when
  flattening merely moves the reading burden to scattered early returns.
- Do keep a condition and its consequence visibly connected; don't scatter a
  short explanation across helpers or references just to reduce local line count.
- Do clarify an opaque external key with a meaningful local name at its use site,
  so readers can follow the value without changing the wire contract; don't rename
  a serialized key or public parameter merely to improve its spelling.
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
