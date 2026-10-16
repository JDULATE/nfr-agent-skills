# Export coverage despite matching counts

This synthetic fixture uses illustrative membership and coverage criteria;
confirm with the user/stakeholder before adopting them.

## Filled universe

| Input | Value |
| --- | --- |
| Source revision | inventory amber, fixed for the whole traversal |
| Source ordered rows | cedar, maple, oak |
| Membership predicate | every row in inventory amber |
| Required identities | {cedar, maple, oak} |
| Representation criterion | emitted export row with the same identity |
| Initial cursor | none |
| Illustrative page capacity | 2 rows; confirm with the user/stakeholder |
| Continuation contract | after a nonterminal page, continue after its last emitted source identity |
| Duplicate policy | not accepted, reported independently |
| Unexpected-member policy | report separately; never offsets missing members |
| Initial output state | [] |
| Owner | export feature maintainer role |

## Before remediation

The first page reads [cedar, maple].
The faulty cursor advances after oak, an unread row, so the next page is empty.
A separate faulty page-join path appends the last emitted row again.

```text
first page output: [cedar, maple]
joined output: [cedar, maple, maple]
next cursor: after oak
next page: []
final export: [cedar, maple, maple]
```

Required and observed row counts both equal 3.
Identity comparison instead finds missing={oak}, duplicates={maple:2},
unexpected={}. Equal counts fail the declared requirement.

These faults are explicitly supplied by the fixture; count equality alone would
not establish which cursor or join path caused a real omission.

## Remediation and after carried state

Advance after the last source identity actually emitted by the page.
Append each returned page once.

| Stage | Cursor before | Source page | Output after append | Cursor after |
| --- | --- | --- | --- | --- |
| initial | none | [cedar, maple] | [cedar, maple] | after maple |
| final page | after maple | [oak] | [cedar, maple, oak] | terminal |

The required set remains inventory amber throughout.
After comparison: missing={}, duplicates={}, unexpected={}.
Coverage passes for this declared set; field-value correctness is not evaluated.

## Independent negative controls

With observed=[cedar, maple, birch], comparison yields missing={oak},
unexpected={birch}, duplicates={}.
The extra birch does not substitute for oak.

With observed=[cedar, maple] and traversal interrupted before the final page,
missing={oak}; traversal status remains incomplete.
Do not relabel oak as excluded after the run.

## Requirement example and limits

For inventory amber, every required identity shall appear at the export boundary;
duplicates and unexpected identities shall be reported independently.
This requirement is illustrative; confirm with the user/stakeholder.

The fixture establishes membership coverage only against the supplied source.
It does not show a real database snapshot mechanism, changing-source coverage,
or correctness of any exported non-identity fields.
