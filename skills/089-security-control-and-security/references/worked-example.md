# Caller-controlled integration destination

This fictional export feature has a protected report and an approved destination
owned by its team. The modeled adversary is an authenticated caller able to alter
the requested destination, not an operator controlling the server or policy store.

## Inputs and misuse path

`report-slate` belongs to `team-amber`; `destination-mint` is approved for that team.
The attacker supplies `destination-coral`, which is not approved for the report.
Both a normal API path and a background retry path can reach the export effect.
The required contract preserves legitimate export to destination-mint.

| Input/path | Candidate control/output | Carried asset evidence |
| --- | --- | --- |
| Valid export to destination-mint | Confirmed team/destination check permits it | Approved report reaches approved recipient |
| Altered request to destination-coral | Reject before protected export effect | No report emitted to forbidden destination |
| Background replay of altered request | Same final-effect policy | No bypass through retry worker |
| Control dependency unavailable | Confirmed policy applied, not caller-supplied authority | Actual effect and unresolved availability trade-off |
| Alert after forbidden export | Detection may be observed | Prevention still failed |

## Requirement example

Illustrative modeled-path gate; confirm with the user/stakeholder:
Allow 0 successful modeled misuse paths across the agreed normal, replay, and
control-failure cases. This gate does not cover unmodeled attackers or prove the
feature broadly secure. Ask for the actual unavailable-policy behavior and authority.

## Interpretation and validation limits

Trace caller input to the final export, not only the interface validation.
An alert arriving after destination-coral received the report is detection evidence,
not successful prevention. Disabling every export avoids the effect but fails the
positive-control requirement unless the stakeholder explicitly changes that scope.
Use synthetic local fixtures under confirmed authorization; no live endpoint,
external destination, scanner, or real attack was exercised in this example.
