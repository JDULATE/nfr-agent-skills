---
name: changeability
description: >-
  Traces one request through decision, delivery, and adoption when tickets say "this ticket is stuck after approval", "merged but not rolled out", or "who needs to hand this change over". Not for changing priorities (see agility) or reducing code-edit effort (see modifiability).
---
# Changeability

## Definition and scope

Changeability means a particular change can pass from request through decision,
delivery, and adoption. Follow that request's handoff and state evidence; separate
reprioritization (`agility`), bounded implementation work (`modifiability`), and
continuing maintenance effort (`maintainability`).

## Use when / Don't use when

- Apply when a requested or approved change stalls between responsible parties
  or deployment is being mistaken for actual adoption.
- Route a changed priority queue to `agility`; request tracking alone cannot
  determine how the delivery process responds to reprioritization.
- Route the implementation diff's scope and effort to `modifiability`.

## Workflow

1. Clarify: Inspect change records, implementation/release code, approval docs,
   rollout configuration, and use evidence before specifying lifecycle progress.
   If adoption is undefined, then Ask the user whether completion means deployed,
   enabled, actually used, or another observable endpoint for the intended audience.

2. Specify: Link request identity to lifecycle states, gate evidence, receiving
   owners, blocker reasons, timing rules, and the target adoption endpoint.
   If the request is to unblock a specific change, then propose this progress card:

   ```text
   Illustrative request record; confirm with the user/stakeholder:
   Identity: named request linked to decision, delivered artifact, and audience.
   Path: requested, decided, implemented, deployed, enabled, adoption evidenced.
   Example handoff bound: owner accepts or records a blocker within 1 working day.
   Clock: ready-for-handoff event and stakeholder working calendar.
   Gates: existing decision authority and release conditions still apply.
   Adoption: named audience performs the changed journey in a controlled check.
   Evidence: transition records, receiver, blockers, artifact identity, use outcome.
   Open items: actual path, calendar, timing, and authority to accept the change.
   ```

   Ask up to three questions: request and blocker; owners and decision gates;
   and what adoption, timing, or proposed states need revision. Begin handoff
   diagnosis with missing decisions visibly pending.
   If a deadline is absent, then offer the illustrative handoff bound and
   confirm with the user/stakeholder; do not present it as a universal approval SLA.

3. Design/Implement: Read [handoff patterns](./references/design-patterns.md) when
   separating state evidence, receiving responsibility, and adoption checks.
   If no receiver owns the next step, then propose that owner decision and its
   ready evidence; a sent notification cannot establish an accepted handoff.
   If deployment occurred without audience use, then inspect enablement and
   adoption conditions separately instead of closing the request as delivered-to-use.

4. Verify: Follow a synthetic or inspected request through the declared states,
   exercising a blocked handoff, delivered artifact, and adoption endpoint.
   If a gate has no decision evidence, then leave it pending rather than inferring
   approval from later activity or the agent's ability to modify code.

5. Report: Return reached states with their evidence, remaining blockers/owners,
   handoff timing, and the observed audience result.
   If a request was abandoned or replaced, then preserve that terminal meaning
   instead of counting it as adopted to improve completion figures.

## Specification patterns

- **Handoff:** Once `{request}` meets `{ready_evidence}`, `{receiving_owner}` shall
  accept responsibility or record `{blocked_reason}` within `{confirmed_bound}`
  from `{handoff_event}` under `{elapsed_time_rule}`.
- **Adoption:** `{change_identity}` shall reach `{adoption_endpoint}` for
  `{target_audience}`, verified by `{artifact_to_use_trace}` after `{required_gates}`.

The illustrative handoff bound is a starting proposal;
confirm with the user/stakeholder. Ask the user which states and decision owners apply.

## Rules of thumb

- Do bind reached lifecycle states to the same accepted behavior decision; a later
  artifact with different behavior leaves this request's path incomplete despite its links.
- Do distinguish ready, offered, and accepted handoffs; the sender's timestamp
  cannot establish that the receiving owner can progress the request.
- Do separate implemented, deployed, enabled, and adopted where they differ;
  collapsing these states hides the lifecycle bottleneck this skill evaluates.
- Do retain blocked and rejected outcomes; labeling them complete makes a
  request path look traversable without the decision required to advance it.
- Do test the target audience's changed journey; an operator seeing deployment
  success cannot establish that the audience crossed the adoption endpoint.
- Don't backfill earlier approval from a later state; missing decision evidence
  leaves the request's path unverified even when the artifact happens to run.

## Verification

Use lifecycle-state review, artifact lineage inspection, and audience journey
checks. Exercise a refused handoff and a delivered-but-disabled artifact.
Compare the accepting decision with released behavior; inspect dwell times and
blocker reasons rather than closed-request totals. Use retained process records
and controlled audience checks, not unauthorized messages or self-issued approvals,
to determine whether the declared transitions have evidence.

## Done checklist

- [ ] Reconcile request, decision, artifact, and use evidence to the same change.
- [ ] Check each claimed gate against its actual authority and decision evidence.
- [ ] Exercise a handoff offered but not accepted by the receiver.
- [ ] Recompute waiting from the agreed start event and working calendar.
- [ ] Distinguish deployed from enabled with a disabled-delivery fixture.
- [ ] Exercise the changed journey as its intended audience at the adoption endpoint.
- [ ] Retain rejected/replaced/abandoned outcomes without calling them adopted.

## Failure modes

- Closing at implementation merge although audience adoption remains blocked.
- Treating a handoff notification as accepted responsibility.
- Using deployment-admin access as target-audience adoption evidence.
- Inferring approval because downstream implementation work already happened.
- Reporting abandoned requests as successful lifecycle completion.

## References

- Read [handoff patterns](./references/design-patterns.md) when defining receivers,
  state evidence, blocked work, or audience adoption.
- Read [approved-change example](./references/worked-example.md) when diagnosing
  a deployed change its intended audience still cannot use.
