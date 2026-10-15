# Worked example: attach a formatter through an existing hook

Assume a fictional report host documents a formatter contract: receive the report
model, return a formatted result, and register under a unique format key. Its
configuration already selects registered formatters without changing host source.
These are scenario assumptions to verify in the real code and documentation.

## Establish the pre-existing contract

Read host dispatch, registration schema, formatter docs, and built-in tests.
Ask what report fields the hook exposes, what result it accepts, and whether a
restart or particular cleanup transition is documented for registration changes.
Do not add those lifecycle promises merely because the user asked for a plugin.

Propose: "A conforming `{requested_formatter}` shall register through
`{existing_format_key_contract}` and produce `{accepted_result}` from
`{documented_report_model}`, without core source changes, verified by
`{independent_fixture_host_diff_and_retained_formatter_cases}`."

Illustrative host-edit target only: 0 core edits per conforming addition;
confirm with the user/stakeholder. Declare extension-owned files and allowed
registration changes separately so the accounting cannot hide a host modification.

## Exercise the seam

Implement a small synthetic formatter using only the documented report model.
Register it through the existing configuration route and invoke ordinary host
dispatch. Add an invalid result case to check the host's declared rejection behavior.

For a concrete invented contract fixture, define input
`{"heading":"demo","rows":["A"]}` and require a text result. Register the format
key `bracketed` through the existing route; its accepted output is `[demo] A`.
Return a list instead of text in a negative fixture and inspect the documented
rejection. These fields, key, and rejection expectation belong to this hypothetical
contract, not a general formatter protocol or an asserted host capability.

| Observation | Interpretation |
| --- | --- |
| New key dispatches through existing registration | Evidence that the route admits this implementation |
| Host source now names the new formatter class | A core change, not unchanged-core admission |
| Fixture requires an undocumented host cache | A missing or misrepresented contract dependency |
| Existing formatter output changes after registration | Investigate a dispatch or lifecycle interaction |
| Removal needs the documented restart | Record that lifecycle boundary rather than claiming hot removal |

If the report model lacks a field required by the requested result, report that
contract gap and route the foundational core addition to the extendability sibling.
Report evidence for this contract and host revision only, not universal plugin support.

## Failed activation and cleanup fixture

Assume this fictional pre-existing lifecycle includes activation that acquires a
subscription and temporary output handle, plus host-invoked cleanup on failure.
Verify those promises in the real hook; absent support is a contract gap, not a
reason to silently patch the host and claim admission through the original hook.
Keep a retained formatter working, record the registry and live resource owners,
then fail the synthetic formatter after acquisition but before activation completes.
Invoke the documented failure path. Check the temporary handle is closed, the
subscription detached, and the failed key unavailable for dispatch; run the
retained formatter and compare its output with the starting result.
Retry through the same registration route and inspect for duplicate subscriptions
or keys. If cleanup cannot finish, require the declared residual-state/restart
procedure rather than assuming hot removal. New host-specific cleanup edits mean
this fixture did not fit the pre-existing lifecycle contract.
