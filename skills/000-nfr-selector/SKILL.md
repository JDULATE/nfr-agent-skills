---
name: nfr-selector
description: >-
  Selects and sequences NFR skills when asked "which NFRs matter?", "make this production-ready", or "balance security and speed". Proposes the smallest covering set and exposes conflicts. Not for a single identified quality (see performance-efficiency-time-or-space-bounds).
---
# NFR Selector

## Definition and scope

Choose the smallest justified set of NFR skills for an explicit selection request,
a broad readiness request, or several quality concerns presented together.
Read the repository index and sibling boundaries; do not reconstruct its taxonomy
from memory. Route one identified quality directly to its individual skill.

## Use when / Don't use when

- Apply when the user asks which NFRs deserve attention for a project.
- Apply when a broad goal such as production readiness needs a scoped quality plan.
- Apply when several qualities need priorities, conflict decisions, and sequencing.
- Route one elapsed-time target directly to `performance-efficiency-time-or-space-bounds`.
- Route one personal-data lifecycle concern directly to `privacy`.
- Ask a focused sibling question for an ambiguous single concern; ambiguity alone
  does not justify running a catalogue-wide selection exercise.

## Workflow

1. Clarify: Locate the NFR bundle root containing `selector.json`; resolve this
   skill's real location or use the bundle path supplied by the user. Read its
   `INDEX.md` and `references/disambiguation-map.md` on every selection, rather
   than an unrelated target project's index. Inspect the target project's code, docs, stated goals,
   existing requirements, and available evidence before suggesting interventions.
   If these repository resources are unavailable, then Ask the user for access;
   do not invent entries or priorities from remembered quality models.
   Ask at most three clarifying questions in total about the outcome/scope,
   consequences of failure, and constraints that actually affect selection.
   Carry answered questions into later skill handoffs instead of restarting interviews.
   If one identified NFR already covers the request, then hand off directly.

2. Specify: Map each stated concern to an observable acceptance question and an
   exact indexed slug. Separate facts, user constraints, and proposed assumptions.
   If a term has competing repository meanings, then read its disambiguation row
   and ask only for the fact needed to choose between them.
   Show every assumption, proposed default, excluded concern, and unknown before
   building anything. Include the ordered skills, why each is necessary, the
   evidence each must produce, and the proposed conflict decisions in one plan.
   If targets are missing, then propose qualitative acceptance boundaries or
   clearly labeled illustrative numeric defaults; confirm with the user/stakeholder.
   Keep unknown targets unresolved rather than calling readiness established.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [selection decisions](./references/design-guide.md) when
   deciding coverage, dependencies, or competing quality claims.
   Rank by the user's stated consequences and constraints; label inferred priorities
   as proposals. Remove any skill that adds no distinct requested acceptance question.
   If a prerequisite supplies evidence another skill needs, then sequence it first;
   independent concerns need no invented dependency or mandatory infrastructure.
   If performance, security, and maintainability may conflict, then name the affected
   requirements and a discriminating check; do not assume one universally wins.
   Read each selected SKILL.md before its handoff and follow that skill's Workflow.
   Build only the smallest authorized version covering the agreed concerns.
   Offer larger extensions separately; obtain the user's yes unless already authorized.
   If the user requested advice only, then return the plan without implementing it.

4. Verify: Check that every requested concern is covered by a selected skill or
   explicitly deferred, and that each selected skill has a distinct justification.
   If an intervention satisfies one quality but jeopardizes another, then retain
   both acceptance checks and report the unresolved trade-off to the user.
   Check handoff paths, assumption disclosure, question count, and sequence against
   actual project evidence. Read [selection examples](./references/worked-example.md)
   when separating a minimal plan from an unsupported readiness claim.
   Do not substitute completed routing for implementation or runtime verification.

5. Report: Return ordered slugs, scope, priorities, assumptions, conflict decisions,
   changes made, and evidence or limitations for each selected acceptance question.
   If any required check was not run, then say what remains unverified.
   Keep a planning result distinct from a claim that the project is production-ready.

## Specification patterns

- **Coverage:** For `{requested_concerns}`, propose `{minimal_skill_set}` so each
  `{acceptance_question}` has `{owning_skill_and_evidence}`, with `{deferred_scope}` explicit.
- **Conflict:** When `{intervention}` affects `{quality_A_and_quality_B}`, accept it
  only under `{stakeholder_confirmed_tradeoff}`, checked by `{paired_verification}`.
- **Sequence:** Complete `{prerequisite_evidence}` before `{dependent_skill_work}`;
  preserve `{assumptions_and_unresolved_decisions}` across handoffs.

When no targets exist, propose these records as illustrative defaults and
confirm with the user/stakeholder before treating them as accepted requirements.

## Rules of thumb

- Select against uncovered acceptance questions; a popular quality label is not
  a reason to add another skill to the plan.
- Separate sibling meanings before prioritizing them; ranking two names for the
  same intended question creates duplicate work rather than extra coverage.
- Preserve both sides of a quality conflict in the plan; a local improvement
  cannot silently replace another selected skill's acceptance condition.
- Carry scope, assumptions, and prior answers into handoffs; per-skill interviews
  must not multiply the selector's question budget.
- Bypass selection for one identified concern; the selector must not become a
  mandatory gate before ordinary individual-skill use.

## Verification

Compare request-to-skill coverage with the index and disambiguation rows.
Inspect omitted concerns, redundant selections, proposed priorities, and real
prerequisites. Check each paired requirement after a conflict-affecting change.
Verify that assumptions were shown before implementation and that advice-only
requests produced no build work. Record which downstream Workflows actually ran.

## Done checklist

- [ ] Read the current index and disambiguation map.
- [ ] Inspect the target project before proposing implementation.
- [ ] Map every requested concern to a skill or an explicit deferral.
- [ ] Remove selections without a distinct acceptance question.
- [ ] State every assumption and proposed default before building.
- [ ] Keep clarifying questions within the shared budget.
- [ ] Name conflicts and sequence only evidenced dependencies.
- [ ] Report downstream checks completed and those still unverified.

## Failure modes

- Applying a fixed readiness checklist without reading the project's scope.
- Choosing many sibling labels that answer the same acceptance question.
- Inventing a universal quality ordering or a conflict without project evidence.
- Treating a selector plan or a routed description as a verified implementation.
- Hijacking a single-quality request with a full selection workflow.

## References

- Read [selection decisions](./references/design-guide.md) when choosing a minimal
  covering set, deciding order, or exposing conflicting requirements.
- Read [selection examples](./references/worked-example.md) when handling broad
  readiness, explicit selection, or several qualities without expanding scope.
