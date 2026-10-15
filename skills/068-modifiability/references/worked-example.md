# Worked example: changing a stored status label

Suppose a fictional parcel service changes its stored status label from `ready`
to `dispatchable`. The intended behavior is agreed separately: consumers must
recognize the new label without changing which parcels qualify for dispatch.
The scenario asserts no real logistics rule or existing database capability.

Read the label writer, schema, selector, export consumer, and ownership docs.
Propose: "Implementing `{status_label_edit}` shall stay within
`{confirmed_owner_and_contract_envelope}`, preserve `{parcel_eligibility}`, and
account for `{generation_migration_and_verification_work}`, evidenced by
`{complete_diff_consumer_cases_and_work_ledger}`."

Illustrative scope only: 2 production owner components;
confirm with the user/stakeholder. This proposed count does not remove work
outside that surface, establish an effort limit, or predict delivery duration.

| Surface | Initial prediction | Synthetic rehearsal discovery / required evidence |
| --- | --- | --- |
| Label writer / parcel owner | Local string edit | Changed output passes through the public write path |
| Dispatch selector / dispatch owner | Recognize new label | Before/after eligibility agrees for retained parcels |
| Export reader / reporting owner | No impact predicted | Reader filters stored `ready`; semantic dependency missed |
| Historical rows | No work predicted | Need an agreed reader/migration policy; not silently reinterpreted |
| Contract tests and generated fixtures | Supporting work | Include updates and retained-case checks in the total ledger |

The export reader need not import the writer to depend on its stored meaning.
Its discovery expands the owner/contract envelope. Report the failed prediction
and obtain the scope decision rather than hiding that reader outside the source count.

| Work category | Evidence in the rehearsal ledger |
| --- | --- |
| Investigation | Dependency trace that discovers reporting's label filter |
| Implementation | Writer and selector diffs; reporting fix separately exposed |
| Migration | Chosen old-row meaning and conversion/reader evidence |
| Verification | Retained parcel cases and export-consumer observations |
| Coordination / waiting | Reporting owner's decision and elapsed wait kept distinct |

Keep measured time in a stakeholder-agreed unit; these task entries are not invented
hours or observations of a real team. A completed code edit with unresolved old-row
semantics is not a demonstrated bounded modification. Return forecast errors,
actual changed owners, effort evidence or its absence, and untested consumers.
