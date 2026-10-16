---
name: atomicity
description: >-
  Specifies all-or-none visible effects when tickets say "we see half an update", "a failed write leaves partial changes", or "rollback happens after users saw the change". Not for preserving acknowledged writes (see durability), restoring service (see recoverability), or agreement between values (see consistency).
---
# Atomicity

## Definition and scope

Atomicity means a defined operation exposes its state changes together or exposes
none of them. Bound participating effects and observation points; distinguish
preservation after acknowledgement (`durability`), agreement across representations
(`consistency`), and reconstruction after disruption (`recoverability`).

## Use when / Don't use when

- Apply when cancellation, a failed write, or concurrent observation can reveal
  only some effects of a logical operation that must be accepted as a whole.
- Route acknowledged data disappearing after later events to `durability`.
- Route eventual reconciliation across independent representations to `consistency`;
  later agreement does not itself satisfy a simultaneous all-or-none visibility contract.

## Workflow

1. Clarify: Read mutation code, transaction boundaries, observer queries, external
   effects, and operation docs before choosing an all-or-none mechanism.
   If effects span independently committing systems, then Ask the user which
   effects must be jointly visible and which must instead use a separate contract.

2. Specify: Record operation identity, participating effects, initial/final states,
   observers, visibility boundary, abort behavior, and ambiguous completion handling.
   If the user requests a partial-update fix, then propose this operation record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Unit: requested logical operation and explicitly listed state changes.
   Observer: normal authorized read path, with its actual snapshot/visibility semantics.
   Allowed views: complete pre-operation or complete post-operation state.
   Trial gate: 0 partial participating-effect views in the agreed interruption scenarios.
   Abort: no committed subset; private intermediate work is not published as success.
   External effects: separate boundary unless actual coordinated visibility is established.
   Unknown completion: inspect operation identity/result before retrying or reporting failure.
   Evidence: write/commit trace, observer snapshots, abort outcomes, and side-effect ledger.
   Status: proposed boundary, not proof supplied by a transaction or rollback label.
   ```

   Ask at most three groups about effects/observers; commit, abort and external
   boundaries; and concurrency, interruption or retry semantics. Continue to a
   bounded design while unresolved participation choices remain explicit.
   If no acceptance target exists, then offer the illustrative partial-view gate
   and confirm with the user/stakeholder before adopting its scenario scope.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [visibility-boundary practices](./references/design-patterns.md)
   when locating commit scope, publication, or irreversible side effects.
   If observers can read between separately committed effects, then change the
   actual publication/commit boundary rather than merely wrapping calls in one function.
   If compensation occurs after an effect became visible, then disclose that
   history; compensation cannot erase the earlier partial view from this contract.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Interrupt before, between, and after participating changes while
   reading through the agreed observer path and inspecting final committed state.
   If the observer assembles its view from different moments, then distinguish
   that read artifact from a stored partial commit and resolve the observer contract.

5. Report: Return the participating-effect boundary, implementation changes,
   allowed/forbidden observations, ambiguous outcomes, and excluded effects.
   If only the final state was checked, then leave intermediate visibility unverified;
   eventual cleanup does not establish all-or-none exposure during the operation.

## Specification patterns

- **Visible unit:** For `{operation}`, `{observer}` shall see only `{complete_before}`
  or `{complete_after}` for `{participating_effects}`, verified under
  `{interruption_and_concurrency_scenarios}` using `{coherent_observation_rule}`.
- **Abort:** When `{failure_or_cancellation}` prevents `{commit_condition}`, expose
  `{no_committed_subset}` and resolve `{operation_identity_and_unknown_result}`
  under `{confirmed_abort_and_retry_contract}`, verified by `{effect_and_snapshot_checks}`.

Use the illustrative partial-view gate when a target is missing; confirm with
the user/stakeholder. Ask the user to settle boundary and observer semantics before accepting it.

## Rules of thumb

- Don't count later compensation as all-or-none visibility; an observer that saw
  the partial effect already defeats that operation's visibility contract.
- Do inspect the observer's read boundary as well as the writes; assembling
  separate-time reads can mimic a partial view even when the commit is indivisible.
- Do separate irreversible external publication from private intermediate work;
  a rolled-back local write does not retract an already observed external effect.
- Don't infer atomicity from an all-success path; interruption between effects
  is exactly where the forbidden subset can become visible.
- Do publish the operation result only at its real visibility boundary; returning
  success after an early participating write invites observers to accept a partial unit.
- Do resolve an unknown commit outcome before replaying the operation; a lost
  acknowledgement is not evidence that no participating effects committed.

## Verification

Use interruption injection, concurrent-observer integration, and committed-state
inspection categories. Trace each participating effect, commit/publication point,
abort and observer read. Exercise error, cancellation, lost response, and boundary
reads with the declared coherence rule. Inspect external effects separately;
a successful rollback message or final corrected state cannot prove the earlier views.

## Done checklist

- [ ] Enumerate participating effects and explicit external-boundary exclusions.
- [ ] Define complete before/after views through a coherent authorized observer.
- [ ] Inspect the actual commit/publication boundary across participating changes.
- [ ] Interrupt between changes and retain observer snapshots and committed state.
- [ ] Verify abort exposes no committed subset under the declared contract.
- [ ] Resolve unknown completion before accepting retry or failure classification.
- [ ] Distinguish private intermediate state, read artifacts, and visible partial effects.

## Failure modes

- Grouping calls in a function while each effect still commits independently.
- Calling later compensation proof that no partial effect was observed.
- Testing only final state and missing an earlier forbidden view.
- Assuming a local transaction covers an independently published external effect.
- Treating a lost success response as proof that the operation aborted.

## References

- Read [visibility-boundary practices](./references/design-patterns.md) when choosing
  commit scope, observation rules, or an external-effect boundary.
- Read [assignment example](./references/worked-example.md) when distinguishing
  partial committed effects from a mixed-time reader artifact.
