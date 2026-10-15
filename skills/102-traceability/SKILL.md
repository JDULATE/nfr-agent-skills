---
name: traceability
description: >-
  Connects requirements, decisions, changes, and evidence across revisions when users say "trace this requirement to its implementation and tests", "find what this change affects", or "these decision links are stale". Uses typed, versioned relationships and reverse navigation. Not for actor responsibility alone (see accountability), an independent examination verdict (see auditability), or whether tests can be controlled and observed (see testability).
---
# Traceability

## Definition and scope

Traceability means relationships connect requirements, decisions, changes and
evidence across their lifecycle. Preserve relationship meaning and revision;
distinguish who acted (`accountability`), whether evidence answers an examination
question (`auditability`) and practical test control/observation (`testability`).

## Use when / Don't use when

- Apply when implementation/test links are missing, superseded requirements point
  to old evidence, or a change cannot be followed backward to rationale and forward to impact.
- Route actor identity attribution to `accountability`.
- Route judging whether retained evidence supports a reviewer question to
  `auditability`; a navigable relationship is not automatically sufficient proof.

## Workflow

1. Clarify: Read requirement/decision docs, implementation code, test/evidence
   artifacts and revision history before creating relationship links.
   If identifiers or artifact versions are ambiguous, then Ask the user which
   authoritative revision and relationship semantics the trace must represent.

2. Specify: Name source/target artifact types, stable identities, relationship
   meaning, revisions, forward/reverse questions, lifecycle and orphan handling.
   If the user requests linkage repair, then propose this trace record:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Scope: selected requirement/decision through actual change and observed evidence artifacts.
   Edges: implements, motivates, verifies, supersedes; each must have reviewed meaning.
   Revisions: exact source/target versions; old evidence stays historical, not silently current.
   Trial gate: 0 unexplained orphan links in the agreed forward/reverse trace fixtures.
   Navigation: requirement -> implementation/evidence and changed artifact -> affected requirements.
   Evidence: relationship basis and actual result status, not merely a test-file pathname.
   Status: proposed trace scope, not proof the requirement itself is satisfied.
   ```

   Ask at most three groups about authoritative artifacts/revisions; relationship
   meanings and impact questions; and lifecycle, gaps or acceptance scope.
   Continue to a typed trace map without inventing missing relationship facts.
   If no criterion exists, then offer the illustrative orphan-link gate and
   confirm with the user/stakeholder before adopting its artifact/scope limits.

3. Design/Implement: Read [relationship practices](./references/design-patterns.md)
   when choosing stable IDs, revisioned edges or evidence-status links.
   If a requirement changes meaning, then separate superseded evidence from
   current verification needs; a working URL to an old test cannot update its coverage.
   If a link only says related, then identify the actual relationship or mark
   it unresolved before using it to assert implementation or verification impact.

4. Verify: Walk forward and backward from the agreed starting artifacts and
   inspect revision, edge meaning, actual target and result status.
   If navigation reaches an irrelevant or obsolete artifact, then retain a
   broken-semantic-link finding even when the file path technically resolves.

5. Report: Return the typed/revisioned map, repaired edges, forward/reverse
   findings, superseded evidence and orphan decisions.
   If a test link exists without relevant observed results, then report the
   link and missing verification separately instead of claiming the requirement passed.

## Specification patterns

- **Typed lineage:** For `{artifact_scope}`, connect `{source_and_target_revisions}`
  through `{reviewed_relationship_types}`, supporting `{forward_and_reverse_questions}`
  verified by `{semantic_walk_and_orphan_checks}`.
- **Change lineage:** After `{requirement_or_implementation_change}`, mark
  `{superseded_edges_and_evidence}` and identify `{current_verification_needs}`,
  verified by `{revision_aware_impact_walk}`.

Use the illustrative orphan-link gate when no criterion is supplied; confirm
with the user/stakeholder. Ask the user whether an absent relationship is a gap or an intentional boundary.

## Rules of thumb

- Do type the relationship instead of using related as a verification claim;
  a rationale edge and a passing-evidence edge support different trace questions.
- Do bind evidence to the requirement meaning and artifact revision it assessed;
  a valid historical result must not silently verify a changed obligation.
- Don't equate a resolving path with a correct trace; the linked function or
  test can exist while addressing a different requirement than the edge asserts.
- Do walk from changed code back to affected requirements as well as forward;
  a forward-only index can hide obligations whose implementation was removed.
- Do retain superseded lineage separately from current coverage; deleting old
  relationships can erase why a decision changed without repairing the new evidence gap.
- Don't mark an obligation satisfied because its test file is linked; the edge
  needs relevant result status and does not itself establish behavioral success.

## Verification

Use typed-link inspection, revision-history review and bidirectional impact walks.
Check stable identity, edge meaning, version, target relevance, result location
and actual outcome status. Include removed/superseded artifacts and intentional
scope exclusions. Record resolving-but-wrong links, missing reverse impact and
unexplained orphans; link count alone is not lifecycle evidence quality.

## Done checklist

- [ ] Define authoritative artifact identities, revisions and relationship types.
- [ ] Inspect each claimed edge's meaning and actual source/target relevance.
- [ ] Walk forward from requirements to implementation and relevant evidence.
- [ ] Walk backward from changes/removals to affected obligations and decisions.
- [ ] Separate superseded lineage and historical results from current coverage.
- [ ] Verify linked result status without equating a test pathname with a pass.
- [ ] Record unexplained or intentional orphans and current evidence gaps.

## Failure modes

- Using generic related links as proof of implementation or verification.
- Treating old evidence as current after the requirement meaning changes.
- Passing link checks while targets address the wrong obligation.
- Maintaining only forward links and missing impact from removed implementation.
- Reporting a requirement satisfied because a linked test file exists.

## References

- Read [relationship practices](./references/design-patterns.md) when defining
  edge meanings, stable IDs, revision transitions or reverse-impact checks.
- Read [approval-rule lineage example](./references/worked-example.md) when a
  changed requirement leaves historical tests valid but current coverage incomplete.
