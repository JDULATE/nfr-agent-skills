---
name: suitability
description: >-
  Checks available capability fit when asked "feed an offline importer", "match a handoff format", or "compare task options". Before routing workflow complaints, Ask the user: missing capability, task fit, or actual outcomes? Not for capability presence alone (see functionality) or achieved outcomes (see effectiveness).
---

# Suitability

## Definition and scope

Suitability means available capabilities fit a particular task and its context.
Identify the task's required inputs, outputs, constraints, and receiving tools,
then assess whether the capability can serve that task without unacceptable workarounds.
Separate task fit from capability presence (`functionality`) and observed
stakeholder outcome attainment (`effectiveness`).

## Use when / Don't use when

- Apply when an export exists but its format or delivery mode cannot serve
  a specified offline handoff.
- Include the actual receiving tool and restrictions on manual workarounds.
- Route a wholly absent required operation to `functionality`.
- Route whether real use achieves a wider goal to `effectiveness`.
- Route exchange interpretation alone to `interoperability` when no particular
  task/context fit is being assessed.
- Route interaction effort to `usability` if the capability fits but is hard to use.

## Workflow

1. Clarify: Read capability docs, export code, receiver contracts, workflow
   instructions, and context constraints before proposing a fit requirement.
   Identify the specific task and an actual input/output example.
   If "make this useful" names no task or context, then Ask the user what
   handoff must succeed and which workarounds are unacceptable.

2. Specify: Record task, actor, source data, required artifact, receiver,
   environment restrictions, allowed adaptation, and fit evidence.
   If no target exists, then propose a labeled illustrative default:
   the named handoff completes with preserved data using the existing receiver,
   without manual re-entry; confirm with the user/stakeholder.
   Ask at most three questions about task/context, receiver constraints,
   and allowed adaptation before changing the export path.

3. Design/Implement: Read [task-fit decisions](./references/design-guide.md)
   when choosing format, local delivery, or constrained adaptation.
   If the receiver is offline, then provide the required local artifact rather
   than relying on a capability that needs remote retrieval.
   If its format cannot represent a source value under the supplied contract,
   then expose that limitation rather than silently dropping or changing the value.

4. Verify: Exercise the complete named handoff from source through the existing
   receiving tool, comparing accepted records with the task's required meaning.
   Keep failed cases, manual steps, and unsupported inputs visible.
   If only artifact generation was checked, then leave receiver/task fit
   unverified even when the export operation succeeds.

5. Report: Return the capability-to-task map, adaptation, receiver evidence,
   remaining workarounds, and context limits.
   If the fixture handoff works, then limit the conclusion to that task and
   avoid claiming population effectiveness or suitability for every recipient.

## Specification patterns

- **Task fit:** For `{actor_task_and_context}`, `{capability}` shall produce
  `{artifact_and_meaning}` usable by `{existing_receiver}` under
  `{environment_and_workaround_constraints}`, verified by `{full_handoff_fixture}`.
- **Unsupported case:** When `{source_case}` cannot meet `{task_format_contract}`,
  the capability shall return `{explicit_limitation}` without
  `{silent_data_change_or_unaccepted_workaround}`.

Use the illustrative direct-handoff proposal in Specify when no number is given;
confirm with the user/stakeholder before accepting the task-fit boundary.

## Rules of thumb

- Judge an export by the receiving task's artifact needs, not the existence of
  a download control; a remote token does not fit a required offline file handoff.
- Keep unaccepted manual re-entry visible as a fit gap; a feature that works only
  after someone reconstructs its output may not satisfy the stated task.
- Preserve task-essential fields and values during adaptation; a parseable file
  that drops zero quantities has not fitted the declared inventory handoff.

## Verification

Use representative handoff fixtures, receiver execution, and task-step review.
Capture source records, emitted artifact, receiver output, and any manual steps.
Check offline constraints and the actual delivery mode.
Compare task-essential meaning independently of parse success.
Exercise unsupported delimiters or other format boundaries only under the
receiver's supplied contract.
Retain rejected inputs and scope limits; do not substitute a demonstration
receiver with weaker requirements.
Separate this bounded fit evidence from general user outcome or usability claims.

## Done checklist

- [ ] Define the task, actor, receiver, and environment.
- [ ] Identify required artifact meaning and allowed workarounds.
- [ ] Map available capabilities to each required handoff step.
- [ ] Produce the artifact through the actual export path.
- [ ] Run the existing receiver on that artifact.
- [ ] Compare task-essential fields, including valid zero values.
- [ ] Exercise and report an unsupported source case.
- [ ] Bound the conclusion to the tested task/context.

## Failure modes

- Treating successful export generation as evidence the recipient can use it.
- Replacing an offline handoff with a remote retrieval dependency.
- Requiring hidden manual re-entry while claiming direct task fit.
- Silently modifying an unrepresentable field to make parsing succeed.

## References

- Read [task-fit decisions](./references/design-guide.md) when selecting
  a capability adaptation for a constrained handoff.
- Read [offline import handoff example](./references/worked-example.md) when
  checking an existing receiver rather than export presence alone.
