---
name: reliability
description: >-
  Specifies and tests failure-free operation over a declared interval and operating profile when users say "stop recurring failures during normal operation", "run this workload without failing", or "check whether retries hide operational failures". Preserves failure occurrence, exposure, and restart history. Not for usable-time ratios (see availability), continued service during injected faults (see fault-failure-tolerance), or restoration procedures (see recoverability).
---
# Reliability

## Definition and scope

Reliability means required behavior continues without failure over the stated
operating interval and conditions. Define what constitutes a failure before
measuring exposure; distinguish how long service is usable (`availability`),
continuation under explicit faults (`fault-failure-tolerance`), and return after
failure (`recoverability`).

## Use when / Don't use when

- Apply when ordinary operation repeatedly violates its required behavior,
  crashes, or appears successful only because retries or restarts hide failure events.
- Route outage duration and service-calendar ratios to `availability`.
- Route controlled rejection of unexpected input to `robustness`; a defined
  valid rejection is not automatically a reliability failure.

## Workflow

1. Clarify: Read execution code, lifecycle/state handling, incident docs, failure
   records, workload definitions, and existing tests before choosing a trial.
   If different sources disagree on required behavior or failure granularity,
   then Ask the user to resolve that boundary before comparing counts.

2. Specify: Choose required behavior, operating profile, trial start/end, failure
   event unit, reset/retry policy, observation coverage, and comparison rule.
   If the user asks to reduce recurring failures, then propose this trial record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scope: requested operation under its documented normal workload and environment.
   Trial: 10 minutes of continuous prescribed operation without a qualifying failure.
   Failure: any violated required result, unexpected process stop, or defined state breach.
   Unit: retain event identity and affected operations; avoid double-counting the same event.
   Retries/resets: retain original failures and restart boundaries; no silent clock reset.
   Coverage: record observation gaps and actual exercised workload, including idle periods.
   Evidence: revision, workload trace, results, failure ledger, exposure, and interruptions.
   Limits: a bounded observed trial, not a production failure probability estimate.
   ```

   Ask at most three groups about required behavior/failure unit; operating
   profile and interval; and allowed retries, resets, observation, and target rules.
   Proceed to a scoped defect investigation or trial design using proposed fields.
   If no target is given, then offer the illustrative continuous trial and confirm
   with the user/stakeholder before using it as the acceptance gate.

3. Design/Implement: Read [failure-occurrence practices](./references/design-patterns.md)
   when changing lifecycle behavior, reproducing repeated defects, or retaining failure evidence.
   If resets conceal a recurring failure, then preserve its event and exposure
   boundary while fixing the cause; a faster restart is a restoration improvement alone.
   If failures emerge only after sustained use, then reproduce the state progression
   rather than repeatedly testing a newly initialized instance.

4. Verify: Run the declared operating profile across the agreed interval, inspect
   required results, and retain failures, restarts, resets, and observation gaps.
   If the run stops early or loses observation, then report incomplete exposure
   rather than a failure-free interval that was never fully observed.

5. Report: Return the changed failure mechanism, operating exposure, event ledger,
   interrupted trials, original/retry outcomes, and remaining profile limitations.
   If no qualifying failure occurred, then state that observation within its scope;
   do not turn the trial into an unsupported future probability or universal guarantee.

## Specification patterns

- **Continuous operation:** Under `{operating_profile}`, `{required_behavior}`
  shall continue over `{confirmed_interval}` with `{confirmed_failure_rule}`,
  verified by `{result_observation_and_failure_ledger}` and `{gap_reset_policy}`.
- **Failure occurrence:** For `{exposure_unit_and_profile}`, record `{qualifying_events}`
  under `{deduplication_and_retry_rules}`, compare with `{confirmed_event_limit}`,
  and retain `{interrupted_or_unobserved_exposure}` separately.

Use the illustrative continuous-operation trial if no interval/criterion exists;
confirm with the user/stakeholder. Ask the user before selecting a statistical model or extrapolation.

## Rules of thumb

- Do keep failure occurrence separate from restoration time; an instant restart
  cannot make the preceding required-behavior violation disappear from the trial.
- Don't reset the failure-free clock without declaring a new trial boundary;
  combining only the surviving tails hides the continuity the interval claim requires.
- Do retain the original attempt's violated result when a retry succeeds unless
  the agreed failure unit is explicitly the complete retried interaction.
- Do drive the declared operational profile during exposure; an idle process
  cannot establish failure-free execution of work that the trial never exercised.
- Do distinguish a permitted rejected input from a failure of required behavior;
  counting every error response can penalize a correctly enforced operating contract.
- Don't generalize a clean bounded run to a future failure probability without
  an agreed model; observed absence is not a universal failure-free guarantee.

## Verification

Use sustained-workload tests, failure reproduction, result-invariant inspection,
and event-ledger review categories. Exercise the state progression implicated
by the defect and compare original/retry outcomes. Correlate workload, process
restarts, result breaches, and observed exposure. Report coverage gaps and ended
trials; a healthy endpoint after a run does not prove the intervening operation.

## Done checklist

- [ ] Resolve the required behavior and qualifying failure/event unit.
- [ ] Retain the exercised workload, environment, revision, and exposure interval.
- [ ] Observe results throughout the trial instead of only checking final health.
- [ ] Preserve original failures, restart/reset boundaries, and retry outcomes.
- [ ] Check event deduplication without erasing separately affected operations.
- [ ] Separate incomplete or unobserved exposure from completed clean intervals.
- [ ] Limit conclusions to the observed profile without unsupported probability claims.

## Failure modes

- Reporting only successful retries while dropping the original violated results.
- Restarting after failure and treating the combined run as uninterrupted.
- Counting idle time as evidence for an operational workload never exercised.
- Defining failure after seeing which response classification looks favorable.
- Extrapolating a short clean trial into a production reliability guarantee.

## References

- Read [failure-occurrence practices](./references/design-patterns.md) when choosing
  event units, exposure accounting, lifecycle fixes, or sustained-state checks.
- Read [repeated-job example](./references/worked-example.md) when a restart and
  successful retry restore service without erasing the earlier reliability failure.
