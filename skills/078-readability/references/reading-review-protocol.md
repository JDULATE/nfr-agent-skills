# Reading review protocol

Establish what readers need to follow before selecting a code or prose style.
Treat the repository's readability boundary as a working convention, not a
universal preference for short lines, small functions, or particular vocabulary.

## Define the reading task

Record audience role, domain familiarity, artifact revision, allowed surrounding
context, expected task, and any accessibility accommodations. Ask the user for
missing audience assumptions. Do not make an expert author's speed the default
for a newcomer who needs the material in a different context.

For code, ask about the meaning and units of values, branch outcomes, dependencies,
and visible order of effects. For prose, ask who must do what, under which
condition, with which exception. Select questions relevant to the actual obstacle.
Trace the answer key to the existing code, approved requirements, or glossary;
resolve disagreements about meaning before presenting a rewritten answer as correct.

Write a requirement with artifact, audience, reading task, allowed context,
answer key, confirmed correctness rule, optional time budget, and preserved meaning.
If no budget exists, propose this illustrative example only: 2 minutes for the
scoped task with required answers correct; confirm with the user/stakeholder.
Ask whether timing is useful for this audience and task before making it a gate.

## Preserve meaning

| Artifact | Inspect before claiming a readability-only change |
| --- | --- |
| Calculation | Operator order, units, rounding locations, and exceptional inputs |
| Branch or guard | Evaluation order, effects, early return behavior, and exceptions |
| Name | Local uses, public signatures, keyword callers, data keys, and documented terms |
| Extracted helper | Hidden captured state, repeated work, and the jumps needed to follow a condition |
| Requirement sentence | Actor, required action, condition, scope, exception, and obligation strength |
| Reordered explanation | Dependencies between statements and the targets of every cross-reference |

If the original meaning appears wrong, report that separately and ask whether a
behavioral or requirements correction is authorized. Do not preserve an apparent
defect silently, but do not disguise its correction as a presentation-only edit.

## Conduct the reader check

- Give readers the agreed material and questions without explaining the rewrite first.
- Record answers, incorrect inferences, requests for context, and backtracking.
- Capture time only if it is part of the accepted protocol and useful to the task.
- Score against the reviewed answer key; distinguish wrong answers from slow correct ones.
- Avoid treating a second reading of the same example as a clean first-read comparison.
- Use equivalent tasks or different readers where feasible; record familiarity and
  presentation order as limitations when a balanced comparison is unavailable.
- Ask the user what participants and outcomes are sufficient for this context;
  do not claim statistical evidence from a convenience review.

If representative readers are unavailable, perform a source-grounded review and
label the reading outcome unverified. List the questions still needing reader
answers. A model's explanation or the author's own walkthrough is not an
independent audience observation.

## Extended review checklist

- [ ] Associate every ambiguous name with a supported domain meaning.
- [ ] Retain any public name whose change would require caller migration.
- [ ] Compare original and rewritten branches over relevant boundary conditions.
- [ ] Identify each effect whose execution or order could have changed.
- [ ] Map every prose qualifier and exception to a retained statement.
- [ ] Keep context needed for a condition near its consequence.
- [ ] Distinguish reader observations from static-tool or author judgments.
- [ ] State whether evidence shows contract preservation, reading success, or both.

## Anti-pattern catalog

- **Abbreviation cleanup:** Reject a shorter name when readers need to decode it.
- **Helper fragmentation:** Keep a coherent rule together when extraction hides its path.
- **Premature guard:** Reject a flattened branch if it changes required work or exceptions.
- **Qualifier loss:** Reinsert dropped conditions before assessing the shorter sentence.
- **Score substitution:** Use complexity or formatting output to locate candidates, not prove readability.
- **Coached success:** Repeat the reader task without hints before counting the answer as unaided.
