---
name: understandability
description: >-
  Explains a system model when asked "map component duties", "explain state ownership", or "follow service interactions". Before routing comprehension requests, Ask the user: whole-system relationships or one explanation? Not for one unclear explanation (see comprehensibility), reading flow (see readability), or topic breadth (see comprehensiveness).
---
# Understandability

## Definition and scope

Understandability means the intended audience can form a correct mental model of
system purpose, behavior, and relationships. Ground responsibilities, state ownership,
and causal paths in the project; separate interpreting one explanation
(`comprehensibility`), reading representation (`readability`), and topic breadth (`comprehensiveness`).

## Use when / Don't use when

- Apply when maintainers cannot explain how components cooperate, where state
  becomes authoritative, or why a cross-component path produces an observed outcome.
- Route acquisition of task skill to `learnability` and provided instruction to
  `trainability`; a correct model is not proof of practiced task competence.
- Route diagnosing one failing execution to `debuggability` rather than expanding
  a general model into an unrequested incident investigation.

## Workflow

1. Clarify: Read system entrypoint code, state writes/readers, asynchronous paths,
   architecture docs, tests, and decision records before describing the model.
   If source behavior conflicts with the diagram or intended design, then Ask
   the user which is being explained and mark the disagreement instead of inventing agreement.

2. Specify: Choose audience, purpose, representative cross-boundary questions,
   source-backed causal answers, allowed materials, and the model's known limits.
   If the user wants a practical system explanation, then propose this model record:

   ```text
   Illustrative model trial; confirm with the user/stakeholder:
   Audience/scope: documented maintainers and the named system path, not every module.
   Model: purpose, responsibilities, authoritative state, async gaps and failure branches.
   Example probe: 3 causal prediction questions with all required answers correct.
   Source key: entrypoint/state/consumer evidence at the inspected project revision.
   Artifact changes: scoped architecture narrative/diagram plus source-linked scenario table.
   Evidence: source consistency and unaided audience predictions, assessed separately.
   Open items: intended versus actual behavior, audience context, questions and owner.
   ```

   Ask at most three groups about audience and system questions; authoritative
   sources and intended/actual gaps; and allowed context or proposed task changes.
   Proceed to a bounded model sketch without claiming an exhaustive system explanation.
   If no criterion is supplied, then offer the illustrative prediction trial and
   confirm with the user/stakeholder before using it as an audience acceptance gate.

3. Design/Implement: Read [model patterns](./references/design-patterns.md) when
   explaining ownership, asynchronous handoffs, or cause-to-state paths.
   If an acknowledgement precedes the business result, then show that intermediate
   state and who completes it rather than drawing an arrow that implies instant success.
   If a component boundary hides a state decision, then expose the owner and its
   input/output meaning rather than adding more unexplained boxes to the diagram.

4. Verify: Reconcile the model with representative source paths and ask intended
   readers to predict a normal case and a changed/failed handoff without hints.
   If the model yields a wrong prediction, then trace the missing responsibility,
   state distinction, or causal link instead of accepting a complete-looking topic list.

5. Report: Return the model and source links, prediction answers, disputed design
   assumptions, and system paths not covered by the chosen questions.
   If only the author validated the sketch, then report source review separately
   and leave the audience mental-model claim unverified.

## Specification patterns

- **Causal model:** Using `{allowed_system_material}`, `{audience}` shall predict
  `{cross_boundary_outcomes}` under `{scenarios}`, meeting `{confirmed_answer_rule}`
  against `{source_grounded_responsibility_and_state_key}`.
- **State ownership:** The explanation of `{system_path}` shall distinguish
  `{acknowledgement_intermediate_and_completed_states}` and `{authoritative_owners}`,
  verified by `{source_trace_and_audience_counterfactual_answers}`.

The illustrative prediction count scopes a trial, not universal system coverage;
confirm with the user/stakeholder. Ask the user which questions make the model useful.

## Rules of thumb

- Do separate accepted requests from completed business results in the model;
  merging them teaches a false prediction at every asynchronous handoff.
- Do connect each important state change to its actual writer and consumer;
  component names alone cannot explain who makes an outcome authoritative.
- Do include a failure or interrupted edge for the selected path; a success-only
  story can leave readers predicting completion after work never reached its owner.
- Do reconcile narrative and diagram against the same source revision; explaining
  proposed ownership as current behavior produces a coherent but false mental model.
- Don't add every module merely to make the diagram comprehensive; retain the
  boundaries needed for the audience's causal questions instead of hiding them in box count.

## Verification

Use responsibility/state source tracing, diagram/narrative consistency review,
and causal prediction tasks. Check acknowledgement, state persistence, handoff,
completion, and a missing downstream step for the chosen path. Record unaided
answers and incorrect predictions; a well-formed diagram or broad document outline
cannot establish that the intended audience formed the correct system model.

## Done checklist

- [ ] Trace the chosen model's important state transitions to actual owners/readers.
- [ ] Reconcile purpose, narrative, and diagram with the inspected source revision.
- [ ] Distinguish intermediate acknowledgements from completed business outcomes.
- [ ] Test a failed/interrupted handoff against the model's predicted state.
- [ ] Ask cross-boundary prediction questions using the agreed audience/context.
- [ ] Match answers to the reviewed causal key or mark reader evidence unavailable.
- [ ] Retain intended/actual disagreements and unmodeled paths as explicit limits.

## Failure modes

- Drawing a direct success arrow across an asynchronous or unconfirmed handoff.
- Naming every component while leaving state authority and causal relationships implicit.
- Presenting the intended future design as the currently implemented system.
- Treating topic coverage or author fluency as audience mental-model evidence.
- Generalizing a narrow path explanation to all system behavior.

## References

- Read [model patterns](./references/design-patterns.md) when choosing causal scope,
  identifying state authority, or testing predictions across component boundaries.
- Read [queued-report example](./references/worked-example.md) when separating
  accepted work, persisted state, and a completed result in a concrete model.
