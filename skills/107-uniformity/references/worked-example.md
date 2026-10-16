# Uniform pagination across list peers

This synthetic convention, fixture values, and acceptance defaults are illustrative;
confirm with the user/stakeholder before adopting them.

## Filled peer record

| Input | Value |
| --- | --- |
| Comparable peers | list-products and list-orders |
| Shared operation | return the first requested count of items in fixture order |
| Selected convention | canonical field page_limit means item count |
| Accepted legacy alias | pageSize on both peers |
| Conflict rule | unequal canonical and alias values return ConflictingLimit |
| Product items | [pen, book, lamp] |
| Order items | [cedar, maple, oak] |
| Initial persistent state | none; listing is read-only |
| Similar but excluded operation | export-bytes uses byte_budget, not item count |
| Owner | list-interface maintainer role |

## Before peer divergence

Input {page_limit:2} yields products=[pen,book].
The orders handler reads only pageSize and returns MissingLimit.
The operations are comparable under the selected convention, so the peer surface
is not aligned despite matching documentation.

All quantities and lists are illustrative fixture values;
confirm with the user/stakeholder.

## Remediation

Make both handlers use the canonical parser and apply its item-count result.
Retain pageSize as the documented compatibility alias on both.
Keep the same conflict rule at each surface.

| Input | list-products result | list-orders result |
| --- | --- | --- |
| {page_limit:2} | [pen,book] | [cedar,maple] |
| {pageSize:2} | [pen,book] | [cedar,maple] |
| {page_limit:2, pageSize:2} | [pen,book] | [cedar,maple] |
| {page_limit:2, pageSize:1} | ConflictingLimit | ConflictingLimit |

Each run starts with the filled lists and produces no persistent mutation.
The contents differ appropriately; uniformity concerns the interaction convention,
not equal product and order values.

## Failing handler control

Update orders documentation and parser, but leave its selection code using an
unrelated fixed count of 1.
The canonical request returns only [cedar], failing the declared common operation.
Shared parser code alone does not establish uniform behavior.

## Semantic exception

export-bytes has input {byte_budget:2} and a supplied byte buffer [97,98,99,100].
It returns prefix [97,98] under its byte-budget fixture rule.
That operation is not an item-count list peer and keeps byte_budget.
Relabeling it page_limit would misleadingly suggest an equivalent quantity.

## Limits

The example covers the declared pagination convention and alias behavior only.
It does not select a convention for other teams, establish value agreement,
or demonstrate every paging operation or encoding.
