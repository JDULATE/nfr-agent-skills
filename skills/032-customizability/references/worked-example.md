# Worked example: an authored parcel layout

Assume a fictional renderer accepts literal text plus `[[parcel]]` and `[[depot]]`.
These are invented delimiters for this example, not syntax promised by any real
engine. Unknown tokens and incomplete delimiters reject rendering under this
proposed contract; no private host fields are exposed.

Illustrative scope only: 1 user-authored layout beyond built-in presets;
confirm with the user/stakeholder before adopting this grammar or coverage.
Propose: "An author shall save `{layout_artifact}` and invoke `{selected_revision}`
through `{normal_render_path}`, producing `{expected_text}` from `{public_inputs}`,
with `{invalid_expression_response}` verified separately."

```json
{"parcel":"parcel-green","depot":"east"}
```

| Artifact/selection state | Concrete result under the proposed contract |
| --- | --- |
| Selected `approved`: `Delivery [[parcel]]` | `Delivery parcel-green` |
| Saved `draft`: `Parcel [[parcel]] -> [[depot]]` | Preview: `Parcel parcel-green -> east` |
| Normal invocation still selects `approved` | `Delivery parcel-green`; new customization is not active |
| Selection explicitly moved to `draft` | Normal invocation: `Parcel parcel-green -> east` |
| Selected content references `[[account_note]]` | Rejected unsupported input; no plausible partial output |
| Selected content ends with `[[parcel` | Rejected invalid artifact under the example grammar |

Carry artifact identity, saved content, selection, and invoked revision through
the fixture. The draft result must derive from authored literals and substitutions,
not a host branch that notices a customer name and emits a built-in string.
If rendering needs fields absent from the public model, expose that contract gap;
if a new hook is needed, separate that host work from the authoring demonstration.
The fixture establishes a testable custom result, not permission to execute code
or compatibility with any installed report renderer.
