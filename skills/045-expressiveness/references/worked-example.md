# Expressing owner-only and explicit denial

This is a synthetic local notation fixture.
Its semantic defaults are illustrative; confirm with the user/stakeholder.
It does not establish a secure authorization implementation.

## Filled semantic context

| Input | Value |
| --- | --- |
| Resource | report cedar, owner=alice |
| Actors | alice and bob |
| Action | read report cedar |
| Old representation | {read: true} for both everyone and owner-only intentions |
| Old evaluator | read=true returns allow for either actor |
| New allow forms | {kind:allow, subject:everyone} and {kind:allow, subject:owner} |
| New negative forms | {kind:deny} and {kind:absent} |
| Combining contexts | owner-only check: no inherited rule, no-decision denies; negative-choice check: inherited allow, explicit deny wins |
| Serialized format | fixture maps preserving every listed key/value |
| State | no mutable resource or actor state |
| Interpretation owner | policy-language maintainer role |

## Before: intentions collapse

The intention "allow alice as owner, no local decision for bob" serializes as
{read:true}, identical to allow-everyone.
Round-tripping cannot recover which intention was supplied.
Both actors evaluate to allow, so owner-only capability fails.

A request for explicit denial has no old form; omitting read produces no local
decision, which the inherited allow makes effectively allowed.

## Remediation

Introduce tagged allow/deny/absent forms and the owner relation.
Preserve them through storage and parsing.
Use the supplied evaluator and combining rule.

| Intention | Stored and parsed form | Alice local result | Bob local result |
| --- | --- | --- | --- |
| allow everyone | {kind:allow, subject:everyone} | allow | allow |
| owner-only local allowance | {kind:allow, subject:owner} | allow | no-decision |
| explicit denial | {kind:deny} | deny | deny |
| no local rule | {kind:absent} | no-decision | no-decision |

In the owner-only context, no inherited rule exists and no-decision denies.
Alice is effectively allowed and bob effectively denied, preserving the intended
distinction. Under a different inherited allow, the same local no-decision could
allow bob; representation capability does not establish an enforcement policy.

## After negative distinction

For actor bob with inherited allow:
{kind:deny} yields effective deny;
{kind:absent} yields effective allow.
Those intentions no longer collapse.

The resource remains report cedar/owner alice, and neither evaluation mutates it.

## Failing and migration controls

Store {kind:allow, subject:owner}, then deliberately drop subject while parsing.
The evaluator returns unsupported-rule rather than silently granting everyone.
The intended owner distinction is not established until the parser preserves it.

Input {kind:allow, subject:team} is unsupported and refused.
Old {read:true} explicitly migrates to {kind:allow, subject:everyone};
it is not reinterpreted as owner-restricted or denial.

## Limits

The fixture demonstrates local subject distinctions and explicit negative choice.
It does not express arbitrary relationships, prove enforcement, or resolve every
combination policy a project might require.
