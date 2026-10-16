# Order list and detail agreement

This synthetic fixture uses illustrative coordination defaults;
confirm with the user/stakeholder before adopting them.

## Filled agreement record

| Input | Value |
| --- | --- |
| Entity | order cedar |
| Authority history | amber: packed; birch: shipped |
| Initial active authority revision | amber |
| Initial detail response | cedar/amber/packed |
| Initial list cache | cedar/amber/packed |
| Update | activate authority revision birch with state shipped |
| Required read boundary after update | exact revision birch |
| List spelling | sent denotes shipped; boxed denotes packed |
| Detail spelling | shipped and packed |
| Equivalence | sent=shipped; boxed=packed; packed differs from shipped |
| Authority support | read_at(cedar, birch) returns shipped while available |
| Unavailable policy | return unresolved(birch), not qualifying data |
| Owner | order-view maintainer role |

## Before remediation

Activate authority birch while leaving list cache unchanged.
Detail returns cedar/birch/shipped.
List returns cedar/amber/boxed without exposing the stale revision to the caller.
The pair does not satisfy the requested birch read boundary.

If the list merely stamps birch onto boxed, it instead creates an actual
same-revision disagreement: birch/boxed versus birch/shipped.
Neither failure is repaired by mapping boxed to packed.

## Remediation and after carried state

Validate cached revision before returning a requested-revision result.
Fetch available authority state and map it to the list vocabulary.

```text
requested revision: birch
cache before: cedar/amber/packed
authority result: cedar/birch/shipped
cache after: cedar/birch/shipped
detail response: cedar/birch/shipped
list response: cedar/birch/sent
equivalence result: agree
```

The raw labels differ, but the agreed state meaning matches.
The cached state and revision are replaced together in this model.

## Authority-unavailable failing branch

Reset cache to cedar/amber/packed, keep requested revision birch,
and make read_at unavailable.
The corrected path returns unresolved(birch), retaining cache cedar/amber/packed.
It does not return boxed as satisfying birch, and it does not count the read as
successful agreement evidence.
The old path would have returned stale qualifying data and failed the policy.

## Wrong-source control

Set both birch views to packed under an alternative filled source.
They agree with each other, but this observation alone cannot establish whether
packed is the real state of the order.
Reference truth is outside the agreement contract.

## Limits

The trace exercises a sequential history with available exact-revision reads.
It does not implement network coordination, guarantee freshness across all
clients, or measure propagation delay under concurrent updates.
