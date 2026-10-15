# Restoring an order store with overlapping replay

This fictional snapshot contains completed order `order-slate`. Replay input
contains the same logical order plus pending `order-amber`. The example contract
requires each accepted order's intended effect without replayed duplicates.

## Inputs, output, and recovery state

| Milestone | Input/action | Expected output/state |
| --- | --- | --- |
| Disruption observed | Service unusable | Recovery clock starts; target isolated |
| Bootstrap | Obtain declared artifacts/keys/config | Restore dependencies available |
| Snapshot import | order-slate already included | Coherent base state, not yet recovered service |
| Replay inspection | order-slate overlaps; order-amber pending | Stable identities classified before applying work |
| Reconciled replay | Do not duplicate order-slate; resolve order-amber | Required order state/effects checked |
| Journey validation | Read/act through recovered business path | Agreed usable result plus state/loss verification |

## Requirement proposal

Illustrative deadline; confirm with the user/stakeholder:
Reach the agreed restored journey/state within 30 minutes from disruption observed.
Ask for the loss allowance and acknowledged-state obligations; snapshot cadence
cannot define them. A timing pass cannot compensate for missing required orders.

## Negative traces and carried uncertainty

If import succeeds but credentials prevent the journey, recovery remains incomplete.
If replay applies order-slate again, inspect actual effects rather than accepting
a normal row count or healthy process. If order-amber may already have caused an
external effect, classify that uncertainty before retry; the example supplies no
external deduplication primitive and cannot promise exactly-once execution.

Retain bootstrap, import, replay, and validation timestamps through the agreed
endpoint. Disclose a rehearsal that preloaded keys unavailable in the declared
scenario. No backup restore, elapsed result, or recovered state was measured here.
