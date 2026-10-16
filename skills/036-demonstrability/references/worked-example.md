# Declined-payment demonstration

Read this example as an illustrative synthetic scene, not a payment-system guarantee.
All fixture quantities and acceptance proposals are illustrative examples;
confirm with the user/stakeholder before applying them to a project.

## Filled scene record

| Field | Fixture value |
| --- | --- |
| Claim | A declined synthetic payment shows refusal and creates no charge in this scene. |
| Audience | Feature reviewers who can open the demo screen and synthetic ledger receipt. |
| Feature path | Local checkout submit handler and its charge-write branch. |
| Provider boundary | Simulated response adapter; no live payment provider is contacted. |
| Scene / attempt / order | scene-decline / attempt-red / order-fern |
| Initial order | awaiting-payment; total 24 credits |
| Initial charge state | no charge for order-fern |
| Initial prior attempts | empty |
| Input | submit order-fern with adapter response declined |
| Expected screen | Payment declined; order still awaiting-payment |
| Expected state | attempt-red recorded as declined; no charge for order-fern |
| Forbidden effect | charge record created for the declined attempt |
| Carry after showing | declined attempt record remains until synthetic reset |
| Reset | restore awaiting-payment order, empty attempts, and empty charges |
| Artifact | scene-decline receipt with scene, attempt, order, provider mode, message, charge state |

## Failing showing before remediation

The original scene displays "Payment declined" after submission.
Its exported receipt contains only:
```text
scene=scene-decline
provider_mode=simulated
message=Payment declined
```

Reviewers see the message but cannot inspect whether a charge exists.
The scene fails its inspectability requirement even if the handler happens to be
correct. No charge defect is established by this missing evidence.

## Remediation and after evidence

Keep the same input and handler, and add a read-only receipt query after submit:
```text
scene=scene-decline
attempt=attempt-red
order=order-fern
provider_mode=simulated
message=Payment declined
order_state=awaiting-payment
attempt_result=declined
charge_state=absent
```

The audience can now compare the refusal and resulting state in the same scene.
Reset the synthetic records, rerun submit, and inspect a new receipt with that
scene identity. A missing charge-state field still fails the showing.

## Contrasting scene

Load scene-paid with order-moss, total 24 credits, state awaiting-payment,
empty attempts, and empty charges. Submit attempt-green with simulated response
approved. The expected receipt identifies scene-paid, attempt-green, order-moss,
provider_mode=simulated, order_state=paid, attempt_result=approved, and one
charge for 24 credits tied to that attempt.

A refusal receipt accidentally attached to scene-paid must be rejected.
This identity check prevents unrelated scenes from supplying each other's result.

## Requirement example

The demonstration package shall let feature reviewers inspect the refusal
message and charge absence for scene-decline after executing its recorded input,
with provider simulation visible in the screen and receipt.

## Limits

These scene receipts illustrate evidence shape; they are not observations from
this repository's payment implementation. The pair shows local response handling,
not every payment state, live-provider integration, or a proof of absence of charges
under concurrency. Keep those claims outside the demonstration result.
