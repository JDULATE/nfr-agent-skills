# Operational-history practices

Assess demonstrated readiness without inventing maturity levels or a universal age threshold.

## Intended-use exposure ledger

- Use when older operation is proposed as evidence for expanded use.
- Trade-off: splitting episodes by feature, version, workload, and audience takes
  effort but prevents unused capabilities inheriting unrelated deployment history.
- Verify: connect each actual operating episode to exercised behavior and context;
  identify idle, unobserved, and newly introduced paths separately.

## Defect lineage across releases

- Use when the same symptom or causal defect recurs under new ticket identities.
- Trade-off: grouping too broadly can merge distinct causes; grouping too narrowly
  makes administrative closure look like operational resolution.
- Verify: compare cause, affected path, revision, and recurrence evidence, retaining
  uncertainty where linkage is unproven instead of inventing a clean or common lineage.

## Repair and operating follow-up

- Use when closed defects or merged patches support readiness claims.
- Trade-off: a focused regression can verify the fix path but does not supply
  relevant post-fix operation that never occurred or was not observed.
- Verify: link fix revision, reproduction/check result, deployed use, and any
  recurrent incident; distinguish code-fixed, verified, followed-up, and still unknown.

## Evidence scope and readiness gaps

- Use when a release/context changes materially or the history is incomplete.
- Trade-off: conditional readiness can preserve useful experience while exposing
  new-use gaps; a single maturity score hides which capability lacks demonstrated use.
- Verify: compare readiness conditions with actual history and observation quality;
  list proposed qualification work separately from demonstrated episodes.
