---
name: enhanceability
description: >-
  Plans refinements to an existing capability when users say "make this feature
  better without adding another one", "refine the current parser", "improve the
  existing result", or "make future quality upgrades easier". Not for adding a
  separately accepted supporting function (see augmentability) or a multi-change
  lifecycle strategy (see evolvability).
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

2. Specify: Capture baseline, improvement metric, protected input groups,
   adjustable implementation surface, and the regression trade-off policy.
   If the request is practical rather than a formal specification, offer:

   ```text
   Illustrative refinement proposal; confirm with the user/stakeholder:
   Capability: the existing operation, output contract, and target audience.
   Baseline: retained current-version results on the agreed representative corpus.
   Target: 10% fewer errors on the existing criterion, only where that metric applies.
   Constraints: preserve named protected cases; no newly invented output capability.
   Surface: a named strategy or internal implementation boundary already in use.
   Evidence: paired old/new outcomes, changed-case explanations, and caller checks.
   Open decisions: error definition, corpus mix, accepted trade-offs, and owner.
   ```

   Ask up to three grouped questions about what better means, which existing
   cases must not worsen, and which consumers or implementation boundaries may
   change. Start a refinement design without pretending an unapproved metric is accepted.
   If a formal target is absent, then offer the illustrative error reduction above
   and confirm with the user/stakeholder; choose another metric when errors do not apply.

3. Design/Implement: Consult [refinement patterns](./references/design-patterns.md)
   when isolating a strategy, comparing candidate results, or staging adoption.
   If the refinement changes output meaning or adds a new result category, then
   reassess whether the request has crossed into a new capability.
   If a candidate helps the aggregate but harms a protected group, then expose
   that trade-off and retain the baseline path until the owner resolves it.

4. Verify: Replay a matched corpus through baseline and candidate implementations;
   compare the existing acceptance measure and protected cases independently.
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
- Do retain old outputs for paired review; don't overwrite the baseline corpus
  while using it to demonstrate a candidate's gain.
- Do compare protected case groups alongside aggregate quality; don't hide a
  degraded existing use case inside a favorable average.
- Do preserve public meaning while changing the internal strategy; don't quietly
  reinterpret an existing field to make the new result appear better.
- Don't revise both the scoring rule and implementation in the same improvement
  claim without showing their separate contributions to the reported difference.

## Verification

Use paired-corpus evaluation, differential contract checks, and strategy-substitution
review categories. Inspect changed outputs, their original acceptance judgments,
and protected-case behavior. Exercise a caller using the existing result format.
Check empty-error baselines, unsupported input groups, and reversions to the old
strategy. Attribute metric changes to the candidate, corpus, or scoring definition
explicitly; a demonstration of swappable code is not evidence of improved results.

## Done checklist

- [ ] Identify the existing capability and its unchanged result meaning.
- [ ] Retain baseline implementation, corpus, and acceptance definitions.
- [ ] Agree the improvement metric and its applicable baseline.
- [ ] Name protected cases and permitted trade-offs.
- [ ] Locate the implementation surface that admits the refinement.
- [ ] Compare candidate outputs, caller behavior, and reversibility.
- [ ] Report actual improvement evidence separately from ease of substituting code.

## Failure modes

- Declaring a new output category to be a better version of the old result.
- Improving an aggregate while concealing regressions in a required existing case.
- Measuring gain after changing the reference answers or removing difficult inputs.
- Claiming relative error reduction when the baseline has no measured errors.

## References

- Read [refinement patterns](./references/design-patterns.md) when defining a stable
  improvement surface, paired evaluation, and consumer-preserving adoption.
- Read [parser refinement example](./references/worked-example.md) when specifying
  an existing capability's improvement without adding a separate capability.
