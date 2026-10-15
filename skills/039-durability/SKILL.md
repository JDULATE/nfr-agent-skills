---
name: durability
description: >-
  Preserves acknowledged state across explicitly named subsequent events when users say "do not lose a confirmed save after restart", "verify committed writes survive storage failure", or "check what our success acknowledgement really preserves". Connects acknowledgement, retained versions, and post-event read evidence. Not for all-or-none visibility (see atomicity), reconstructing usable service (see recoverability), or continuous service during failure (see fault-failure-tolerance).
---
# Durability

## Definition and scope

Durability means an acknowledged state change remains preserved through the
specified subsequent events. Bind the acknowledgement promise to actual state
versions and persistence boundaries; distinguish all-or-none visibility (`atomicity`)
and reconstructing usable service after loss or interruption (`recoverability`).

## Use when / Don't use when

- Apply when confirmed saves disappear after restart, failover, or another named
  event, or when a success response promises more persistence than its write path provides.
- Route partial-operation visibility to `atomicity`.
- Route broader restore time and recovered-service correctness to `recoverability`;
  a backup's existence alone establishes neither property.

## Workflow

1. Clarify: Read acknowledgement-producing code, write/flush/replication paths,
   storage config, state-version docs, and loss incidents before choosing a promise.
   If acknowledgement means only queued or accepted work, then distinguish it
   from the user's claimed durable commit and Ask the user which promise is required.

2. Specify: Name acknowledged unit/version, promise point, event model, retained
   state oracle, legitimate supersession, persistence dependencies, and evidence.
   If the request is a confirmed-save fix, then propose this preservation record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Unit: acknowledged change plus identity/version and its defined business contents.
   Promise: existing documented completion acknowledgement; actual persistence point unverified.
   Trial event: process restart after observed acknowledgement, with storage assumptions explicit.
   Trial gate: 0 missing acknowledged versions in the agreed event/retrieval checks.
   Supersession: approved later change is distinguished from lost earlier persistence.
   Read evidence: post-event authoritative retrieval; bypass unverified warm-process evidence.
   Limits: no device/site-loss claim inferred from a process-restart exercise.
   Status: proposed event-scoped preservation contract, not a property of a storage label.
   ```

   Ask at most three groups about acknowledgement/content; subsequent events
   and persistence assumptions; and supersession, loss and retrieval requirements.
   Continue to a persistence-path design while the actual promise remains proposed.
   If no loss criterion exists, then offer the illustrative missing-version gate
   and confirm with the user/stakeholder before adopting the event scope.

3. Design/Implement: Read [acknowledged-state practices](./references/design-patterns.md)
   when aligning the response, persistence boundary, and post-event retrieval.
   If success precedes the required persistence condition, then align the promise
   or the write path with the confirmed contract instead of relying on response wording.
   If replicas or backups share the modeled loss dependency, then expose that
   limitation rather than declaring the acknowledged change protected by copy count.

4. Verify: Record acknowledged identities/contents outside the component under
   test, trigger the scoped event, and retrieve state through the agreed authority.
   If the event also destroys the reference ledger, then use an independently
   retained oracle; missing expected-state evidence cannot certify preservation.

5. Report: Deliver the acknowledgement contract, changed persistence path,
   post-event comparisons, legitimate supersessions, losses, and excluded events.
   If only a clean read before restart succeeded, then leave post-event preservation
   unverified; do not infer durability from immediate visibility or fast response.

## Specification patterns

- **Acknowledged preservation:** After `{acknowledgement_point}`, preserve
  `{state_identity_version_and_contents}` through `{event_model}` under
  `{storage_and_copy_assumptions}`, verified by `{post_event_authoritative_comparison}`.
- **Promise alignment:** Emit `{completion_acknowledgement}` only after
  `{confirmed_persistence_condition}`, verified by `{write_ack_event_trace}`
  and `{loss_checks_with_supersession_rules}`.

Use the illustrative acknowledged-version trial if no loss target exists;
confirm with the user/stakeholder. Ask the user which loss events the promise actually covers.

## Rules of thumb

- Don't treat immediate read-after-write visibility as post-event preservation;
  the same live process may still be serving state the named failure would remove.
- Do anchor the expected-state ledger to observed acknowledgements, not attempted
  writes; otherwise unaccepted work can be misreported as lost confirmed state.
- Do test the promised event boundary itself; a process restart cannot establish
  preservation across storage destruction when the same storage survives the test.
- Don't count copies without tracing their failure dependencies and commit state;
  unconfirmed or jointly lost copies cannot justify the acknowledged-state promise.
- Do distinguish permitted supersession from missing persistence by identity/version;
  comparing only the latest value can incorrectly call a legitimate later change data loss.
- Do inspect acknowledgement ordering against the persistence condition; adding
  a backup later does not fix a success promise already sent before its required boundary.

## Verification

Use write/acknowledgement tracing, event-scoped restart/loss rehearsal, and
state-version comparison categories. Retain expected acknowledged contents,
event timing, actual persistence assumptions, retrieval authority, and supersession
history. Exercise the named event, not a weaker substitute. Report ambiguous
acknowledgements separately; storage brand, replica count, and backup files are not outcome evidence.

## Done checklist

- [ ] Map acknowledged identity/version/contents to the promised persistence point.
- [ ] Retain an expected-state oracle independent of the tested loss boundary.
- [ ] Inspect write, persistence-condition, and acknowledgement ordering.
- [ ] Exercise every event class claimed by the preservation contract.
- [ ] Compare authoritative post-event contents with acknowledged expected versions.
- [ ] Separate legitimate supersession, unacknowledged work, ambiguous responses, and actual loss.
- [ ] Disclose shared copy dependencies and untested storage/site-loss assumptions.

## Failure modes

- Returning confirmed-save success while work remains only in an unverified volatile path.
- Passing a warm read check and claiming survival of a later destructive event.
- Testing process restart while promising storage-loss or site-loss preservation.
- Comparing attempted rather than acknowledged changes and misclassifying loss.
- Treating a valid later update as disappearance of an earlier acknowledged version.

## References

- Read [acknowledged-state practices](./references/design-patterns.md) when mapping
  response promises, persistence dependencies, or a trustworthy loss-test oracle.
- Read [confirmed-document example](./references/worked-example.md) when testing
  preserved content after restart without confusing attempted or superseded versions.
