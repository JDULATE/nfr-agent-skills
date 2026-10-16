---
name: modifiability
description: >-
  Bounds one code change and its ripple effects when tickets say "how much code will this edit touch", "changing this rule breaks other modules", or "estimate the work for this code change". Not for recurring upkeep (see maintainability), request progress (see changeability), or successive changes (see evolvability).
---
# Modifiability

## Definition and scope

Modifiability means making a named implementation change with bounded impact
and effort. Include affected responsibilities, contracts, migration, and verification;
distinguish continuing maintenance (`maintainability`), request progress
(`changeability`), and a future change sequence (`evolvability`).

## Use when / Don't use when

- Apply when a specified rule edit, replacement, or refactor needs an inspectable
  impact envelope and evidence of the implementation work it actually requires.
- Route ongoing diagnosis/repair burden to `maintainability`.
- Route new core capability admission to `extendability`; this skill can separately
  bound its implementation impact. Route an existing-result refinement surface
  to `enhanceability` where that capability's improvement is the acceptance question.

## Workflow

1. Clarify: Inspect target code, dependencies, ownership docs, contract tests,
   generated outputs, and past related diffs before bounding an edit.
   If no particular edit is known, then Ask the user for a representative change
   instead of inferring universal ease of modification from a small module count.

2. Specify: Define counted responsibilities, contracts, retained behavior, work
   categories, estimate assumptions, and how actual impact will be compared.
   If the user wants an implementation plan, then propose this edit envelope:

   ```text
   Illustrative impact envelope; confirm with the user/stakeholder:
   Edit: named rule change, with its new behavior separately agreed.
   Example bound: 2 production owner components under an agreed ownership map.
   Full impact: callers, generated artifacts, migrations, tests, docs, coordination.
   Work ledger: investigation, implementation, verification, migration, waiting separate.
   Preservation: named unaffected behaviors and before/after counterexamples.
   Evidence: predicted/actual dependency diff, owner review, focused behavior checks.
   Open decisions: counted units, scope/effort bound, exceptions, estimate confidence.
   ```

   Ask up to three questions: which edit and retained meanings; which surface or
   effort limit matters; and which consumer/migration obligations exist.
   Proceed to an impact map with forecasts separate from measured work.
   If no bound is supplied, then offer the labeled component example and confirm
   with the user/stakeholder; obtain a separate time bound when effort is the goal.

3. Design/Implement: Read [impact patterns](./references/design-patterns.md) when
   tracing semantic fan-out, choosing an edit seam, or accounting for work.
   If a local edit changes a public meaning, then expand the consumer/migration
   ledger before calling it local, even if callers need no textual changes.
   If actual impact exceeds the envelope, then expose extra owners and required
   work for a scope decision instead of hiding generated or test changes.

4. Verify: Compare the actual diff and behaviors with the predicted impact map;
   exercise changed-rule and retained cases through real consumers.
   If a caller fails outside the predicted surface, then revise the dependency
   assumptions and rerun its checks before asserting bounded modification impact.

5. Report: Return predicted/actual owner and contract impact, work records,
   migration evidence, preserved-case results, and estimate uncertainty.
   If work was only planned, then label effort as forecast and withhold any
   claim of observed cost or a demonstrated bound for future edits.

## Specification patterns

- **Impact:** Implementing `{named_edit}` shall remain within
  `{confirmed_owner_and_contract_surface}` under `{counting_rule}`, verified by
  `{complete_diff_and_consumer_checks}` including `{accepted_exceptions}`.
- **Effort:** Completing `{edit}` including `{work_categories}` shall meet
  `{confirmed_effort_bound}`, measured by `{actual_work_ledger}` with
  `{coordination_and_wait_rule}` and forecasts identified separately.
- **Preservation:** After `{edit}`, `{unaffected_behaviors}` shall retain
  `{agreed_meanings}` under `{consumer_cases}`, except for `{approved_delta}`.

Use the illustrative component bound only with a transparent ownership map;
confirm with the user/stakeholder. Ask the user which effort categories count.

## Rules of thumb

- Do map semantic consumers as well as imports; stored rule results can spread
  this edit's impact to code with no dependency on the edited function.
- Do include investigation and verification in edit-effort accounting; a tiny
  patch can require broad reasoning work that changed-line counts conceal.
- Do separate predicted from observed impact; a plausible dependency diagram
  cannot prove this particular implementation stayed inside its envelope.
- Do charge generated adapters and migrations to the edit requiring them;
  excluding them from a production source count does not remove their change cost.
- Do choose seams from the named edit's fan-out; a generic platform that does not
  reduce that fan-out can add modification work instead of bounding it.

## Verification

Use dependency/contract review, focused regression checks, and predicted-versus-actual
diff inspection. Exercise the edited rule and preserved counterexamples through
callers, including consumers of written meanings. Reconcile actual work with the
agreed categories; retain unexpected owners and failed predictions. Treat repeat
edits as separate evidence, not universal cheap-change proof. Missing consumer
checks or unmeasured coordination remain gaps in this edit's impact claim.

## Done checklist

- [ ] Reconcile changed responsibilities against the agreed ownership map.
- [ ] Compare affected contracts and semantic consumers with the prediction.
- [ ] Exercise the changed rule through its actual public caller path.
- [ ] Replay unaffected cases without weakening retained expectations.
- [ ] Account for required generation, migration, and verification work.
- [ ] Compare observed effort with the ledger convention, separating forecasts.
- [ ] Expose out-of-envelope owners and untested consumers rather than omitting them.

## Failure modes

- Treating a small diff as proof of bounded total modification effort.
- Ignoring stored-meaning consumers whose source imports did not change.
- Reporting a predicted impact map as observed implementation work.
- Omitting generation or migration to satisfy a production-only count.
- Generalizing one successful edit into cheap future changes without a bound.

## References

- Read [impact patterns](./references/design-patterns.md) when selecting counted units,
  tracing semantic fan-out, or separating forecasts from measured work.
- Read [label-rule example](./references/worked-example.md) when reconciling a local
  rule edit with consumer obligations and a complete change-impact ledger.
