---
name: <slug>
description: <third person; what it does + WHEN to use it + 3-6 trigger phrases + one Not for X (see sibling-slug) clause; max 1024 chars>
status: todo
---
# <NFR name>

## Definition and scope

<Write 2-3 sentences defining this NFR.>
<State what is in scope and out of scope.>
<Distinguish the nearest siblings by slug.>

## Use when / Don't use when

<List concrete trigger signals.>
<List concrete non-triggers and route each to a sibling slug.>

## Workflow

1. Clarify: <Read the existing codebase and docs; ask about missing context.>
   <If context is missing, then Ask the user before specifying it.>

2. Specify: <Write measurable requirements with acceptance evidence.>
   <If no target is supplied, then propose an illustrative example and confirm with the user/stakeholder.>

3. Design/Implement: <Choose changes specific to this NFR.>
   <If a tradeoff affects a sibling NFR, then record it and ask for a priority.>

4. Verify: <Execute the concrete checks below.>
   <If a check fails, then repair the cause and repeat the affected check.>

5. Report: <Report evidence, limitations, and open decisions.>
   <If evidence is missing, then mark the requirement unverified.>

## Specification patterns

<Write 2-3 requirement templates with placeholders.>

The system shall <behavior> under <condition>, measured by <metric> at <target>.

<Provide an evidence and acceptance pattern for this NFR.>

<Label example numbers illustrative and pair them with confirm with the user/stakeholder.>

## Rules of thumb

- <Do: add a code or architecture rule specific to this NFR.>
- <Do: add a distinct rule.>
- <Do: add a distinct rule.>
- <Don't: add a specific prohibited pattern.>
- <Don't: add a distinct prohibited pattern.>

<Use 5-10 specific Do / Don't items; remove interchangeable advice.>

## Verification

<Name concrete test types and the evidence each produces.>

<Specify code or design review checks.>

<Name runtime signals and explain how to interpret them.>

<Name tool categories; include a specific tool only when verified.>

## Done checklist

- [ ] <Add an objectively checkable NFR-specific item.>
- [ ] <Add an objectively checkable NFR-specific item.>
- [ ] <Add an objectively checkable NFR-specific item.>
- [ ] <Add an objectively checkable NFR-specific item.>
- [ ] <Add an objectively checkable NFR-specific item.>
- [ ] <Add an objectively checkable NFR-specific item.>

<Use 6-10 items; keep long supporting checklists in references.>

## Failure modes

- <Describe a common mistake and how to detect it.>
- <Describe a different mistake and how to detect it.>
- <Describe a false positive and how to reject it.>

<Use 3-6 failure modes.>

## References

<Link files directly under ./references/ with read when guidance.>
<Include a short worked example; keep long material in references.>
<Keep reference documents under 150 lines and do not chain references.>
<Cite only items allowed by the repository standards allowlist once it exists.>
