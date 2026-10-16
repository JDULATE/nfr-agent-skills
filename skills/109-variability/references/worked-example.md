# Bounded edition family

This synthetic product family, feature constraints, and coverage criteria are
illustrative; confirm with the user/stakeholder before adopting them.

## Filled model

| Input | Value |
| --- | --- |
| Family | inventory-tool build editions |
| Variation points | store=local or remote; sync, audit, export each false or true |
| Defaults | none; every selection explicitly supplies every field |
| Binding stage | build request before emitting artifacts |
| Constraint | sync implies store=remote |
| Constraint | export implies audit |
| Derivation | store module plus each enabled sync/audit/export module |
| Initial artifact state | [] for every build |
| Refusal order | sync/store check, then export/audit check |
| Owner | edition-build maintainer role |

## Before failure

Input {store:local, sync:false, audit:false, export:true}.
Old build code emits [local-store, export] without checking the audit requirement.
The emitted variant violates export implies audit.

## Remediation and selection-space record

Validate all constraints before emitting modules.
The following table enumerates the complete filled space.
Values and counts are illustrative fixture data; confirm with the user/stakeholder.

| store | sync | audit | export | Validity |
| --- | --- | --- | --- | --- |
| local | false | false | false | valid |
| local | false | false | true | invalid |
| local | false | true | false | valid |
| local | false | true | true | valid |
| local | true | false | false | invalid |
| local | true | false | true | invalid |
| local | true | true | false | invalid |
| local | true | true | true | invalid |
| remote | false | false | false | valid |
| remote | false | false | true | invalid |
| remote | false | true | false | valid |
| remote | false | true | true | valid |
| remote | true | false | false | valid |
| remote | true | false | true | invalid |
| remote | true | true | false | valid |
| remote | true | true | true | valid |

## After actual derivation cases

For {store:local, sync:false, audit:false, export:false},
result=[local-store], artifact state=[local-store].

For {store:remote, sync:true, audit:true, export:true},
result=[remote-store,sync,audit,export], with the same artifact state.

For the original invalid export selection,
result=Refused(export-needs-audit), artifact state=[].
For {store:local, sync:true, audit:true, export:false},
result=Refused(sync-needs-remote), artifact state=[].

## Direction and omission controls

{store:local, sync:false, audit:true, export:false} is valid and derives
[local-store,audit]. Audit does not force export.

A mutant accepts the all-enabled remote selection but emits
[remote-store,sync,audit], dropping export.
Validity checking passes while artifact comparison fails; both checks are needed.

## Limits

The table defines validity for this bounded model.
Only the listed derivation cases have filled output traces here; the table alone
is not execution evidence for all builds.
No live configuration transition, migration, or external feature-model standard
is implied.
