---
name: flexibility
description: >-
  Supports alternative ways to perform the same task when tickets say "offer manual and automatic routes", "let users choose another way through", or "keep both workflows supported". Not for external changes (see adaptability), tuning a control (see adjustability), or switching state (see reconfigurability).
---
# Flexibility

## Definition and scope

Flexibility means supporting meaningful alternative ways to perform or arrange
the same work. Accept each route's result and conditions of choice; distinguish
external accommodation (`adaptability`), parameter tuning (`adjustability`),
and actually moving between arrangements (`reconfigurability`).

## Use when / Don't use when

- Apply when users need manual/automated routes or another supported arrangement
  that produces the same agreed task outcome.
- Route contextual fitting to `tailorability` and user-defined behavior beyond
  built-in choices to `customizability`; alternatives alone do not prove either.
- Route moving in-progress work between arrangements to `reconfigurability`.

## Workflow

1. Clarify: Read task code, dispatch decisions, mode docs, supported arrangements,
   and acceptance examples before specifying useful alternatives.
   If only a parameter value differs, then Ask the user whether `adjustability`
   or the valid settings menu in `configurability` is the real concern.

2. Specify: Map alternatives to shared results, deliberate differences, eligible
   choosers, route prerequisites, and evidence that each arrangement is usable.
   If the user wants practical choice, then offer this alternative record:

   ```text
   Illustrative option record; confirm with the user/stakeholder:
   Task: documented result and required side effects shared by all routes.
   Example scope: 2 alternatives, manual and automated, only where useful/requested.
   Choice: explicit selection before task start; no live-state transfer assumed.
   Differences: route-specific inputs, authority, resources, allowed result variation.
   Evidence: independently completed tasks, selection traces, unavailable-choice cases.
   Owner/status: task owner; alternative set, prerequisites, and defaults proposed.
   ```

   Ask at most three questions: shared outcome and useful alternatives; who may
   choose under which conditions; and differences or constraints needing revision.
   Proceed to an alternatives design without promising live switching.
   If no choice set is given, then propose the illustrative pair only where
   relevant and confirm with the user/stakeholder before accepting that scope.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [alternative patterns](./references/design-patterns.md) when
   choosing common obligations, route-specific prerequisites, and selection behavior.
   If routes require different inputs or authority, then expose those conditions
   before counting them as available options for the intended chooser.
   If live work must move between routes, then separate its transition/state
   requirements under `reconfigurability` from independent route coverage here.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Complete matched tasks separately through each agreed route; compare
   common outcomes and deliberately allowed differences.
   If choices dispatch to the same blocked implementation, then report the missing
   alternative rather than accepting several menu labels as task flexibility.

5. Report: Return the outcome/eligibility matrix, distinct dispatch evidence,
   observed differences, restrictions, and arrangements not exercised.
   If a route worked only with administrator access or fixture privileges, then
   leave its usability for the intended chooser unverified.

## Specification patterns

- **Alternatives:** For `{task_and_audience}`, `{system}` shall support
  `{confirmed_alternative_set}` meeting `{shared_outcome}` under `{route_conditions}`,
  evidenced by `{independent_per_route_tasks}`.
- **Choice:** Under `{eligibility}`, `{chooser}` shall select `{supported_route}`
  before `{task_start}`, with `{unavailable_route_response}`, checked by
  `{selection_and_dispatch_trace}`.
- **Difference:** Results from `{route_pair}` shall agree on `{shared_obligations}`
  while allowing `{named_differences}`, verified by `{outcome_matrix}`.

The illustrative pair is a scope proposal, not a universal workflow requirement;
confirm with the user/stakeholder. Ask the user which alternatives matter.

## Rules of thumb

- Do identify the result shared by alternatives; unrelated features under a mode
  selector do not establish different ways to accomplish the same task.
- Do trace each choice to actual work; aliases for the same blocked implementation
  cannot satisfy independent alternative coverage.
- Do list each route's eligibility before counting it; an administrator-only route
  is not a usable alternative for an audience without that authority.
- Do compare required writes as well as displayed results; a manual route omitting
  the task's commit is not an equivalent alternative to the automated route.
- Do state deliberate route differences; forcing identical intermediate steps
  can erase the different way of working the stakeholder actually requested.
- Don't turn independent route starts into a live-switching promise; coverage of
  both arrangements does not establish transfer of in-progress task state.

## Verification

Use alternative-path integration checks, eligibility matrices, and dispatch review.
Run equivalent tasks independently with matched starting conditions; inspect
result artifacts, required writes, and route prerequisites. Reject unavailable
selections using the accepted response. Inspect failed choices by eligibility
class; an unused route is not automatically impossible, but absent real use
cannot establish that the intended audience successfully used it.

## Done checklist

- [ ] Complete each agreed route independently as the intended chooser.
- [ ] Compare shared results and required writes across the route matrix.
- [ ] Trace distinct labels to their actual task implementations.
- [ ] Exercise unavailable or ineligible choices under the accepted response rule.
- [ ] Check prerequisites without silently using elevated fixture authority.
- [ ] Reconcile result differences against the explicitly allowed variation.

## Failure modes

- Calling several labels for the same blocked path independent alternatives.
- Counting a route whose prerequisites the intended audience cannot meet.
- Equating matching display text with equivalent committed task outcomes.
- Promising stateful switching from successful independent route starts.

## References

- Read [alternative patterns](./references/design-patterns.md) when defining shared
  obligations, route differences, and chooser eligibility.
- Read [dispatch-route example](./references/worked-example.md) when testing manual
  and automated arrangements without inventing live-transition guarantees.
