# Confirmed document after restart

This fictional save promise covers process restart while the underlying store
survives. It does not cover device destruction, storage loss, or site loss.

## Inputs and acknowledgement ledger

Document `doc-slate` starts with version `rev-before`, content `draft`.
Save `save-amber` proposes `rev-confirmed`, content `reviewed`; its completion
acknowledgement is observed and retained in a separate test ledger.
A later attempted save `save-mint` with content `unconfirmed` has no known response.
Do not silently count it as acknowledged or assume it could not have committed.

| Checkpoint | Required comparison | Carried evidence |
| --- | --- | --- |
| save-amber acknowledged | Expected confirmed content reviewed | Identity/version and promise point |
| Process stopped and restarted | Exercise the declared event | Store-survival assumption retained |
| Authoritative post-restart read | Confirm required acknowledged preservation | Actual identity/version/content |
| Unknown save-mint resolved | Separate legitimate supersession from loss | Attempt/acknowledgement distinction |

## Requirement trial

Illustrative preservation gate; confirm with the user/stakeholder:
Permit 0 missing acknowledged versions under the agreed event and supersession
rules. Confirm whether the promise requires the latest valid state or queryable
history; the gate does not silently require historical retention.

## Interpretation and rejection

If no valid later write exists, `rev-before` after restart contradicts the confirmed
save promise. If save-mint validly superseded save-amber, inspect that commit and
apply the agreed current-state/history rule instead of automatically declaring loss.

A warm pre-restart read of `reviewed` proves visibility at that point, not survival.
A clean process restart cannot support an untested destroyed-store promise.
The example proposes an oracle and event boundary; it supplies no real storage result.
