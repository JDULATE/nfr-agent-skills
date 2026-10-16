# Independent reconstruction decisions

Use this guide when another executor must rebuild the procedure from its handoff.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A local default changes the calculation. | Put the semantic setting in the package and reject an omitted value. Setup becomes more explicit. | Reconstruct with a clean environment and inspect the effective setting. |
| The handoff reads the author's private working directory. | Supply the required input artifacts or declare an authorized source. The package may grow. | Deny access to that directory and follow the published setup. |
| Another runner merely downloads the reference result. | Separate executable procedure and inputs from the comparison artifact. Independent computation takes work. | Inspect the newly produced output and its invocation record. |
| Setup succeeds only after a private author fix. | Record the intervention and revise the public handoff. The first attempt remains an assisted failure. | Repeat reconstruction using the revised handoff without that intervention. |
| Platforms differ in an unexamined dependency. | Declare the required capability and test the supported reconstruction boundary. Some environments may remain outside scope. | Inspect the independent executor's capability result and report unsupported differences. |

## Package-driven sketch

```text
package = read_declared_handoff()
require package.include_adjustments is explicitly set
fixture = package.ledger_rows
result = sum_rows(fixture, package.include_adjustments)
write_new_output(result, effective_setup)
compare_with_predeclared_contract(result)
```

Do not implement sum_rows by copying the comparison result.
The independent executor needs the procedure's meaning, not just a filename
that happens to exist on the author's machine.

## Attempt record

Identify executor, starting workspace, declared resources, effective semantic
settings, actions performed, produced result, and assistance.
Keep a failed setup in that record even if a revised handoff later succeeds.

If no independent executor is available, prepare the package and report the
reconstruction claim unverified. Do not relabel an author-only replay.
