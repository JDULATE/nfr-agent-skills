---
name: comprehensiveness
description: >-
  Checks topic coverage for an audience when users ask "this guide skips recovery", "are we missing topics for operators", or "our manual only covers the happy path". Not for a fixed inventory (see completeness), unclear passages (see comprehensibility), or the system model (see understandability).
---
# Comprehensiveness

## Definition and scope

Comprehensiveness means an explanation covers the subject areas its audience
needs. Discover and justify that breadth; distinguish checking a fixed required
set (`completeness`), interpreting a passage (`comprehensibility`), and building
a causal model of the system (`understandability`).

## Use when / Don't use when

- Apply when a guide discusses setup but ignores operation, failures, handoff,
  or other subject areas supported by the intended audience's actual questions.
- Route a missing entry in an agreed closed list to `completeness`.
- Route unnecessary repetition to `conciseness`; do not delete a needed subject
  solely because it makes the explanation longer.

## Workflow

1. Clarify: Read code paths, existing docs, support questions, and audience/task
   records before proposing which subjects the explanation should cover.
   If a stakeholder already supplies a fixed exhaustive inventory, then identify
   the completeness check separately from discovery of missing subject areas.

2. Specify: Record audience questions, candidate subjects, evidence of need,
   sufficient depth, locations, justified exclusions, and review ownership.
   If the user asks to broaden a guide, then propose this scoped coverage record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Audience/purpose: named guide readers and the decisions they must make.
   Breadth trial: inspect 3 contrasting reader journeys, including a non-happy path.
   Map: reader question -> needed subject -> source evidence -> usable explanation location.
   Depth: enough explanation to support the mapped decision; a heading alone does not count.
   Exclusions: explicit reason and owner; unresolved topics remain gaps, not irrelevant.
   Acceptance: stakeholder-approved subject coverage, with unassessed journeys disclosed.
   Evidence: question sources, source-path review, topic map, and reader/reviewer feedback.
   Status: discovery proposal; not an exhaustive inventory or topic quota.
   ```

   Ask at most three groups about readers and decisions; neglected questions and
   source evidence; and depth, exclusions, or scope limits. Continue with a topic map.
   If no breadth measure is supplied, then offer the illustrative journey trial
   and confirm with the user/stakeholder before treating its scope as sufficient.

3. Design/Implement: Read [coverage-mapping practices](./references/design-patterns.md)
   when distinguishing genuine subjects from decorative headings.
   If a question spans normal use and recovery, then cover both decision contexts
   or record the recovery gap; a setup-only paragraph does not cover operation.
   If the subject is explained elsewhere, then make its location discoverable
   from the relevant guide rather than duplicating an entire chapter.

4. Verify: Trace each retained subject to an actual explanation supporting its
   reader question; inspect adjacent failure and handoff questions for blind spots.
   If a reader cannot locate the needed discussion, then record a coverage-access
   gap instead of counting an unfindable reference as effective breadth.

5. Report: Return the coverage map, added discussions, justified exclusions,
   source disagreements, and audience journeys not reviewed.
   If only the selected journeys were explored, then limit the breadth claim
   to them instead of calling the manual universally comprehensive.

## Specification patterns

- **Subject breadth:** For `{audience_and_decisions}`, `{guide}` shall address
  `{approved_subject_domains}` to `{decision_support_depth}`, verified by
  `{question_to_explanation_mapping_and_review}` with `{explicit_exclusions}`.
- **Gap discovery:** Review `{contrasting_reader_journeys}` against `{source_and_question_evidence}`;
  each newly needed subject shall receive `{usable_discussion_or_owned_gap}`,
  with `{unexplored_contexts}` retained as limitations.

Use the illustrative journey trial to initiate a missing scope definition;
confirm with the user/stakeholder. Ask the user which readers and decisions are excluded.

## Rules of thumb

- Do derive subject breadth from reader decisions rather than the existing table
  of contents; auditing only current headings cannot reveal an omitted domain.
- Don't credit a topic heading as coverage when it contains no explanation for
  the mapped reader decision; breadth counts subjects addressed, not labels displayed.
- Do inspect an audience's handoff and recovery questions when the guide only
  describes setup; repeating setup details does not fill those missing subject areas.
- Do preserve justified subject exclusions beside the coverage map; unexplored
  domains must not silently become claims that no audience needs them.
- Don't use page count as breadth evidence; a long treatment of the happy path
  can leave every recovery and responsibility question unanswered.

## Verification

Use documentation gap review, audience-question mapping, and source-path inspection
categories. Inspect whether the cited explanation exists, is findable, and supports
the claimed decision. Reconcile new topics with actual behavior or mark intended
behavior explicitly. Review unexplored journeys and disagreement about audience
needs; a covered subject is not proof that every required item is present.

## Done checklist

- [ ] Ground reader questions in audience, task, or stakeholder evidence.
- [ ] Link each accepted subject to a usable explanation and relevant source.
- [ ] Inspect failure, recovery, and handoff contexts for missing subject areas.
- [ ] Reject empty headings and undiscoverable destinations as sufficient coverage.
- [ ] Retain exclusions with reasons and an accountable reviewer.
- [ ] State which audiences and journeys remain outside the breadth review.

## Failure modes

- Treating the existing contents list as proof that no subject is missing.
- Adding headings without enough material to support a reader decision.
- Expanding the happy path while omitting recovery and responsibility domains.
- Claiming exhaustive breadth after inspecting only a convenient audience.

## References

- Read [coverage-mapping practices](./references/design-patterns.md) when discovering
  subjects, setting explanatory depth, or separating open breadth from a fixed inventory.
- Read [import-guide example](./references/worked-example.md) when converting
  concrete reader questions into subject additions and explicit unknowns.
