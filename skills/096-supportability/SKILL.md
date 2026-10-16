---
name: supportability
description: >-
  Equips support investigation when asked "prepare safe diagnostics", "give support evidence", or "resolve an export case". Ask the user: support investigation or implementation upkeep? Not for recurring upkeep (see maintainability), state inference alone (see observability), or delivery handoffs (see changeability).
---
# Supportability

## Definition and scope

Supportability means a support provider can investigate and resolve a user's issue
using available artifacts and procedures. Build a case-specific evidence-to-action
path; separate ongoing code upkeep (`maintainability`), runtime inference alone
(`observability`), and a release request's progress (`changeability`).

## Use when / Don't use when

- Apply when support cannot connect a reported symptom to the right revision,
  permitted diagnostic evidence, reproducible conditions, or a verified next action.
- Route localizing one failing execution alone to `debuggability`; it may support
  the case but does not establish that the support provider can resolve it.
- Route adding generic telemetry to `observability`; require a named case question
  before treating extra logs as an improved support path.

## Workflow

1. Clarify: Read diagnostic code, error handling, support/runbook docs, release
   identity, case evidence, and the support actor's available access before specifying.
   If the reported issue is actually a pending approval for a feature change, then
   route its handoff to `changeability` rather than inventing a support diagnosis.

2. Specify: Record symptom, affected actor/context, artifact revision, permitted
   collection, decision tree, resolution oracle, escalation limits, and evidence owner.
   If the user wants a practical support improvement, then propose this case record:

   ```text
   Illustrative support path; confirm with the user/stakeholder:
   Example scope: 1 synthetic case bundle tied to a symptom, actor context, and revision.
   Contents: only stakeholder-approved diagnostic fields; unresolved data scope stays open.
   Decisions: each finding maps to an existing verified remedy or a stated escalation gap.
   Resolution: affected-actor journey produces the agreed result after the action.
   Repo changes: scoped diagnostic utility, error mapping, runbook branch, and case tests.
   Limits: no broad access grant, external contact, or production remedy implied.
   Open items: permitted evidence, remedy authority, actual case outcome and support owner.
   ```

   Ask at most three questions: symptom and affected context; evidence/access and
   remedy authority; and what successful resolution or escalation must demonstrate.
   Proceed using synthetic inputs where collection permission or case data is unknown.
   If no scope is supplied, then offer the illustrative case-bundle trial and confirm
   with the user/stakeholder; obtain any time objective separately rather than inventing one.

3. Design/Implement: Read [support patterns](./references/design-patterns.md) when
   designing bundle fields, diagnostic branches, or remedy/escalation evidence.
   If a code or runbook change enables a support decision, then test the symptom,
   artifact output, and resulting action together rather than adding context-free logs.
   If the support actor lacks evidence or remedy authority, then report the exact
   escalation gap and proposed handoff contents without granting access or contacting others.

4. Verify: Reproduce the synthetic case as the affected actor, run collection under
   the support actor's declared access, and check the chosen action against its oracle.
   If only an administrator can reproduce or resolve it, then leave the intended
   support path unverified and expose the missing prerequisite.

5. Report: Return symptom-to-evidence reasoning, bundle/revision, permitted action,
   affected-actor result, and unresolved escalation needs.
   If a remedy was proposed but not executed, then distinguish diagnosis from
   resolution; a case status change cannot replace the user's successful journey.

## Specification patterns

- **Investigation:** For `{case_class}`, `{support_actor}` shall distinguish
  `{decision_branches}` using `{permitted_artifacts}` under `{available_access}`,
  verified by `{symptom_bundle_and_branch_fixtures}` at `{recorded_revision}`.
- **Resolution:** Applying `{authorized_remedy}` under `{case_preconditions}` shall
  restore `{affected_actor_result}`, checked by `{before_after_journey}`; unresolved
  `{authority_or_evidence_gap}` shall yield `{accepted_escalation_record}`.

The illustrative case count is not a response-time commitment;
confirm with the user/stakeholder. Ask the user what evidence and actions are authorized.

## Rules of thumb

- Do bind a diagnostic bundle to the reported case's revision and actor context;
  explaining a current build under admin access can misresolve an older customer symptom.
- Do collect fields that distinguish a runbook decision; a larger bundle with no
  action-bearing difference increases collection without making that case resolvable.
- Do test each remedy's case preconditions; a generic retry or reset can hide the
  symptom while leaving the reported user's underlying outcome unresolved.
- Do verify resolution through the affected actor's journey; an operator-only
  success cannot close a case whose user still cannot complete the task.
- Do retain the minimum missing evidence and authority in an escalation proposal;
  forwarding an unexplained log dump does not establish a usable next support action.
- Don't label a new log statement a support improvement until the case decision
  and permitted action can be followed from it by the declared support provider.

## Verification

Use synthetic support-case replay, diagnostic artifact checks, runbook decision
coverage, and affected-context acceptance tests. Include stale revision, insufficient
access, misleading symptom, failed remedy, and unresolved authority cases.
Inspect unresolved-case reasons and unusable bundles rather than case closure totals.
Check permitted versus excluded fields with synthetic markers; output collection
must follow the supplied data boundary, not assumptions about what support may see.

## Done checklist

- [ ] Reproduce the symptom under the affected actor/context and recorded revision.
- [ ] Generate the declared bundle using only the support actor's permitted evidence.
- [ ] Exclude forbidden synthetic fields under the confirmed collection boundary.
- [ ] Distinguish the agreed decision branches from actual bundle contents.
- [ ] Reject a remedy when its case preconditions do not match.
- [ ] Verify the affected user's result after a permitted remedy or label it unexecuted.
- [ ] Check an unresolved branch produces actionable missing-evidence/authority contents.

## Failure modes

- Diagnosing a different revision or privileged context than the reported case.
- Collecting a large bundle that cannot select a runbook decision.
- Closing a case after an operator action without checking the user's required result.
- Treating missing remedy authority as permission to expand the support role.
- Reporting a proposed workaround as an executed resolution.

## References

- Read [support patterns](./references/design-patterns.md) when connecting a case
  symptom to diagnostic code, runbook decisions, permitted remedies, or escalation.
- Read [export case example](./references/worked-example.md) when testing concrete
  evidence, actor context, and a resolution oracle rather than ticket-status changes.
