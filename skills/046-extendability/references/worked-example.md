# Worked example: add structured receipts to a core renderer

Imagine a receipt service with a core request dispatcher and a text renderer.
The user requests a structured receipt result alongside the existing text result.
Assume code and docs show no current formatter-extension contract; verify that
condition in a real project instead of inferring it from this scenario.

## Define the new meaning

Read dispatch, text rendering, caller parsing, and receipt contract tests.
Keep the old text operation unchanged. Define an explicit structured operation
whose result fields are accepted by the requesting consumer.
If a suitable formatter hook is discovered, route its use to the extensibility
sibling rather than editing core dispatch merely because this example does so.

Propose: "The receipt core shall add `{structured_operation}` through
`{approved_dispatch_and_renderer_surface}`, producing `{accepted_structured_fields}`
while existing text requests retain `{text_result_and_error_contract}`, verified
against `{old_and_new_consumer_cases}`."

Illustrative impact bound only: changes in at most 2 owner modules;
confirm with the user/stakeholder. Count other adapters and migrations explicitly
even if the approved production-module measure lists them separately.

Make the invented operation concrete: an old request with `result_kind=text`
still receives its existing text receipt. A new request with
`result_kind=structured` receives this separately accepted example shape:

```json
{"receipt_key":"synthetic-receipt","total_text":"example-total"}
```

Keep the example field meanings distinct from real pricing or receipt rules.
Returning that object for the old text selector would change the old contract,
even if the structured renderer's own assertion passes.

## Inspect an actual change surface

Use the owner/interface ledger below instead of counting renderer files alone.

If the implementation reuses the old text selector but returns a structure,
reject the claim that the old result contract was preserved. If every caller
needs a new format branch, report the wider ownership impact and reconsider
where dispatch belongs. A successful structured-render demo does not settle either issue.

Return the full change ledger, consumer evidence, and any unresolved scope exception.
This scenario does not establish real module ownership or a universal acceptable diff size.

## Example owner/interface ledger

These are fictional ownership decisions, not modules found in the user's project.

| Surface / owner | Actual addition or retained obligation | Evidence and impact decision |
| --- | --- | --- |
| Request dispatch / receipt-core | Add structured selector; keep text dispatch | Old request still selects text; count dispatch core edit |
| Structured renderer / receipt-core | Implement distinct object result | Accepted fields; count renderer core edit |
| Generated request schema / interface owner | Add explicit result variant | Diff generator input and output; disclose separate interface coordination |
| Existing text client / billing-client owner | No new selector branch | Unchanged client contract check; any required edit expands the envelope |
| New structured client / requesting owner | Opt into new selector | Consumer acceptance fixture; disclose caller work outside core count |

Compare this ledger with the full diff and dependency trace. The illustrative
owner-module limit stated above covers dispatch and renderer only; it does not
claim the interface or consumer work disappeared. If the generated schema forces
old clients to branch, obtain an expanded envelope or revisit dispatch/contract
placement. Ask the user whether that wider owner coordination is acceptable.
