# Repairing a domain-to-web dependency

This synthetic role organization and its acceptance criteria are illustrative;
confirm with the user/stakeholder before adopting them.

## Filled graph and behavior

| Input | Value |
| --- | --- |
| Elements | web/handler, web/format_response, domain/calculate |
| Role membership | web elements in delivery; domain/calculate in domain |
| Allowed role edges | delivery->domain, delivery->delivery |
| Forbidden edge | domain->delivery |
| Cycle policy | no directed dependency cycle in this fixture graph |
| Request | {amount_minor: 700} |
| Domain behavior | return accepted amount unchanged |
| Required web result | {status: accepted, amount_minor: 700} |
| Initial mutable state | none |
| Exceptions | none |
| Owner | application architecture maintainer role |

The numeric amount is an illustrative fixture value;
confirm with the user/stakeholder before using it as an acceptance example.

## Before edges and failure

```text
web/handler -> domain/calculate
domain/calculate -> web/format_response
web/format_response -> web/handler
```

Domain calculation calls the web formatter directly.
The formatter imports a handler constant, completing a directed cycle.
The request can still produce the expected response; correct behavior does not
remove the organizational violations.

Moving domain/calculate into a directory named core without changing those
relationships leaves the dependency problem intact.

## Remediation

Return a plain DomainResult from domain/calculate.
Have web/handler invoke web/format_response.
Move the formatter's required status literal into its own web responsibility,
removing its dependency on the handler.

## After actual graph and outputs

```text
web/handler -> domain/calculate
web/handler -> web/format_response
domain/calculate -> no web element
web/format_response -> no handler element
```

For request {amount_minor:700}:
domain output is {accepted_amount_minor:700};
web output is {status:accepted, amount_minor:700}.
No persistent state is created.
The graph has no domain->delivery edge and no directed cycle in this model.

## Failing dynamic-edge control

Keep the repaired imports, but register a domain callback targeting
web/format_response.
When calculation invokes it, the runtime graph again contains domain->delivery.
An import-only result cannot establish runtime organization for this mutant.
The broader check reports the forbidden callback edge.

## Limits

The fixture supports organization of the listed elements and inspected edge types.
It does not demonstrate independent deployment, all dynamic registrations, or
a universal prohibition on domain/delivery arrangements in other projects.
