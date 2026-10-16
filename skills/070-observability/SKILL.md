---
name: observability
description: >-
  Makes runtime state inferable when tickets say "is this job queued or stuck", "we cannot join the retry to its first attempt", or "the logs do not explain the missing result". Not for displaying status alone (see visibility), defining units (see measurability), or one defect replay (see debuggability).
---

# Observability

## Definition and scope

Observability means runtime evidence lets an operator infer relevant internal
state and explain the observed behavior. Choose signals that distinguish the
states in question; separate exposing status (`visibility`), defining a measure
(`measurability`), and replaying one defect (`debuggability`) from inference
about the running system.

## Use when / Don't use when

- Apply when operators cannot tell whether work is queued, owned, or blocked.
- Apply when retries cannot be connected to their original logical work.
- Route showing a known status to an audience to `visibility`.
- Route deciding measurement units and collection semantics to `measurability`.
- Route expression-level inspection of a particular failure to `debuggability`.

## Workflow

1. Clarify: Read job and request lifecycles, asynchronous boundaries, current
   signals, collection paths, and incident questions before adding instrumentation.
   Identify the hidden states and the decision an operator needs to make.
   If the request is only "more logs", then Ask the user which states or explanations
   the current evidence cannot distinguish.

2. Specify: Record the inference question, candidate states, signal meanings,
   correlation identity, ownership boundaries, collection gaps, and validation fixture.
   If no diagnostic contract exists, then propose labeled illustrative defaults:
   distinguish queued, claimed, dependency-waiting, and committed states for the
   requested path, with logical-job and attempt linkage; confirm with the user/stakeholder.
   Keep retention, field exposure, and collection cost within existing policy.

3. Design/Implement: Read [runtime inference design](./references/design-guide.md)
   when choosing semantic lifecycle events, attempt links, or handoff evidence.
   If enqueue acknowledgment is labeled done, then instrument the actual result
   boundary separately. If an asynchronous handoff loses identity, then propagate
   the minimum correlation context. If identical signals fit several hidden states,
   then add a discriminator instead of increasing duplicate message volume.

4. Verify: Exercise known queued, claimed, waiting, failed-attempt, retry, and
   committed fixture states. Infer state from collected signals without reading
   the hidden fixture oracle until the inference is recorded.
   If signals are missing or inconsistent, then report unknown or competing
   explanations; preserve collection loss and incomplete work.
   Read [job inference example](./references/worked-example.md) when validating
   state discrimination and retry lineage without inventing a root cause.

5. Report: Return the inference questions, added signals, reconstructed lifecycle,
   ambiguous intervals, and collection/privacy costs.
   If telemetry supports only a state distinction, then do not promote it to an
   untested explanation of why the dependency entered that state.

## Specification patterns

- **State discrimination:** For `{runtime_path}`, collected evidence shall let
  `{operator}` distinguish `{named_hidden_states}` using
  `{semantic_signals_and_identity}`, validated against `{known_state_fixture}`.
- **Handoff:** Across `{asynchronous_boundary}`, retain
  `{logical_work_attempt_and_parent_identity}` and `{ownership_transition}`
  sufficient to reconstruct `{retry_or_handoff_question}`.
- **Ambiguity:** When `{required_evidence}` is unavailable, inference shall return
  `{unknown_or_candidate_set}` instead of `{unsupported_state_claim}`.

For absent numeric targets, use the illustrative state-discrimination proposal
in Specify and confirm with the user/stakeholder; do not invent a telemetry-volume target.

## Rules of thumb

- Do select signals that distinguish the named hidden states; many identical
  "working" messages cannot separate queued work from a blocked owner.
- Do preserve logical-job identity alongside distinct attempt and parent identities;
  overwriting the attempt id can make a retry look like unrelated new work.
- Do place ownership evidence on both sides of an asynchronous handoff; a producer's
  enqueue success does not identify the worker currently responsible.

## Verification

Use lifecycle instrumentation review, trace reconstruction, controlled dependency
responses, and collection-failure checks.
Compare inferred states with the fixture's known state after recording the inference.
Check that completion signals occur at the required result boundary rather than
at request acceptance; inspect the actual committed output before inferring completion.
Test a failed attempt followed by a retry so identity survives without merging attempts.
Remove a handoff event and inspect whether the result becomes ambiguous.
Check collection coverage before calling a last-observed state current; an event
establishes a state at its boundary, not that the state persists until inspection.
Record sample loss, filtering, raw events, unfinished paths, and timing/clock limits
rather than filling gaps with successful states.
Review signal cardinality, retention, and personal-data fields under existing policy.
A diagnostic view must expose what the evidence supports, including uncertainty.

## Done checklist

- [ ] Name the hidden states and operator decision.
- [ ] Define lifecycle signal meanings at actual code boundaries.
- [ ] Link logical work, attempts, and retry parentage.
- [ ] Expose ownership across the asynchronous handoff.
- [ ] Distinguish known fixture states from the collected evidence.
- [ ] Produce uncertainty when required signals are removed.
- [ ] Review collection loss, field exposure, and retention.
- [ ] Separate inferred state from untested causal explanations.

## Failure modes

- Adding more messages without distinguishing the competing hidden states.
- Calling enqueue success completion while the output is absent.
- Replacing attempt identity on retry and losing the original path.
- Treating a missing event as evidence that the operation succeeded.
- Inferring a dependency's root cause from a single waiting-state signal.

## References

- Read [runtime inference design](./references/design-guide.md) when choosing
  lifecycle semantics, ownership signals, and retry correlation.
- Read [job inference example](./references/worked-example.md) when checking
  whether collected signals distinguish known states and expose missing evidence.
