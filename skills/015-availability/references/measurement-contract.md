# Availability measurement contract

Use this worksheet to make an availability claim reproducible. Confirm the
service boundary and accounting decisions before using them as acceptance criteria.

## Resolve the boundary

Record the named journey, required result, audience segments, service calendar,
completion deadline, and mandatory dependencies. Ask the user for missing items.
Distinguish an optional recommendation panel from an essential order submission.
Accept a degraded path only when its result still meets the agreed journey contract.

Choose the primary accounting family before selecting a target:

| Family | Denominator | Success evidence | Accounting risk to resolve |
| --- | --- | --- | --- |
| Time | Duration of eligible service intervals | Journey probes classified under the agreed bin rule | Unobserved time between probes and unknown bins |
| Requests | Eligible attempts observed at the agreed ingress | Required result within the agreed deadline | Missing ingress traffic, retries, and audience weighting |

Do not substitute a request success ratio for a time availability ratio. If a
contract requires both, calculate and label them separately.

## Time accounting worksheet

Record `{window_start}`, `{window_end}`, time zone, bin width, probe cadence,
probe locations, sample freshness limit, and the rule for classifying a bin.
Specify what happens when probes disagree or a bin has partial observations.
Use the same calendar and bin rule for comparisons across deployment versions.
Do not infer continuous usability between samples; state that resolution limit.

Partition eligible time into good, bad, and unknown intervals. Merge overlapping
outage intervals before adding durations so the same affected time is not counted
twice. Keep excluded calendar time outside eligible time and show it separately.

Calculate a conservative lower ratio as good / eligible and a possible upper
ratio as (good + unknown) / eligible. These are accounting bounds for the chosen
bin policy, not a statistical confidence interval or proof about unsampled time.
If eligible time is empty, report no eligible observation instead of a ratio.
Show coverage as (good + bad) / eligible alongside either ratio.

Ask the user whether unknown time blocks acceptance or is charged as unavailable.
Do not approve a target because a good / observed-only calculation looks favorable.
If the policy is unresolved, report the bounds and mark attainment unverified.

## Illustrative numeric calculation

Illustrative example only — confirm with the user/stakeholder before adopting
this window or accounting policy. Assume continuous eligible service, no calendar
exclusions, fixed-duration days, and non-overlapping classified intervals:

| Illustrative input | Minutes |
| --- | --- |
| Window: 30 days | 43,200 |
| Good time | 43,140 |
| Bad time | 30 |
| Unknown time | 30 |

Check the partition: 43,140 + 30 + 30 = 43,200 minutes.
Compute these illustrative ratios, rounded to four decimal places:

- Lower: 43,140 / 43,200 = 99.8611%.
- Upper: (43,140 + 30) / 43,200 = 99.9306%.
- Coverage: (43,140 + 30) / 43,200 = 99.9306%.

Upper and coverage coincide here because bad and unknown durations are equal,
but their numerators mean different things. Keep unknown time visible; these are
bin-accounting bounds, not evidence about unsampled interruptions. If comparing
against the illustrative target of 99.9%, confirm with the user/stakeholder:
the lower ratio falls short while the upper exceeds it. Counting unknown time
against attainment fails that illustrative target; an unresolved unknown policy
does not support a pass. Do not select a policy after seeing the favorable bound.

## Request accounting worksheet

Define ingress, request class, business success condition, deadline, cancellations,
client errors, retries, and accepted exclusions. Preserve the initial attempt and
its outcome when retries occur; do not let a successful retry erase the failed
attempt unless the agreed unit is a complete user interaction with retry behavior.
Identify users who cannot reach the measured ingress. Use an external journey
probe for that blind spot rather than assuming missing requests mean no outages.

## Requirement record

- Service and mandatory result: `{journey_and_result}`.
- Audience and service calendar: `{segments_and_calendar}`.
- Metric and unit: `{time_ratio_or_request_ratio}`.
- Eligibility and classification: `{denominator_success_exclusion_unknown_rules}`.
- Target and status: `{proposed_or_confirmed_target}`.
- Window and resolution: `{window_bin_cadence_locations}`.
- Evidence and owner: `{stored_observations_query_revision_service_owner}`.

If no target is supplied, use this illustrative example only: 99.9% good eligible
time over `{stakeholder_chosen_window}`; confirm with the user/stakeholder.
Keep the record proposed until the other fields and that target are confirmed.

## Outage evidence checklist

- [ ] Retain start, end, affected segment, failed journey step, and observation source.
- [ ] Separate dependency failure time from user-visible unavailability time.
- [ ] Retain bins where monitors, clocks, or routes were not producing usable evidence.
- [ ] Review exclusion intervals against the previously accepted calendar.
- [ ] Check that cached success pages do not stand in for completed writes.
- [ ] Show measurement resolution when interpreting brief interruptions.
- [ ] Compare computed results with the target only under the agreed unknown-data policy.

## Anti-pattern catalog

| Pattern | Reject the claim when | Replace it with |
| --- | --- | --- |
| Health-only availability | The probe bypasses a mandatory dependency | A journey probe with a verifiable business outcome |
| Replica counting | All replicas share the outage-producing dependency | A reviewed shared-failure map and a controlled exercise |
| Convenient maintenance | Exclusions were selected after the outage | The pre-agreed calendar plus an exclusion ledger |
| Successful transport | The response omits the required result | A response and state assertion for the journey |
| Silent monitor loss | Missing bins disappear from the denominator | Explicit unknown time, coverage, and acceptance status |
