---
name: attractiveness
description: >-
  Judges and improves visual appeal for a stated audience when users say "make this screen more attractive", "compare these visual styles", or "the layout looks uninviting". Uses aesthetic responses under comparable viewing conditions. Not for overall feelings after interaction (see likeability), visual symbol recognition alone (see legibility), or task completion (see usability).
---
# Attractiveness

## Definition and scope

Attractiveness means the visual presentation appeals to its intended audience.
Evaluate appearance in a specified setting; distinguish positive feelings after
interaction (`likeability`), symbol recognition (`legibility`), and successful tasks (`usability`).

## Use when / Don't use when

- Apply to an audience's response to composition, visual rhythm, styling, or imagery.
- Route recognition barriers to `legibility` or `accessibility-access-control`;
  an appealing screen can still exclude its intended users.
- Route complaints about the experience after a task to `likeability` unless
  the user identifies appearance as the acceptance question.

## Workflow

1. Clarify: Inspect existing presentation code, theme assets, design docs, and
   supported viewing contexts before choosing aesthetic changes.
   If the complaint concerns mistakes or unreadable symbols, then separate visual
   appeal from `usability` task checks or `legibility` recognition checks.

2. Specify: Name audience, screen/state, visual question, comparison conditions,
   response method, preservation constraints, and how mixed preferences are reported.
   If the user wants an improvement, then propose this complete trial record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Audience/artifact: requested audience and screen, using synthetic representative content.
   Context: same viewport, state, content, and delivery quality for compared variants.
   Task: view each variant without task interaction; describe visual appeal and reasons.
   Response: anchored 5-point visual-appeal scale, low = unappealing, high = appealing.
   Decision: report response distributions and comments; no winning cutoff is assumed.
   Preservation: same information, controls, brand constraints, and recognition checks.
   Evidence: variant revision, viewing context, presentation order, and response records.
   Status: proposed evaluation, not evidence of audience preference.
   ```

   Ask at most three grouped questions: whose appearance judgments matter;
   which visual/brand and viewing constraints apply; and which comparison or
   acceptance rule should replace the proposal. Proceed to a reversible style draft.
   If the stakeholder supplies no numeric goal, then use the illustrative scale
   and confirm with the user/stakeholder before selecting an acceptance rule.

3. Design/Implement: Read [visual comparison practices](./references/design-patterns.md)
   when choosing variants or reducing presentation confounds.
   If a style change hides distinctions or controls, then restore their function
   before asking viewers to prefer it; do not exchange recognition for decoration.
   If multiple visual dimensions change, then retain a variant ledger rather
   than attributing the response to an individual color or spacing decision.

4. Verify: Inspect rendered variants under the recorded conditions, then collect
   visual judgments separately from task outcomes and post-task sentiment.
   If content or rendering differs between conditions, then disclose that confound
   and withhold a causal claim about styling alone.

5. Report: Show the variants, audience responses, reasons, and functional constraints.
   If only the author judged appearance, then call it a design proposal and leave
   the intended audience's aesthetic response unverified.

## Specification patterns

- **Visual appeal:** For `{audience}` viewing `{screen_state}` under `{conditions}`,
  `{variant}` shall meet `{confirmed_visual_response_rule}` using `{anchored_question}`,
  with `{response_distribution_and_reasons}` retained.
- **Constrained restyling:** Changes to `{visual_dimensions}` shall preserve
  `{information_controls_and_recognition_constraints}`, verified by `{render_review}`
  alongside `{separate_aesthetic_comparison}`.

Use the illustrative response scale above when no measure exists; confirm with the user/stakeholder. Ask the user for the decision rule, rather than inventing taste consensus.

## Rules of thumb

- Do ask about appearance before task interaction when isolating visual appeal;
  a frustrating task otherwise contaminates the aesthetic judgment being accepted.
- Don't infer visual appeal from a contrast or transcription pass; those establish
  recognition evidence, not whether the audience likes the composition.
- Do compare the same populated state for aesthetic choices; empty placeholders
  can make a layout seem attractive while its actual content changes the composition.
- Don't choose a visual winner from completion speed; faster interaction can coexist
  with a less appealing style and answers a different acceptance question.
- Do retain opposing visual preferences by audience/context; averaging away a
  disliked variant's audience is not evidence that its appearance suits them.

## Verification

Use rendered-state inspection, visual comparison, and audience-response review
categories. Inspect populated and empty states for clipping or hidden controls.
Record the exact question, anchors, order, device context, and missing responses.
Review recognition and interaction regressions independently; aesthetic ratings
cannot waive either constraint or establish improved task performance.

## Done checklist

- [ ] Retain comparable rendered content, state, and viewport for each variant.
- [ ] Record which visual dimensions changed in each candidate.
- [ ] Inspect that required controls and information remain present and recognizable.
- [ ] Collect the agreed visual question and its scale anchors without task framing.
- [ ] Report response distribution, missing responses, and conflicting visual preferences.
- [ ] Separate aesthetic evidence from task and general sentiment evidence.

## Failure modes

- Selecting a style from the author's taste and claiming audience validation.
- Comparing an empty mockup with a populated production screen.
- Using a recognition check or faster task time as an aesthetic verdict.
- Hiding disliked audience responses inside a single favorable aggregate.

## References

- Read [visual comparison practices](./references/design-patterns.md) when building
  comparable variants, response prompts, or a preservation review.
- Read [queue-screen example](./references/worked-example.md) when separating
  a visual-style choice from recognition and task-performance evidence.
