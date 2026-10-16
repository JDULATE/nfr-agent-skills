# Batch 10 fixes

## Findings after revision

The changes are confined to ids 41, 72, 74, 77, 88 and 99 and this report.
The catalogue already marks these entries draft. No other batch, index,
authoring contract, audit or validation threshold was changed.

All 20 Rules of thumb bullets marked transferable in the audit now appear
verbatim in Verification and no longer appear in Rules of thumb. Additional
shared condition-group, class-accounting and resource-policy checks were moved
there too. New bullets describe intervention choices under the skill's acceptance
question; the removed bullets were not disguised through noun changes.

Every design reference now contains an evidence -> intervention -> verification
decision table with trade-offs and four concrete interventions, plus a short
pseudocode sketch. The four requested guides have positive implementation
choices rather than only measurement cautions. Efficiency and Sustainability
also received decision tables to address their named depth gaps.

Each worked example fills its cohort, relevant conditions, carried state and
outcome rule, with a failing case and a before/after remedy. The examples remain
explicitly synthetic. They do not represent observed performance of this repo.

## Per-skill findings

### 041 efficiency-device-efficiency

The report example now identifies every offered result, the dropped subset,
comparison window, worker scope and exact output. The missing-result failure
therefore follows from a supplied cohort obligation rather than just a smaller
completion count. Request-local coalescing reduces modeled decode calls while
preserving every output; setup/batch selection has a separate decision sketch.
A second filled wire example supports the description's transferred-byte trigger.
The plan-selection requirement pattern now includes an acceptance rule.

Remaining limitation: the costs are supplied model inputs. Real decode equivalence,
scope and packing overhead need source inspection and measurement. The wire
variant deliberately has no CPU model and cannot support a compute-saving claim.

### 072 performance-efficiency-time-or-space-bounds

The description explicitly includes absolute tail-percentile deadlines and
excludes spread/variation. Bounded lookup batching, overlapped dependency waits,
private-page streaming and reduced queued service demand have selection evidence,
trade-offs and verification. The example supplies row counts, arrival times,
stage costs, memory accounting, complete artifacts and a mixed-outcome policy.
The fast completed subset fails when required exports time out or are rejected.
Correctness and disclosure are now separate done items.

Remaining limitation: the fixture's stage costs are stipulated. A real page reader
may materialize internally, so a small caller-side page is not sufficient proof
of the actual memory bound. No live throughput or memory measurement is claimed.

### 074 predictability

The description asks whether a tail complaint means variation or an absolute
deadline. The incremental-cleanup example supplies a shared cursor, full expired
cohort, arrival pattern, work costs, complete observations and zero unknowns.
It demonstrates a narrower range with unchanged mean and complete cleanup by
the observation end. Padding results supplies a distinct failing remedy.

Remaining limitation: no new expiry work enters this finite fixture. A production
quota can leave growing cleanup debt; the guide explicitly calls for checking
that case instead of inferring sustainable capacity from this run.

### 077 quality-of-service

The example is retitled around a failed batch deadline and reserved dispatch.
It supplies eligible jobs, trusted class assignment, worker capacity, service
times, dispatch order and independent limits. The original policy eventually
completes batch work, so its missed deadline is not labeled starvation.
The reservation improves batch progress while worsening interactive latency
within its accepted bound. Both classes' exact results remain present.

Remaining limitation: this is a finite non-preemptive cohort with no later arrivals.
A reservation sequence does not establish a completion guarantee under arbitrary
job lengths, continued demand or downstream contention. The guide distinguishes
dispatch opportunities from elapsed-time guarantees and bounds borrowing.

### 088 scalability

The example supplies observation duration, actual resource amounts, independent
keys, source capability, coordination budget, result identity and backlog state.
Removing the stipulated coordination gate changes the fixed-resource curve;
adding workers is a separate series with explicit allocation cost. The passing
and failing points remain visible. The known cause is an input to this model,
not a diagnosis inferred solely from a plateau.

Remaining limitation: the model uses balanced independent keys and no owner
movement. Real skew, cross-key transactions or stale owners may rule out the
partitioning remedy. The sketch requires a real supported ownership/effect
mechanism; it does not assume a hash supplies those semantics.

### 099 sustainability

The description now promises operational energy and device-life choices, with
both demonstrated. The energy example fills its synthetic source, component
ledger, output cohort, period, idle allocation and local boundary. A new device-life
example shows temporary-buffer retention causing a task failure, then release
of disposable state keeping the unchanged device profile useful through a defined
review event. Required output files remain readable; preview eviction is not
silently treated as permission to delete retained records.

Remaining limitation: simulated service adequacy is not longer physical hardware
life. Acquisition, retirement, physical-failure and emissions evidence remain
unavailable; neither example supports a net environmental conclusion. Objective
comparison and continued useful service now have separate done items.

## Transfer test after fixes

These counts cover every remaining rule. Partly means an intervention mechanism
can help a sibling, but its acceptance question cannot move unchanged. It does
not mean a shared measurement safeguard was retained as a rule. Specific means
the rule's differentiated-class decision is directly the mapped concern.

- 041: 0 transferable, 4 partly, 0 specific. Nearest sibling: sustainability;
  resource-cost intervention selection does not itself settle stewardship.
- 072: 0 transferable, 4 partly, 0 specific. Nearest siblings: quality-of-service
  and scalability; the interventions here accept a stated operation envelope,
  not independently differentiated classes or a growth curve.
- 074: 0 transferable, 4 partly, 0 specific. Nearest sibling:
  performance-efficiency-time-or-space-bounds; preserving or reducing spread is
  the acceptance question even where the same path affects absolute latency.
- 077: 0 transferable, 1 partly, 4 specific. Nearest sibling:
  performance-efficiency-time-or-space-bounds; the shared-pool mechanism transfers,
  while the rule accepts or rejects independent class treatment.
- 088: 0 transferable, 4 partly, 0 specific. Nearest siblings: expandability,
  predictability and performance-efficiency-time-or-space-bounds; the acceptance
  question concerns response to growth under a resource policy.
- 099: 0 transferable, 4 partly, 0 specific. Nearest sibling:
  efficiency-device-efficiency; continued device service and lifecycle decisions
  differ from accepting a device resource ratio.

Total: 25 rules checked after fixes; 0 transferable, 21 partly, 4 specific.
Mechanisms remain shared across NFRs. These are author judgments about acceptance
questions, not evidence of empirically distinct agent routing or independent approval.

## Description routing findings

For an absolute percentile-budget request, 072 is now the direct lead; 074 points
back to it rather than competing on generic outlier language. A request for less
spread leads to 074. A vague pause complaint still needs the stated deadline-versus-
variation question. This missing intent cannot be repaired by a longer exclusion list.

The audit's remaining probes still require honest context: less memory can mean
041's resource objective or 072's space ceiling; larger imports can mean 072's
fixed envelope or 088's growth curve; keep interactive work fast needs competing
class obligations before selecting 077. Adding workers alone still points to
expandability. CPU per valid report selects 041; device-life extension selects
099 and now reaches a filled example. None of these manual checks measures
model-selection accuracy.

## Measured footprint

Counts include blank lines; combined counts include frontmatter and directly
linked references. All descriptions fit the new limit, all rule lists have
4-6 items, all guides are below 80 lines and all references are below 150 lines.

| Id | Description characters | Body lines | Rules | Design guide lines | Example lines | Combined lines |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| 041 | 286 | 124 | 4 | 39 | 64 | 232 |
| 072 | 306 | 126 | 4 | 45 | 68 | 244 |
| 074 | 318 | 122 | 4 | 42 | 51 | 220 |
| 077 | 291 | 127 | 5 | 43 | 58 | 233 |
| 088 | 276 | 123 | 4 | 43 | 60 | 231 |
| 099 | 282 | 129 | 4 | 39 | 48 + 55 | 276 |

No document was padded to vary or reach a count. The combined footprints fall
within the current guideline. The retained pre-existing audit remains historical
and still describes the sources before these revisions.

## Validation evidence

- Selected repository validation: 6 skills checked, 0 absent todo skills, 0 errors.
- Full repository validation: 63 skills checked, 51 absent todo skills, 0 errors.
- Foundation suite: all 19 tests passed.
- Skill-creator frontmatter validation: all six revised skills passed.
- Seven inline model tests passed: report coalescing and wire equivalence;
  export paging, mixed outcomes and percentile calculations; cleanup work/range;
  class dispatch and deadlines; coordination budgets, key order and backlog;
  energy-ledger arithmetic; device-buffer release and required file preservation.
- A source comparison confirmed all 20 audit-marked transferable bullets were
  preserved verbatim in Verification and removed from Rules of thumb.
- Manual contract checks confirmed description limits, rule counts, decision-table
  interventions, sketches, reference links and footprint limits.

## Uncertain claims

Actual workload costs, cleanup arrival rates, permitted key independence, scheduler
capacity, physical device life and energy impact are unknown for a real target
repository. The guides call for source evidence and stakeholder decisions before
applying the corresponding intervention. No external standard, tool version,
legal obligation, formal proof or measured production result was added.

Passing validators checks structure, citations and similarity; it does not validate
an architecture or establish that every remaining rule will route distinctly in use.
The simplified sketches require implementation-specific concurrency, cancellation,
storage and policy semantics. No real system exercise or stakeholder review occurred.
