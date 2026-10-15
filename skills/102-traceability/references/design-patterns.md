# Relationship practices

Give links lifecycle meaning and revision context, not just destinations.

## Typed edge record

- Use when one artifact can motivate, implement, verify or supersede another.
- Trade-off: explicit relationship types need review; a single related edge is
  cheaper but cannot distinguish rationale, implementation and result evidence.
- Verify: inspect why the edge exists, its source/target identities and revisions,
  and which actual forward/reverse question that relationship can answer.

## Requirement change and historical evidence

- Use when obligation meaning changes while old tests or decisions remain relevant history.
- Trade-off: preserving history adds lifecycle states; reusing the same identifier
  without revision can silently promote obsolete evidence to current coverage.
- Verify: compare old/new meaning, mark superseded edges and identify unverified
  current obligations without deleting why the earlier result existed.

## Reverse impact walk

- Use when implementation or evidence is changed or removed.
- Trade-off: maintaining reverse relationships adds work, but a forward index can
  leave removed implementations unnoticed by the obligations they formerly served.
- Verify: start at the changed artifact, walk to affected requirements/decisions,
  and distinguish intentional retirement from unexplained orphaning.

## Semantic target and outcome check

- Use when automated link checking reports success.
- Trade-off: resolving paths are useful but cannot establish relevance or a passed
  behavioral result; deeper review needs artifact content and evidence status.
- Verify: open the actual target, compare its addressed obligation/revision, and
  retain observed result status separately from test-file or implementation existence.
