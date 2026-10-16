---
name: learnability
description: >-
  Checks learning through product use when tickets say "new users never get the hang of it", "people still need help after practicing", or "can beginners do it unaided next time". Not for courses (see trainability), experienced task performance (see usability), or reading flow (see readability).
---
# Learnability

## Definition and scope

Learnability means a newcomer can acquire the ability to perform the intended
task through using the product. Observe acquisition and later unaided attempts;
separate a structured teaching intervention (`trainability`) and current task
performance without a learning claim (`usability`).

## Use when / Don't use when

- Apply when unfamiliar users require repeated hints or cannot transfer practice
  to another instance of the same task.
- Route building a course or instructor-led exercise to `trainability`.
- Route experts' current task errors to `usability`; a single successful novice
  attempt does not establish that the user acquired independent ability.

## Workflow

1. Clarify: Inspect task-flow code, onboarding docs, existing hints, help content,
   and novice feedback before choosing a learning intervention.
   If prior exposure or expert coaching is unknown, then Ask the user and record
   that uncertainty rather than calling the audience untrained beginners.

2. Specify: Choose newcomer background, skill, initial attempt, allowed practice,
   assistance accounting, changed-instance probe, and any retention interval.
   If the user wants practical onboarding improvement, then offer this trial:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Audience/skill: documented newcomers and the requested product task.
   Sequence: initial attempt, product-guided practice, then unaided changed-instance probe.
   Assistance: record prompts, help openings, and facilitator interventions separately.
   Trial scope: 2 practice opportunities; transfer probe changes task data, not skill demand.
   Outcome: independently correct task result under agreed support and context.
   Preservation: no hidden prefilled result or reduced task requirements in the probe.
   Evidence: prior-exposure record, attempt traces, hint use, and probe outcome.
   Limits: no delayed-retention claim without an agreed later probe.
   ```

   Ask at most three groups about newcomer background and task; permitted practice
   and help; and independent success or delayed-retention needs. Start a reversible
   hint or onboarding design while scope decisions remain recorded as proposals.
   If no learning criterion exists, then propose the illustrative acquisition
   sequence and confirm with the user/stakeholder before treating it as acceptance.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [acquisition patterns](./references/design-patterns.md)
   when changing progressive hints, safe practice, or transfer probes.
   If a hint gives the exact answer, then remove that assistance from the probe
   so completion cannot masquerade as independently acquired task ability.
   If the practice data repeats in assessment, then change the instance without
   changing the target skill; memorizing an answer is not the intended transfer.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Observe initial and later attempts under the recorded support conditions,
   including an unaided changed-instance attempt where independence is required.
   If help or facilitator rescue was needed, then retain that result as assisted
   rather than resetting the record to an apparent independent success.

5. Report: Deliver the product changes, acquisition sequence, assistance history,
   transfer outcomes, and unresolved audience or retention limits.
   If only immediate practice succeeded, then withhold claims about later retention
   or other task types that were never probed.

## Specification patterns

- **Acquisition:** After `{allowed_product_practice}`, `{newcomer_background}` shall
  perform `{target_task}` under `{assistance_conditions}`, meeting
  `{confirmed_transfer_criterion}` on `{changed_instance_and_result_oracle}`.
- **Retained ability:** Following `{agreed_delay}`, `{audience}` shall repeat
  `{skill_probe}` with `{allowed_support}`, verified by `{attempt_trace}` and
  compared with `{initial_exposure_and_assistance_record}`.

Use the illustrative practice sequence if no learning target is known; confirm
with the user/stakeholder. Ask the user before adding any delayed-retention promise.

## Rules of thumb

- Do inspect what users discover before a walkthrough supplies the procedure;
  teaching the answer can conceal whether ordinary product use permits acquisition.
- Don't credit a copied practice answer as transfer; change the task instance
  while holding the acquired skill demand stable.
- Do record hint use against each attempt instead of erasing failed starts;
  the independence claim depends on what support the learner actually received.
- Do place discovery cues where newcomers first choose between task alternatives;
  a detached course is not a repair for an unexplained first-use product decision.
- Don't infer retained ability from an immediate repeat; any later-use claim needs
  a separately agreed interval and a probe after it.
- Do distinguish domain knowledge from product exposure when choosing first-use
  trials; requiring expert inference can hide the product discovery barrier for genuine newcomers.

## Verification

Use novice task observation, controlled-assistance trials, and changed-instance
probes. Capture task inputs, existing knowledge, failed starts, help openings,
facilitator cues, result state, and whether the probe demanded the same skill.
Check onboarding code cannot pre-complete the assessed outcome. Distinguish
immediate acquisition, assisted success, transfer, and delayed retention.

## Done checklist

- [ ] Record prior product exposure and relevant domain knowledge for the audience.
- [ ] Retain an initial attempt distinct from product-guided practice.
- [ ] Inspect hints and fixtures for answers that leak into the assessed result.
- [ ] Preserve failed attempts, help requests, and facilitator interventions.
- [ ] Run a changed-instance probe with the agreed skill demand and assistance.
- [ ] Check the actual result against the task oracle, not just a clicked finish button.
- [ ] Limit retention claims to an observed later probe or mark them unavailable.

## Failure modes

- Calling a completed walkthrough evidence of independent task ability.
- Reusing the practice answer as the supposedly new assessment instance.
- Hiding facilitator rescue inside a reported successful attempt.
- Treating expert users as representative product newcomers without qualification.
- Claiming retention from an immediate repetition alone.

## References

- Read [acquisition patterns](./references/design-patterns.md) when selecting
  product practice, fading help, or independent transfer evidence.
- Read [filter-learning example](./references/worked-example.md) when tracing
  beginner attempts, assistance, and a new task instance without a course.
