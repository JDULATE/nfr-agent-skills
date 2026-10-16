---
name: demonstrability
description: >-
  Makes scenarios inspectable when asked "show payment failure", "replay an approval demo", or "let reviewers inspect results". Before routing a showing, Ask the user: inspect behavior or decide requirement acceptance? Not for proving every possible case (see provability) or designing acceptance evidence (see verifiability).
---

# Demonstrability

## Definition and scope

Demonstrability means an intended audience can inspect a claimed capability
through a defined demonstration. Prepare the scenario, visible result, and
replayable setup; distinguish acceptance-method design (`verifiability`) and
arguments covering all modeled cases (`provability`) from what one showing establishes.

## Use when / Don't use when

- Apply when a reviewer needs to see a specific success, refusal, or recovery path.
- Apply when the demo depends on an author's private setup or unexplained screen.
- Route an undecided acceptance method to `verifiability`.
- Route an invariant over every possible input to `provability`; a demo cannot supply it.
- Route consistency across held-condition reruns to `repeatability` when that is the claim.

## Workflow

1. Clarify: Inspect the feature code, existing tests, run instructions, and audience
   docs before choosing a scenario. Identify the capability, audience, and evidence
   they can inspect without author narration. If "show it works" lacks a claimed
   result, then Ask the user whether they want a scenario, acceptance check, or proof.

2. Specify: Write the claim, initial state, inputs, actions, expected visible
   outputs, forbidden effects, audience view, reset procedure, and replay artifact.
   If acceptance detail is missing, then propose labeled illustrative defaults:
   use synthetic state, show the requested result and its contrasting refusal,
   and expose the resulting state; confirm with the user/stakeholder.
   Keep this proposed demonstration record separate from product acceptance.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [demonstration design](./references/design-guide.md)
   when replacing an author-only performance with inspectable evidence.
   If a screen hides the consequential state, then expose a read-only scenario
   receipt or inspection step. If a fake dependency is necessary, then label its
   boundary visibly and keep the real feature path in the scenario.
   If narration supplies the supposed result, then add an observable artifact
   rather than strengthening the narrator's assertion.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Replay from the recorded setup without the author filling in missing
   steps. Check expected outputs and forbidden effects against the scene record.
   If the setup cannot be replayed or the audience cannot inspect the outcome,
   then mark that showing incomplete; retain failures and changed setup details.
   Read [declined-payment example](./references/worked-example.md) when separating
   a demonstrable refusal from an unsupported claim about every payment path.

5. Report: Return the scenario record, audience-visible artifacts, replay result,
   substitutions, and capability boundaries. If only the synthetic route was
   shown, then identify that limit and withhold claims about the live provider.

## Specification patterns

- **Inspectable scenario:** For `{audience}`, demonstrate `{capability_claim}`
  from `{initial_state}` using `{inputs_and_actions}`; expose `{visible_result}`
  and verify absence of `{forbidden_effects}` through `{inspection_artifact}`.
- **Replay:** A reviewer shall reproduce `{scenario}` using `{setup_and_reset}`
  and compare `{observable_outputs}` with `{scenario_expectation}`, while
  `{declared_substitutions}` remain visible in the evidence.

For unspecified presentation limits, propose the illustrative scene record in
Specify and confirm with the user/stakeholder; do not invent an audience time budget.

## Rules of thumb

- Do place the claimed consequence in the audience's view; a button animation
  cannot demonstrate that a declined payment created no charge.
- Do mark a simulated provider on the scene and its receipt; don't let a polished
  screen imply that the real provider participated.
- Do present the triggering action before inspecting its consequence; a preloaded
  final screen cannot demonstrate the claimed action-to-result transition.

## Verification

Use scripted scenario runners, fixture loaders, and read-only state inspection
categories. Start with the supplied synthetic setup and follow the published
actions rather than the author's remembered shortcuts.
Compare screen result, scene identity, state receipt, and dependency mode.
Reject a receipt or screenshot from an earlier scene as evidence of this run.
Run the contrasting refusal as well as the successful path when both are claimed.
Check replay instructions on a fresh scenario instance and capture deviations.
Retain failed showings and missing artifacts rather than editing the recording
into a sequence that never occurred.
Treat an audience's ability to inspect evidence as distinct from their agreement
that the broader product requirement is satisfied.

## Done checklist

- [ ] Tie the shown scene to a named capability and audience.
- [ ] Load and identify the recorded initial state without private manual edits.
- [ ] Execute the actions from the published scene instructions.
- [ ] Compare the visible result with the scene's expected result.
- [ ] Inspect the forbidden side effect through a scene-specific artifact.
- [ ] Identify every simulated boundary in the audience-visible evidence.
- [ ] Replay from reset and record setup or artifact gaps.

## Failure modes

- Demonstrating a static screenshot while claiming an executed state transition.
- Showing the refusal message but hiding a charge created behind it.
- Presenting a simulated response as evidence of live-provider integration.
- Replacing a failed showing with an unrelated successful scene's receipt.

## References

- Read [demonstration design](./references/design-guide.md) when selecting visible
  consequences, substitutions, and replay mechanisms.
- Read [declined-payment example](./references/worked-example.md) when preparing
  an executable scene record with an inspectable refusal and a bounded claim.
