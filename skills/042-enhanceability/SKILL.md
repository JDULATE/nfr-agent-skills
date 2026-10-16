---
name: enhanceability
description: >-
  Designs changes that improve an existing capability when tickets say "make this parser easier to improve", "swap in a better algorithm", or "upgrade this feature without adding a new one". Not for judging output error alone (see accuracy), adding helpers (see augmentability), or staged changes (see evolvability).
---
# Enhanceability

## Definition and scope

Enhanceability means an existing capability can be improved against its existing
acceptance criteria without becoming a separately accepted capability. Identify
the refinement surface and the old result being improved; separate a supporting
function (`augmentability`) and a sequence of future changes (`evolvability`).

## Use when / Don't use when

- Apply when the same capability needs a controlled refinement and the design
  must support that refinement without replacing its purpose or consumers.
- Focus on the path for improving the existing result, not any arbitrary code change.
- Route a specified output-error question alone to `accuracy`, or a response-time
  objective alone to `performance-efficiency-time-or-space-bounds`.
- Route a new independently useful result to `extendability` or `augmentability`
  according to whether it changes core capability or attaches a supplement.

## Workflow

1. Clarify: Read the current implementation code, acceptance docs, reference corpus,
   caller expectations, and past refinement diffs before choosing an improvement.
   Name the unchanged capability and the acceptance dimension that should improve.
   If no existing criterion distinguishes better from merely different, then
   Ask the user for that criterion before declaring a refinement successful.

2. Specify: Capture baseline, improvement metric, protected inputs, refinement
   impact bound, adjustable surface, and the regression trade-off policy.
   If the request is practical rather than a formal specification, offer:

   ```text
   Illustrative refinement proposal; confirm with the user/stakeholder:
   Capability: the existing operation, output contract, and target audience.
   Baseline: retained current-version results on the agreed representative corpus.
   Target: 10% fewer errors on the existing criterion, only where that metric applies.
   Constraints: preserve named protected cases; no newly invented output capability.
   Surface: named computation boundary; list admitted edits and affected callers.
   Evidence: refinement diff versus agreed impact; paired outcomes and caller checks.
   Open decisions: error definition, corpus mix, accepted trade-offs, and owner.
   ```

   Ask up to three grouped questions about what better means, which existing
   cases must not worsen, and which consumers or implementation boundaries may
   change. Start a refinement design without pretending an unapproved metric is accepted.
   If a formal target is absent, then offer the illustrative error reduction above
   and confirm with the user/stakeholder; choose another metric when errors do not apply.

3. Design/Implement: Consult [refinement patterns](./references/design-patterns.md)
   when isolating a strategy, comparing candidate results, or staging adoption.
   If the candidate requires edits beyond the agreed refinement surface, then
   expose those edits before claiming that surface admits the refinement.
   If a candidate helps the aggregate but harms a protected group, then expose
   that trade-off and retain the baseline path until the owner resolves it.

4. Verify: Replay a matched corpus through baseline and candidate implementations;
   compare quality and protected cases, then reconcile the adoption diff with
   the agreed refinement surface and impact bound.
   If fixture edits or revised acceptance definitions explain the apparent gain,
   then separate those changes and rerun the original comparison before claiming improvement.

5. Report: Present the refinement surface, paired outcomes, protected-group results,
   caller impact, and the decision to adopt or retain the baseline.
   If the baseline already has no measured errors, then report that the proposed
   relative-error target is inapplicable rather than inventing a percentage gain.

## Specification patterns

- **Refinement:** The existing `{capability}` shall support replacing `{internal_strategy}`
  to improve `{existing_acceptance_metric}` from `{baseline}` to `{confirmed_target}`
  on `{matched_corpus}`, without changing `{public_result_meaning}`.
- **Protected cases:** Refining `{capability}` shall preserve `{named_case_invariants}`
  under `{protected_inputs}`, verified by `{paired_regression_record}` and
  `{explicit_tradeoff_policy}`.
- **Adoption:** Switching between `{baseline_and_candidate}` shall leave
  `{caller_contract}` intact, checked against `{existing_consumer_cases}`.

Use the labeled proposal only for a meaningful nonempty baseline; Ask the user
for an absolute or qualitative acceptance criterion when a relative metric is undefined.

## Rules of thumb

- Do define the same result before and after refinement; don't count a new output
  category as an improvement without acknowledging the capability change.
- Do isolate the part that computes the existing result when it enables the named
  refinement; don't build a general extension platform for an unrequested upgrade.
- Do replay retained outputs through the proposed replacement surface; a better
  candidate patched into a separate evaluation script does not prove the application
  can adopt that refinement through its declared boundary.
- Do exercise protected groups and current callers through the replacement surface;
  an aggregate gain that requires caller-specific repair hides the refinement's impact.
- Do separate edits that admit a candidate from changes to its scoring definition;
  a revised acceptance rule cannot prove the old capability became easier to refine.

## Verification

Use paired-corpus evaluation, differential contract checks, and strategy-substitution
review categories. Inspect changed outputs, their original acceptance judgments,
and protected-case behavior. Trace adoption edits and affected callers against the
confirmed refinement-impact envelope; better output alone does not establish it.
Check empty-error baselines, unsupported input groups, and reversions to the old
strategy. Attribute metric changes to the candidate, corpus, or scoring definition
explicitly; a demonstration of swappable code is not evidence of improved results.

## Done checklist

- [ ] Replay matched baseline/candidate cases through the inspected refinement surface.
- [ ] Reconcile the refinement diff and affected callers with the accepted impact bound.
- [ ] Compare protected input groups without hiding a regression in the aggregate.
- [ ] Exercise existing callers without reinterpreting their result fields.
- [ ] Select and revert the strategy, checking any persisted results afterward.
- [ ] Attribute the quality difference using unchanged reference/scoring rules and
  identify inapplicable relative targets when the baseline has no measured errors.

## Failure modes

- Declaring a new output category to be a better version of the old result.
- Improving an aggregate while concealing regressions in a required existing case.
- Showing improved offline results while adopting the candidate still requires
  unreported edits outside the declared refinement surface.
- Measuring gain after changing the reference answers or removing difficult inputs.
- Claiming relative error reduction when the baseline has no measured errors.

## References

- Read [refinement patterns](./references/design-patterns.md) when defining a stable
  improvement surface, paired evaluation, and consumer-preserving adoption.
- Read [parser refinement example](./references/worked-example.md) when specifying
  an existing capability's improvement without adding a separate capability.
