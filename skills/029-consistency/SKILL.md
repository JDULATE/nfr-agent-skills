---
name: consistency
description: >-
  Aligns representations when tickets say "the list and detail page disagree", "the cache shows an older status", or "these views conflict at the same revision". Not for external reference error (see accuracy) or unauthorized edits (see integrity).
---

# Consistency

## Definition and scope

Consistency means representations or decisions agree under an explicit
equivalence and coordination rule. Define which entities, fields, and revisions
may be compared and what differences the rule permits.
Separate mutual agreement from external reference error (`accuracy`) and
protection against alteration (`integrity`).

## Use when / Don't use when

- Apply when a cache, list, detail view, or decision path conflicts with another
  representation of the same agreed state.
- Require the comparison boundary: same revision, minimum revision, snapshot,
  or another stakeholder-defined coordination model.
- Route a mutually agreed but factually wrong value to `accuracy`.
- Route unauthorized or unintended state alteration to `integrity`.
- Route choosing common vocabulary to
  `standardizability-standardization-standard`; matching spelling alone does
  not establish agreement about the underlying state.

## Workflow

1. Clarify: Read writers, read models, cache keys, invalidation paths, revision
   metadata, and coordination docs before specifying.
   Trace the disagreement to actual entity and revision pairs.
   If the user asks for "consistent" without a comparison model, then Ask the
   user what must agree, when, and whether stale but identified views are allowed.

2. Specify: Record authority, entity identity, equivalence mapping, revision
   boundary, allowed lag or unknown behavior, and the fields compared.
   If no model is selected, then propose this labeled illustrative default:
   named views agree for the requested revision or explicitly report unavailable
   evidence for it; confirm with the user/stakeholder.
   Do not silently promise instantaneous agreement across all readers.
   Ask at most three grouped questions about authority, comparison semantics,
   and stale/unknown behavior before a practical remediation.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [agreement decisions](./references/design-guide.md)
   when choosing revision-aware reads, snapshot assembly, or semantic comparison.
   If a cached revision differs from the required revision, then fetch qualifying
   state or report the declared unresolved result rather than relabeling the cache.
   If representations use different state names, then compare their agreed
   meanings instead of raw spelling.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Interleave updates and reads through both paths, recording entity,
   revision, returned values, and the selected agreement decision.
   Preserve stale results and unfinished propagation in the evidence.
   If values disagree only because the compared revisions differ, then classify
   that finding under the stated freshness rule rather than declaring a same-state conflict.

5. Report: Return the equivalence contract, changed read/write boundaries,
   interleaving results, and remaining coordination limits.
   If only a sequential fixture was checked, then withhold claims about
   untested concurrent or partitioned behavior.

## Specification patterns

- **View agreement:** For `{entity_and_revision_boundary}`,
  `{representations}` shall agree on `{fields_under_equivalence_mapping}`,
  verified by `{paired_read_and_revision_evidence}`.
- **Stale read:** When `{read_path}` cannot supply `{required_revision}`,
  it shall return `{declared_stale_or_unresolved_result}` without presenting
  `{older_state}` as satisfying that boundary, checked by `{update_read_interleaving}`.

Use the illustrative revision-qualified proposal in Specify if targets are absent;
confirm with the user/stakeholder, including whether any staleness is acceptable.

## Rules of thumb

- Compare agreement only at the declared state boundary; different revisions must
  not be called contradictory snapshots without applying the chosen freshness rule.
- Define semantic equivalence for each compared field; different labels may agree,
  while identical labels can conceal different state meanings.
- Do not use mutual agreement as evidence of factual accuracy; two views can share
  the same wrong source and still satisfy their agreement contract.
- Keep the revision attached to the returned state; updating its label without
  updating its values fabricates agreement at a revision the view never held.

## Verification

Use paired-view fixtures, controlled update/read interleavings, and cache inspection.
Capture the same entity identifiers and the actual revision supplying each value.
Check semantic aliases, genuine conflicting values, and stale-but-identified reads.
Exercise authority unavailability under the declared read policy.
Retain initial cache contents, update events, failed refreshes, and raw responses.
Verify joined views under a common snapshot when that is the selected boundary.
Do not claim a coordination algorithm or lag bound from a successful sequential run.

## Done checklist

- [ ] Define authority and the entity/revision comparison boundary.
- [ ] Record semantic equivalence for compared fields.
- [ ] Capture initial and updated state from both read paths.
- [ ] Exercise an update while one view retains old state.
- [ ] Check that stale state is not relabeled as current.
- [ ] Test declared behavior when qualifying state cannot be read.
- [ ] Separate agreement findings from external-value correctness.
- [ ] State untested concurrency and propagation assumptions.

## Failure modes

- Comparing different snapshots as though they represented the same state.
- Stamping a new revision onto unchanged stale data.
- Equating identical strings with equivalent business meaning.
- Reporting aligned views as proof that the source value is true.

## References

- Read [agreement decisions](./references/design-guide.md) when repairing
  stale views, mixed snapshots, or semantic comparison.
- Read [order-view example](./references/worked-example.md) when checking
  revision-qualified agreement without inventing a global freshness guarantee.
