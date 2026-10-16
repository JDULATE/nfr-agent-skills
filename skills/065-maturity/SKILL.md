---
name: maturity
description: >-
  Assesses operating history when asked "check use since the fix", "link returning defects", or "review exercised workflows". Ask the user if past experience vs future failure trials is unclear. Not for future failure trials (see reliability), combined assurance (see dependability), or upkeep effort (see maintainability).
---
# Maturity

## Definition and scope

Maturity means operational and defect-handling evidence supports readiness for
the intended use. Assess what has actually been exercised, learned, repaired,
and followed up; distinguish a future failure-free interval (`reliability`),
a combined reliance case (`dependability`), and maintenance effort (`maintainability`).

## Use when / Don't use when

- Apply when widening use or changing readiness status depends on demonstrated
  operating history and how recurring defects were handled.
- Route a proposed clean-run experiment to `reliability`; an unexecuted test plan
  is not historical operational evidence.
- Route a broad assurance argument spanning multiple failure properties to
  `dependability`; this skill contributes the actual experience record.

## Workflow

1. Clarify: Read release/feature code history, deployment docs, actual operation
   records, incident/defect history, and repair follow-up before judging readiness.
   If the supplied evidence belongs to a different version, audience, or workload,
   then separate transferable experience from the intended-use gaps instead of merging it.

2. Specify: Record readiness decision, intended use, operating episodes, revisions,
   exposure gaps, defect recurrence, repair verification, and evidence freshness.
   If the user asks for a practical readiness review, then propose this history record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Decision: readiness for the stated expansion of actual use, not universal maturity.
   History trial: review the available last 30 days of operation and defect handling.
   Relevance: audience, workload, configuration, release, and exercised features per episode.
   Defects: severity/recurrence definitions need the stakeholder; closed labels are not evidence.
   Repairs: source change plus verification and relevant post-change operating follow-up.
   Gaps: unexercised features, missing telemetry/history, and changed-context assumptions.
   Decision rule: each readiness condition supported, explicitly conditional, or unresolved.
   Status: proposed evidence window; age alone and invented maturity scores confer no readiness.
   ```

   Ask at most three groups about intended use/readiness; available history and
   qualifying contexts; and criticality, required follow-up, or decision authority.
   Continue to a versioned experience ledger without fabricating missing episodes.
   If no review window exists, then offer the illustrative history window and
   confirm with the user/stakeholder before treating it as sufficient coverage.

3. Design/Implement: Read [operational-history practices](./references/design-patterns.md)
   when mapping exposure, recurring defects, and verified repairs.
   If a defect is marked closed without relevant follow-up, then separate the
   code fix from demonstrated operating improvement and identify the missing evidence.
   If the same failure returns under a new ticket, then link the recurrence;
   resetting identifiers must not make the experience record look resolved.

4. Verify: Reconcile releases, actual episodes, defect identity, fix revisions,
   reproductions, and post-fix use; inspect gaps and contradictory incidents.
   If operation was unobserved, then mark exposure quality unknown rather than
   treating a quiet incident list as proof of defect-free demonstrated use.

5. Report: Return the relevant experience ledger, unresolved recurrences,
   verified repairs, new-use gaps, and a scoped readiness assessment.
   If the intended use lacks relevant history, then report that limitation and
   any proposed trial separately; do not manufacture experience through planned work.

## Specification patterns

- **Readiness evidence:** For `{intended_use_and_release}`, assess `{readiness_conditions}`
  using `{relevant_operational_episodes}`, `{defect_and_repair_history}`, and
  `{confirmed_follow_up_rule}`, with `{missing_or_changed_contexts}` explicit.
- **Recurrence handling:** For `{defect_family}`, connect `{observed_episodes}`
  to `{cause_fix_revision_and_verification}`, and substantiate `{resolution_claim}`
  through `{qualifying_post_change_use}` rather than `{ticket_status_alone}`.

Use the illustrative history window to propose a missing review scope;
confirm with the user/stakeholder. Ask the user which evidence supports their readiness decision.

## Rules of thumb

- Don't substitute release age for exercised experience; an old but unused feature
  supplies no operating history for the new audience that will depend on it.
- Do link recurring defects across renamed tickets and releases; administrative
  closure must not reset the record of unresolved operating experience.
- Do distinguish code-fixed from followed-up in relevant operation; a patch's
  presence does not establish that the reported failure stayed resolved after use.
- Don't import another environment's incident-free history without its context;
  changed workloads or configurations can leave the intended release insufficiently experienced.
- Do preserve observation gaps beside quiet incident periods; missing failure
  reports cannot support demonstrated readiness when qualifying operation was unobserved.

## Verification

Use release/incident reconciliation, defect-lineage review, and repair-follow-up
inspection categories. Link evidence to actual revisions and exercised features,
not only deployment dates. Inspect recurrence under changed ticket identifiers,
fix verification, post-fix exposure, and observation gaps. Separate a proposed
qualification trial from already demonstrated experience; neither age nor a closed ticket count is a readiness oracle.

## Done checklist

- [ ] Ground readiness in the intended release, use, audience, and operating context.
- [ ] Link qualifying episodes to actual revisions and exercised capabilities.
- [ ] Distinguish relevant exposure, idle deployment, and unobserved history.
- [ ] Connect recurrent defect families across tickets and releases.
- [ ] Map repairs to source changes, verification, and qualifying post-fix use.
- [ ] Reconcile contrary incidents and still-open recurrence claims.
- [ ] Report new-use gaps and planned trials separately from demonstrated experience.

## Failure modes

- Calling a release mature because it has existed for a long time.
- Treating ticket closure as proof a defect stayed resolved in operation.
- Counting deployments or users without checking what behavior was exercised.
- Hiding recurrence by renaming incidents or splitting them across releases.
- Presenting planned tests or missing observation as demonstrated history.

## References

- Read [operational-history practices](./references/design-patterns.md) when deciding
  which experience transfers, linking recurrences, or assessing repair follow-up.
- Read [release-expansion example](./references/worked-example.md) when old operational
  history does not establish readiness for a newly introduced workflow.
