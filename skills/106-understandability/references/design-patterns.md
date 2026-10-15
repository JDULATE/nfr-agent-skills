# Source-grounded system model patterns

Model the path needed for the audience's questions. Distinguish an explanation
of implemented behavior from a proposed design before drawing responsibilities.

## Responsibility and state-authority map

- **Use when:** Readers know component names but cannot explain who changes a
  business state or which component's record makes that state authoritative.
- **Trade-off:** Listing every module can hide the relevant owner; excessive
  abstraction can omit the very writer/reader distinction needed for a prediction.
- **How to verify:** Trace selected state writes and reads in source, reconcile
  diagram/narrative responsibility, and ask which component makes the outcome true.

## Explicit asynchronous/intermediate states

- **Use when:** An accepted request, queued work, persisted result, and user-visible
  completion occur at different points. Show each distinction relevant to the task.
- **Trade-off:** More states cost explanation; collapsing them can falsely imply
  that an acknowledgement proves the business result already exists.
- **How to verify:** Walk the normal path and an interrupted handoff, predicting
  what state exists, what is absent, and what the reader can legitimately conclude.

## Causal prediction rather than box recognition

- **Use when:** A system explanation claims readers understand relationships.
  Choose scenarios that require reasoning across owners, not recalling names.
- **Trade-off:** A narrow prediction set cannot prove a complete model of the system;
  harder questions may require domain context the intended audience was never given.
- **How to verify:** Supply agreed material and fresh cases without hints, retain
  answers against the source-grounded key, and identify the missing causal link.

An illustrative trial asks 3 causal questions with required answers correct;
confirm with the user/stakeholder. Ask the user which audience, material, states,
and failure paths make that trial meaningful. Source consistency and audience
prediction evidence remain separate; author fluency establishes neither by itself.
