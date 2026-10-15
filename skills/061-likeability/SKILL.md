---
name: likeability
description: >-
  Assesses and improves subjective response after using a product when users say "people dislike using this tool", "find out why the experience feels frustrating", or "which interaction do users prefer". Records positive and negative judgments separately from observed task outcomes. Not for visual appeal alone (see attractiveness), task success alone (see usability), or task learning alone (see learnability).
---
# Likeability

## Definition and scope

Likeability means users express a positive subjective response to interacting
with the product. Ground the response in an actual experience; distinguish visual
appeal (`attractiveness`), achieved task outcomes (`usability`), and acquired ability (`learnability`).

## Use when / Don't use when

- Apply when users dislike an interaction, prefer another flow, or describe the
  experience as frustrating despite being able to finish the task.
- Route a judgment about a screenshot's appearance alone to `attractiveness`.
- Route a completion defect to `usability`; retain any preference question here
  without treating sentiment as a substitute for the task result.

## Workflow

1. Clarify: Read interaction code, existing feedback docs, complaint context,
   and task traces before inferring what users like or dislike.
   If feedback concerns only appearance without use, then route aesthetic
   evaluation separately rather than labeling it a post-interaction judgment.

2. Specify: Bind audience, experienced scenario, question, response anchors,
   collection point, comparison conditions, and handling of contradictory responses.
   If the request is to improve sentiment, then propose this experience record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Audience/context: intended users after the named task, using synthetic task data.
   Exposure: same goal and equivalent result/error conditions across compared flows.
   Question: How positive or negative was your experience of this interaction?
   Response trial: 5-point scale, low = negative, middle = neutral, high = positive.
   Follow-up: which moment shaped that response, and what would change it?
   Evidence: response, stated reason, actual task outcome, assistance, and exposure order.
   Decision: present mixed responses and reasons; no universal positive cutoff assumed.
   Status: proposed subjective-response protocol, not a product-wide approval claim.
   ```

   Ask at most three groups about audience/scenario; the complained-about moments
   and permitted changes; and response criteria or comparison constraints.
   Continue to a reversible interaction proposal tied to the reported experience.
   If no measure exists, then propose the illustrative anchored response and
   confirm with the user/stakeholder before selecting a pass rule.

3. Design/Implement: Read [experience-response practices](./references/design-patterns.md)
   when changing disliked interactions or comparing preference evidence.
   If comments name a particular moment, then trace and change that interaction
   rather than restyling unrelated screens and attributing any new rating to it.
   If a candidate removes a control or task result, then keep that functional
   difference explicit instead of comparing sentiment as if the tasks were equivalent.

4. Verify: Collect the response after the specified experience without suggesting
   the preferred answer; retain negative, neutral, and absent responses.
   If observed task success conflicts with the reported feeling, then report both
   rather than correcting the user's opinion to match the task outcome.

5. Report: Return response patterns, quoted reasons with appropriate permission,
   changed interaction points, task-outcome context, and unresolved contradictions.
   If no intended users experienced the candidate, then report a hypothesis;
   withhold claims that the product is now liked better.

## Specification patterns

- **Experience response:** After `{interaction_scenario}`, `{audience}` shall meet
  `{confirmed_subjective_response_rule}` under `{anchored_question_and_conditions}`,
  with `{reasons_task_outcomes_and_missing_responses}` retained.
- **Preference comparison:** Compare `{flows}` for `{equivalent_task_context}`
  using `{order_and_exposure_protocol}`; report `{preference_distribution}` separately
  from `{observed_success_errors_and_assistance}`.

Use the illustrative anchored question if there is no response measure and
confirm with the user/stakeholder. Ask the user before turning preference into a release gate.

## Rules of thumb

- Don't infer positive experience from repeated visits or completed tasks;
  required use can coexist with an explicitly disliked interaction.
- Do preserve negative sentiment beside successful task evidence; changing a
  user's answer to agree with the outcome erases the property being evaluated.
- Do ask about the experienced interaction before naming a proposed redesign;
  soliciting approval of the author's solution contaminates the sentiment baseline.
- Don't blend screenshot preference into post-task sentiment; an attractive
  surface may leave the actual interaction disliked for entirely different reasons.
- Do retain the moment and reason attached to a preference, not just its rating;
  changing an unrelated step cannot substantiate the proposed explanation for that preference.

## Verification

Use post-interaction response collection, complaint-to-flow tracing, and comparable
experience trials. Inspect actual exposure, task result, assistance, presentation
order, and whether the question suggests an answer. Preserve neutral and missing
responses without scoring silence as approval. Separate self-reported feeling,
visual judgment, observed behavior, and the author's proposed causal explanation.

## Done checklist

- [ ] Verify respondents actually encountered the interaction being judged.
- [ ] Retain the exact neutral question and its response anchors.
- [ ] Link reported reasons to the relevant interaction moments and candidate changes.
- [ ] Record task results and assistance separately from the subjective response.
- [ ] Preserve negative, neutral, contradictory, and missing responses distinctly.
- [ ] Disclose non-equivalent task conditions or order effects in a comparison.
- [ ] Limit conclusions to the audience and experiences actually examined.

## Failure modes

- Treating compulsory use as proof that the product is liked.
- Discarding a negative response because the user completed the task.
- Asking a leading question about how much better the redesign feels.
- Generalizing a screenshot preference to the whole interaction experience.

## References

- Read [experience-response practices](./references/design-patterns.md) when
  tracing complaints, framing questions, or comparing post-task preferences.
- Read [confirmation-flow example](./references/worked-example.md) when task success
  stays the same but users report different feelings about the interaction.
