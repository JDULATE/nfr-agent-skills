---
name: maintainability
description: >-
  Reduces recurring upkeep when asked "stop repeated repair work", "help future maintainers", or "review ongoing fix effort". Ask the user if ongoing upkeep vs one edit or support case is unclear. Not for one edit (see modifiability), a support encounter (see supportability), or successive migrations (see evolvability).
---
# Maintainability

## Definition and scope

Maintainability means ongoing diagnosis, repair, and modification remain practical
through repeated upkeep. Evaluate maintenance tasks, evidence, effort, and obligations
left behind; separate one edit's impact (`modifiability`), a support encounter
(`supportability`), and an ordered future migration path (`evolvability`).

## Use when / Don't use when

- Apply when maintainers repeatedly rediscover context, cannot regenerate artifacts,
  or accumulate manual repair steps that make continuing upkeep costly.
- Route one concrete edit envelope to `modifiability` and one failing execution's
  localization to `debuggability`; those can supply maintenance evidence here.
- Route a user's case investigation to `supportability` rather than treating every
  support request as authorization for general maintenance refactoring.

## Workflow

1. Clarify: Read upkeep code, build/test paths, maintainer docs, defect history,
   regeneration procedures, and actual repair examples before specifying sustainability.
   If only a single proposed edit is known, then Ask the user for recurring tasks
   or keep its impact claim under `modifiability` instead of generalizing lifecycle cost.

2. Specify: Select diagnosis, repair, and modification tasks with starting artifacts,
   maintainer context, required outcomes, effort categories, and retained obligations.
   If the request is a practical upkeep improvement, then propose this record:

   ```text
   Illustrative upkeep trial; confirm with the user/stakeholder:
   Scope: 3 representative tasks spanning diagnosis, repair, and modification.
   Starting context: clean checkout plus documented maintainer access and artifacts.
   Example bound: 30 minutes active work per task, with coordination/wait recorded separately.
   Acceptance: required task result plus preserved prior fixes and regeneration evidence.
   Costs: investigation, implementation, verification, repeated operator steps, leftover upkeep.
   Evidence: actual task traces versus forecasts; no claim from changed-line count alone.
   Open choices: task set, effort unit/bound, maintainer context, owners and upkeep horizon.
   ```

   Ask at most three groups about recurring tasks and current pain; maintainer
   context and retained behaviors; and effort accounting, horizon, or defaults.
   Proceed to a scoped maintenance-path design with trial values still proposed.
   If no bound is given, then offer the labeled task/effort trial and confirm with
   the user/stakeholder; do not extrapolate its results to all future maintenance.

3. Design/Implement: Read [upkeep patterns](./references/design-patterns.md) when
   preserving diagnosis context, regeneration paths, or recurring repair obligations.
   If a fix requires repeated manual invalidation, then include that operator work
   in the upkeep comparison instead of reporting only the simpler code path.
   If maintainers need private remembered steps to repair from a clean checkout,
   then make those prerequisites explicit or repair the repository-supported path.

4. Verify: Rehearse the selected tasks from their declared starts; retain outcomes,
   active work, waits, prior-fix checks, and regeneration results.
   If a later maintenance task breaks an earlier repair, then include the resulting
   rediscovery/rework before claiming sustainable upkeep from the successful patch.

5. Report: Return task-specific effort, observed upkeep improvements, remaining
   manual dependencies, and untested maintainer contexts.
   If timings are invented examples or forecasts, then label them accordingly
   and withhold any claim that actual maintenance effort met the proposed bound.

## Specification patterns

- **Upkeep tasks:** `{maintainer_context}` shall complete `{recurring_task_set}`
  from `{documented_starts}` within `{confirmed_effort_bound}` using `{cost_rule}`,
  verified by `{task_results_prior_fix_checks_and_actual_work_log}`.
- **Regeneration:** Maintaining `{generated_artifact}` shall remain possible from
  `{declared_inputs_and_procedure}`, evidenced by `{fresh_regeneration_and_consumer_checks}`
  without `{undocumented_manual_repair}`.
- **Residual work:** After `{maintenance_change}`, continuing upkeep shall include
  at most `{confirmed_manual_or_temporary_obligations}` under `{inspection_horizon}`,
  checked by `{operator_and_temporary_path_ledger}`.

Use the illustrative trial only after confirmation with the user/stakeholder.
Ask the user which representative tasks and maintainer context make the claim meaningful.

## Rules of thumb

- Do replay later upkeep against retained repair fixtures; a patch that makes the
  next maintainer rediscover a solved defect shifts rather than reduces lifecycle work.
- Do retain the regeneration path, not only repaired generated output; a hand-edited
  artifact that breaks again on regeneration creates recurring maintenance debt.
- Do make diagnosis prerequisites available in the declared maintainer context;
  success by an expert's private remembered steps cannot establish a reusable upkeep path.
- Do charge recurring operator repair steps to upkeep after a code simplification;
  moving the work into an undocumented manual ritual does not make maintenance cheaper.
- Don't accept temporary repair scaffolding as free after closing its defect;
  keep its owner, repeated checks, and removal condition in the continuing upkeep ledger.

## Verification

Use clean-checkout maintenance rehearsals, regression replay, regeneration checks,
and task-effort accounting. Retain the same task identity when comparing work;
report active effort separately from excluded waits and repeated operator actions.
Inspect reopened defects, manual repair dependence, and regeneration drift without
turning a favorable task sample into a universal lifecycle-effort forecast.

## Done checklist

- [ ] Complete the agreed diagnosis/repair/modification tasks from declared starts.
- [ ] Reproduce maintenance prerequisites without undocumented expert-only state.
- [ ] Replay retained repair fixtures after a later upkeep task.
- [ ] Regenerate an affected artifact and verify its consumer behavior.
- [ ] Reconcile active effort, waiting, and recurring operator work with the cost rule.
- [ ] Inspect temporary repair paths for owners and continuing/removal obligations.
- [ ] Separate actual task evidence from forecast or synthetic timing.

## Failure modes

- Claiming lifecycle improvement from one small successful diff.
- Hand-editing generated output while losing the procedure that recreates it.
- Removing code complexity by requiring repeated undocumented operator repair.
- Reporting an expert-only repair demonstration as maintainability for ordinary maintainers.
- Ignoring rework when later maintenance reintroduces a previously repaired defect.

## References

- Read [upkeep patterns](./references/design-patterns.md) when choosing recurring
  tasks, cost categories, regeneration evidence, or leftover repair obligations.
- Read [maintenance ledger example](./references/worked-example.md) when comparing
  concrete task outcomes, retained state, and explicitly illustrative effort.
