---
name: survivability
description: >-
  Preserves essential mission work when asked "dispatch after site loss", "operate without central login", or "reconcile offline assignments". Ask the user if essential continuity vs restoration is unclear. Not for normal restoration (see recoverability), routine fault handling (see fault-failure-tolerance), or uptime accounting (see availability).
---
# Survivability

## Definition and scope

Survivability means explicitly selected essential mission functions persist
through a severe, scoped disruption. Define minimum mission results and permitted
degradation under lost normal resources; distinguish routine fault service
(`fault-failure-tolerance`), restoration afterward (`recoverability`), and normal
all-journey usable-time accounting (`availability`).

## Use when / Don't use when

- Apply when severe disruption can remove multiple normal dependencies yet a
  prioritized subset of mission work must continue during that disruption.
- Route a routine isolated component-fault contract to `fault-failure-tolerance`.
- Route returning normal service after admitted interruption to `recoverability`;
  a successful later restore cannot prove the mission persisted during the event.

## Workflow

1. Clarify: Read mission-path code, dependency/config maps, continuity docs,
   authority/state rules, and severe-disruption scenarios before choosing a mode.
   If essential functions or severe scope are unspecified, then Ask the user;
   do not assume every normal feature is essential or that any fallback is acceptable.

2. Specify: Record mission priority, essential results, disruption boundary,
   remaining resources, authority/data limits, duration, degradation, and handback.
   If the request is practical continuity work, then offer this mission record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Mission: stakeholder-selected essential result; normal optional work may be unavailable.
   Disruption: stated severe loss plus shared control/data/operator dependencies.
   Remaining mode: discovered alternate/manual/offline path, with its actual constraints.
   Trial horizon: preserve the agreed minimum mission result through 30 minutes of disruption.
   Authority/state: confirmed permitted decisions, stale-data use, identity and duplicate rules.
   Evidence: disrupted-dependency trace, essential results during exposure, deferred-work ledger.
   Handback: reconcile deferred/conflicting work before silently returning to normal authority.
   Status: proposed scope; no permission to bypass mission, data, or harm constraints.
   ```

   Ask at most three groups about essential mission/results; disruption, surviving
   resources and duration; and permitted degradation, authority, or handback constraints.
   Continue to a mission-path design without claiming an unverified alternate survives.
   If no duration is supplied, then propose the illustrative mission trial and
   confirm with the user/stakeholder before treating its horizon as sufficient.

3. Design/Implement: Read [essential-mission practices](./references/design-patterns.md)
   when separating optional work, building an alternate, or reconciling handback.
   If the alternate relies on the lost identity, routing, data, or control service,
   then revise the disruption path; physical distance or a manual label cannot supply independence.
   If degraded authority or stale information changes mission consequences, then
   obtain the confirmed constraint before enabling that decision in the alternate mode.

4. Verify: Hold the declared disruption while exercising essential results with
   only the stated surviving resources, then inspect handback state and work.
   If success relies on a normal dependency outside the surviving-resource record,
   then expose that dependency and leave the mission-continuity claim unsupported.

5. Report: Return essential/deferred functions, lost and surviving resources,
   exposure results, authority limits, deferred-work reconciliation, and unsupported cases.
   If the mission stops until normal service returns, then report the gap;
   successful restoration does not retroactively establish persistence through disruption.

## Specification patterns

- **Essential persistence:** During `{severe_disruption_and_horizon}`, preserve
  `{essential_mission_results}` using `{surviving_resources}` under
  `{confirmed_degradation_and_authority_limits}`, verified by `{during_event_result_trace}`.
- **Handback:** Before `{normal_authority_resumption}`, reconcile `{deferred_or_conflicting_work}`
  under `{confirmed_identity_and_effect_rules}`, preserving `{mission_state_constraints}`
  as verified by `{disruption_to_handback_scenario}`.

Use the illustrative mission horizon when no duration exists; confirm with the
user/stakeholder. Ask the user which minimum results and authority remain acceptable during the event.

## Rules of thumb

- Do prioritize the essential result explicitly before dropping normal features;
  preserving a convenient subset is not evidence that the stakeholder's mission survived.
- Don't count a standby path as surviving if it still needs a lost control or
  identity service; the severe-disruption boundary includes those dependencies too.
- Do exercise essential decisions with the degraded data and authority actually
  available; borrowing normal permissions or fresh data can fabricate mission continuity.
- Don't replace during-disruption result evidence with an eventual normal restore;
  a recovered system may conceal an interval in which the essential mission stopped.
- Do reconcile alternate-mode work before handing authority back; unresolved
  duplicate or conflicting mission actions can invalidate the result preserved during disruption.
- Do retain nonessential losses separately from essential-result failures;
  requiring every normal feature confuses the scoped survival contract with ordinary availability.

## Verification

Use controlled severe-disruption exercises, essential-path dependency inspection,
and alternate-to-normal reconciliation categories. Record lost resources,
remaining operators/data/authority, essential outputs, deferred work, and handback.
Exercise the entire horizon under its scoped constraints. Verify mission result
semantics as well as process survival; a standby heartbeat or later recovery report alone is insufficient.

## Done checklist

- [ ] Confirm essential results and distinguish deferred/nonessential functions.
- [ ] Map the severe disruption and surviving resources, including control and identity.
- [ ] Check the alternate path against every lost mandatory dependency.
- [ ] Validate degraded data, decisions, authority, and permitted result constraints.
- [ ] Observe essential outputs during the held disruption and agreed horizon.
- [ ] Retain deferred/conflicting work with stable identity and effect evidence.
- [ ] Verify handback reconciles work before normal authority silently resumes.
- [ ] Report essential failures separately from nonessential losses and restoration results.

## Failure modes

- Choosing an easy fallback function instead of the essential mission result.
- Using a remote standby that shares the disrupted control or identity dependency.
- Assuming manual/offline operation may bypass normal harm or authority constraints.
- Claiming survival because the system eventually returned after the mission stopped.
- Losing or duplicating alternate-mode work when normal operation resumes.
- Demanding every ordinary feature and obscuring the agreed minimum mission scope.

## References

- Read [essential-mission practices](./references/design-patterns.md) when choosing
  priorities, verifying alternate independence, or planning constrained handback.
- Read [site-loss dispatch example](./references/worked-example.md) when proving
  an essential result during disruption without importing normal dependencies.
