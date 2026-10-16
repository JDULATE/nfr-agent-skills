# Inclusive discount boundary

All values and behavioral defaults in this synthetic fixture are illustrative;
confirm with the user/stakeholder before using them as requirements.

## Filled behavioral record

| Input | Value |
| --- | --- |
| Rule source | stakeholder fixture discount-rule revision maple |
| Operation | apply_discount(total_minor, coupon_state) |
| Illustrative threshold | 10000 minor units; confirm with the user/stakeholder |
| Illustrative discount | 1000 minor units; confirm with the user/stakeholder |
| Eligibility | unused coupon and total at least the threshold |
| Accepted output | applied, payable=total minus discount, next coupon state used |
| Below-threshold output | ineligible, payable unchanged, next state unused |
| Used-coupon output | refused-used, no payable result, coupon state unchanged |
| Initial persisted state | coupon cedar=unused |
| Effect boundary | fixture caller stores the returned coupon state |
| Owner | checkout feature maintainer role |

## Expected cases derived from the rule

| Input total / state | Expected result | Expected payable | Expected next state |
| --- | --- | --- | --- |
| 9999 / unused | ineligible | 9999 | unused |
| 10000 / unused | applied | 9000 | used |
| 10001 / unused | applied | 9001 | used |
| 10000 / used | refused-used | absent | used |

The equality expectation follows "at least," independently of the implementation.

## Before remediation

The old implementation applies the discount only when total is greater than
10000, despite the inclusive rule.
At total=10000 and coupon=unused it returns:
`{result: ineligible, payable: 10000, coupon_state: unused}`.
The caller stores unused. Both eligibility and resulting state violate the table.
The 9999 and 10001 cases alone would not detect the equality defect.

## Change and after state

Replace the strict acceptance predicate with the inclusive one expressed in
the design sketch. Start the equality run again with coupon cedar=unused.

```text
input: total_minor=10000, coupon_state=unused
returned: {result: applied, payable: 9000, coupon_state: used}
caller persisted state: coupon cedar=used
```

Run the below and above cases with separate reset coupons:
9999 returns ineligible/9999/unused;
10001 returns applied/9001/used.
These neighboring cases retain their specified behavior.

## Repeated-operation negative

Carry coupon cedar=used from the accepted equality run.
Call again with total_minor=10000.
The result is refused-used, no payable field, and coupon cedar remains used.
A broken implementation returning applied/9000 would violate the state precondition
even if its arithmetic matched the accepted case.

## Separate output/state failure

From a reset unused coupon, a mutant returns applied/9000 but leaves state unused.
Output-only checking would pass; the state comparison rejects it.
This control demonstrates why both declared observables are required.

## Limits

The fixture checks the enumerated valid inputs and used-state refusal.
It does not define negative totals, currency conversion, concurrent redemption,
or persistence failures. Those require contract decisions and separate evidence,
not extrapolation from this pure sequential model.
