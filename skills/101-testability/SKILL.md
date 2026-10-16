---
name: testability
description: >-
  Adds test controls when asked "force the timeout branch", "inject a clock", or "observe which test path ran". Ask the user if missing test seams vs one failing replay is unclear. Not for selecting acceptance evidence (see verifiability) or diagnosing a particular failing execution (see debuggability).
---

# Testability

## Definition and scope

Testability means tests can control relevant conditions and observe enough
behavior to distinguish whether the intended path worked. Add practical seams
and outcome access around the real behavior under test; distinguish choosing
acceptance evidence (`verifiability`), diagnosing one failed execution
(`debuggability`), and live operator control (`controllability`).

## Use when / Don't use when

- Apply when tests cannot force a timeout, dependency result, or state boundary.
- Apply when success and failure paths produce indistinguishable test observations.
- Route missing acceptance meaning or evidence selection to `verifiability`.
- Route inspection of a particular execution defect to `debuggability`.
- Route live administrative state-changing controls to `controllability`.

## Workflow

1. Clarify: Read the target branch, callers, test harness, fixtures, dependency
   construction, and existing outcome signals before adding a seam.
   Identify the condition tests cannot control and the states they cannot distinguish.
   If the expected result is undefined, then Ask the user to resolve that requirement
   before building a harness that can only repeat the implementation's assumption.

2. Specify: Record the target path, controlled inputs, observed outputs,
   dependency substitutions, preserved production boundary, and test oracle.
   If no seam contract exists, then propose labeled illustrative defaults:
   inject a clock at dependency construction, script external responses, and
   inspect a semantic result plus its side effect; confirm with the user/stakeholder.
   Keep the real decision logic inside the tested boundary.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [test seam decisions](./references/design-guide.md)
   when choosing a clock seam, response adapter, or outcome observation.
   If a test sleeps to reach a boundary, then expose the time source rather than
   changing the deadline rule. If stubbing replaces the rule under test, then move
   the substitution outward. If observations cannot distinguish two paths, then
   expose a stable semantic outcome instead of private line-by-line execution.
   Do not expose a public bypass simply to make a test easier to drive.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Drive the targeted branches through the same entrypoint using the
   seam; compare expected results and externally relevant effects.
   If a deliberately wrong branch still passes, then improve control or observation
   before claiming the seam makes the behavior testable.
   Read [deadline test example](./references/worked-example.md) when checking
   clock control, branch discrimination, and the unchanged normal dependency path.

5. Report: Return the missing test capability, seam change, controllable scenarios,
   observed outcomes, and integration coverage left outside substitutions.
   If only substituted dependencies were exercised, then report that boundary
   rather than claiming the production integration was verified.

## Specification patterns

- **Control:** Tests for `{behavior}` shall set `{condition_or_dependency_result}`
  through `{construction_time_seam}` while executing `{real_decision_boundary}`,
  without `{sleep_or_live_dependency_requirement}`.
- **Observation:** Tests shall distinguish `{meaningful_outcomes}` using
  `{semantic_result_and_effect_evidence}`, demonstrated by
  `{contrasting_cases_and_deliberately_wrong_branch}`.
- **Production boundary:** Normal construction shall continue to use
  `{production_dependency}`; `{external_inputs}` shall not activate
  `{test_only_override}`.

For absent seam detail, offer the illustrative proposal in Specify and confirm
with the user/stakeholder; do not invent a coverage percentage as a testability target.

## Rules of thumb

- Do inject time where dependencies are assembled; don't add a public request
  parameter that can bypass the expiry branch merely to help tests.
- Do substitute the external response boundary, not the decision whose correctness
  the test is intended to distinguish.
- Do expose semantic outcomes that separate the targeted branches; asserting only
  "no exception" cannot distinguish a timeout refusal from successful completion.

## Verification

Use controlled-clock, scripted-adapter, integration, and fault-simulation categories.
Exercise time before, at, and after the stated deadline without wall-clock sleeps.
Force both a dependency success and an explicit failure response.
Observe result status and the consequential write or emitted action, not just
that a mocked function was called.
Restore test-owned state and retain failed attempts and unfinished executions.
Use a deliberately broken deadline comparison or altered result as a negative
control for the harness.
Inspect normal construction and external inputs for accidental test switches.
Exercise normal dependency construction separately from the test adapter.
Review assertions for incidental private call order that would reject a harmless
refactoring without distinguishing a required outcome.
Keep substituted-boundary results separate from real dependency integration evidence.

## Done checklist

- [ ] Locate the previously uncontrollable condition or invisible outcome.
- [ ] Drive the real target entrypoint through the new dependency seam.
- [ ] Force the relevant time or response boundary without sleeping.
- [ ] Distinguish the contrasting branch outcomes and side effects.
- [ ] Demonstrate that a wrong branch outcome fails the assertion.
- [ ] Confirm normal construction retains the production dependency path.
- [ ] Check that public input cannot activate the test override.
- [ ] Report which real integrations remain outside the seam-based test.

## Failure modes

- Mocking the decision itself and then reporting the decision as tested.
- Sleeping until a timeout instead of controlling the deadline input.
- Inspecting only a mock call while ignoring an incorrect stored result.
- Shipping an external clock or authorization bypass as a test convenience.
- Making tests depend on incidental private method order.

## References

- Read [test seam decisions](./references/design-guide.md) when choosing control
  and observation seams without bypassing the behavior under test.
- Read [deadline test example](./references/worked-example.md) when driving
  timeout and response branches and checking a deliberately wrong outcome.
