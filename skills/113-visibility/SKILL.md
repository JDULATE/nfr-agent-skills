---
name: visibility
description: >-
  Exposes status to its intended audience when tickets say "customers cannot see export progress", "show when this job status was updated", or "the status page shows another team's job". Not for inferring hidden causes (see observability), notifying users (see communicativeness), or permission design (see accessibility-access-control).
---

# Visibility

## Definition and scope

Visibility means the intended stakeholder can see the relevant status or progress
at the point where they need it. Expose a subject-scoped view with its observation
context; distinguish diagnosing hidden runtime state (`observability`), sending
timely notifications (`communicativeness`), and deciding permissions
(`accessibility-access-control`) from presenting status under an existing policy.

## Use when / Don't use when

- Apply when customers cannot find their export's current observed status.
- Apply when a status page omits freshness or shows the wrong subject's progress.
- Route inferring why a job is blocked to `observability`.
- Route notification timing or channel design to `communicativeness`.
- Route deciding who may access an object to `accessibility-access-control`;
  apply confirmed access rules here rather than inventing a new policy.

## Workflow

1. Clarify: Read status producers, view queries, ownership checks, projection
   updates, and audience docs before choosing a display.
   Identify stakeholder, subject, workflow point, and the decision the view supports.
   If "show progress" leaves those missing, then Ask the user what status belongs
   to whom and whether a notification or diagnostic explanation is also needed.

2. Specify: Record the subject key, authorized audience, source observation,
   visible states, progress meaning, freshness rule, and unknown/stale presentation.
   If no view contract exists, then propose labeled illustrative defaults:
   show the requested subject's observed state, observation time, and stale/unknown
   marker under existing permissions; confirm with the user/stakeholder.
   Ask the user for a freshness budget if elapsed time determines acceptability.

3. Design/Implement: Read [status projection design](./references/design-guide.md)
   when choosing audience scoping, freshness labels, or state projection.
   If a latest-row query can select another subject, then scope it by verified
   audience and subject identity. If the source is stale, then retain its last
   observation with a stale marker rather than relabeling it current.
   If no source exists, then show unknown rather than an invented starting state.

4. Verify: Open the view for the intended audience with fresh, stale, missing,
   and wrong-subject fixture records. Inspect what is actually visible.
   If the view cannot establish subject or observation context, then keep the
   status claim unresolved. Retain failed queries and missing-source cases.
   Read [export status example](./references/worked-example.md) when checking
   audience scope and freshness without claiming a new authorization policy.

5. Report: Return the visible state mapping, source boundary, audience checks,
   stale/unknown behavior, and unresolved status needs.
   If only status exposure was verified, then do not claim the view explains the
   job's cause or delivers notifications.

## Specification patterns

- **Status access:** At `{workflow_point}`, `{authorized_audience}` shall see
  `{subject_specific_status_and_progress}` from `{source}`, accompanied by
  `{observation_identity_and_time}`.
- **Freshness:** When `{confirmed_freshness_rule}` is not met, the view shall
  present `{stale_or_unknown_state}` and shall not imply `{current_state_claim}`.
- **Scope:** A status read for `{subject}` shall use `{existing_access_policy}`
  and shall not substitute `{other_subject_projection}` when its source is absent.

Use the illustrative status-view proposal in Specify for an unquantified request
and confirm with the user/stakeholder. Do not invent an acceptable freshness duration.

## Rules of thumb

- Do bind the view to the stakeholder's requested subject; the newest job anywhere
  is not a substitute for that subject's status.
- Do show when the state was observed, not merely when the page rendered;
  a fresh page can contain an old observation.
- Do keep the subject's terminal projection across page reloads unless a newer valid
  source revision changes it; rendering must not restart displayed export progress.

## Verification

Use status-query integration, audience-context, projection, and view-state checks.
Verify allowed subject access using the existing confirmed policy and reject
cross-subject fallback paths.
Inspect source observation time, clock comparability, and the stale rule independently
of page rendering time.
Exercise absent, delayed, contradictory, and terminal projections.
Verify missing projections remain visibly unknown instead of becoming apparent
queued or completed jobs.
Check the meaning and denominator of progress counters before displaying them.
Label estimates separately from observed progress; a predicted finish must not
appear as confirmed completed work.
Retain query failures, unfinished work, and missing-source records.
A readable status view does not establish diagnostic causality or notification delivery.

## Done checklist

- [ ] Identify the audience, subject, workflow point, and source.
- [ ] Apply the existing access policy to the status query.
- [ ] Inspect the view's subject identity against the requested subject.
- [ ] Show source observation context rather than render time alone.
- [ ] Exercise fresh, stale, and missing-source presentations.
- [ ] Distinguish observed progress from estimated progress.
- [ ] Check that a missing subject never falls back to another subject.
- [ ] Limit the result to verified status exposure.

## Failure modes

- Returning the latest global job when the requested subject has no record.
- Calling a status current because the page was just rendered.
- Displaying missing projection data as an ordinary queued state.
- Presenting predicted completion as observed progress.
- Claiming a status badge explains the cause of a blocked job.

## References

- Read [status projection design](./references/design-guide.md) when choosing
  scoped queries, source freshness, and explicit unknown presentations.
- Read [export status example](./references/worked-example.md) when checking
  fresh, stale, and wrong-subject cases under a supplied access policy.
