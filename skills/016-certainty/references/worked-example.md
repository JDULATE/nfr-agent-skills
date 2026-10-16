# Delivery claim qualification

This synthetic fixture uses illustrative qualitative policy defaults;
confirm with the user/stakeholder before adopting them.
No probability or real delivery guarantee is asserted.

## Filled claim record

| Input | Value |
| --- | --- |
| Requested claim | parcel-cedar has been delivered |
| Authoritative source | receiver-ledger fixture |
| Evidence match | parcel cedar; delivery proposition, with delivered or not-delivered assertions |
| Validity | record is in current ledger revision birch |
| Compatible evidence | delivered assertion for the requested parcel |
| Conflict rule | current delivered and not-delivered assertions conflict |
| Labels | supported, unverified, conflicting, contradicted |
| UI mapping | supported: supported delivery; unverified: delivery unverified; conflicting: delivery evidence conflicts; contradicted: delivery contradicted |
| Allowed action | show status; do not trigger automated settlement |
| Initial cached state | no cache entry |
| Policy revision | claim-policy maple |
| Owner | tracking feature maintainer role |

## Before: missing evidence promoted

Input evidence is [].
The old code initializes label=confirmed and replaces it only on a found record.
API output is `{parcel: cedar, delivery: confirmed}`.
UI says `Delivery confirmed`.

The empty ledger cannot support the requested claim under the declared policy.
The fixture identifies the defaulting path; it makes no claim that the parcel
was in fact delivered or not delivered.

## Remediation and after cases

Replace the unconditional default with explicit qualification.
Each row starts with no cache entry and the same requested claim.

| Evidence in current revision birch | Qualified output | UI text | Carried output state |
| --- | --- | --- | --- |
| [] | unverified | Delivery unverified | cedar/unverified/maple/birch |
| [cedar, delivered, source receiver-ledger] | supported | Supported delivery | cedar/supported/maple/birch |
| [cedar, dispatch, source receiver-ledger] | unverified | Delivery unverified | cedar/unverified/maple/birch |
| [oak, delivered, source receiver-ledger] | unverified | Delivery unverified | cedar/unverified/maple/birch |
| [cedar, not-delivered, source receiver-ledger] | contradicted | Delivery contradicted | cedar/contradicted/maple/birch |
| [cedar, delivered] and [cedar, not-delivered], both receiver-ledger | conflicting | Delivery evidence conflicts | cedar/conflicting/maple/birch |

For the conflict row both records have revision birch.
Neither record is counted as a stronger vote because the assertion is repeated.
The dispatch row can support a separate dispatch claim, not delivery.

## Cached-status failing branch

Start with cached cedar/supported/maple/amber based on an amber delivery record.
Current revision is birch and contains no cedar evidence.
Under the illustrative refresh contract, mismatched evidence revision requires
qualification again before display; confirm with the user/stakeholder.
The old cache-only display says supported and fails that contract.
The revised path returns cedar/unverified/maple/birch and displays
`Delivery unverified`.

## Requirement example and limits

For parcel cedar, delivery wording shall retain unverified or conflicting status
unless matching current authoritative evidence supports delivery.
This proposal is illustrative; confirm with the user/stakeholder.

The fixture covers missing support, mismatched claims, contrary evidence, conflicts, and cache
qualification. It does not establish the truthfulness of receiver-ledger,
a refresh time budget, or calibrated probability of delivery.
