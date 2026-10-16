---
name: communicativeness
description: >-
  Times user feedback when asked "notify on export completion", "report errors sooner", or "send job updates". Ask the user if notifications vs visible status is unclear. Not for explaining current state and actions (see self-descriptiveness) or clarifying a standalone explanation (see comprehensibility).
---
# Communicativeness

## Definition and scope

Communicativeness means users receive the information and feedback they need at
the relevant point in an interaction. Connect events to recipients, channels,
and next actions; distinguish context visible in a state (`self-descriptiveness`)
and interpretation of a separate explanation (`comprehensibility`).

## Use when / Don't use when

- Apply when acknowledgement, progress, completion, or failure messages are late,
  absent, duplicated confusingly, or delivered where the user cannot retrieve them.
- Route a static action's unexplained availability to `self-descriptiveness`.
- Route diagnosing hidden runtime state to `observability`; a diagnostic log is
  not necessarily information delivered to the person waiting on the task.

## Workflow

1. Clarify: Read event-producing code, notification handlers, interaction docs,
   state transitions, and current message copy before promising feedback.
   If backend acceptance differs from completion, then map those events separately
   and identify the user decision that each message is meant to support.

2. Specify: Bind trigger, recipient, payload, channel, timing, ordering, persistence,
   next action, and evidence to each task event.
   If the request is practical, then offer this message contract together:

   ```text
   Illustrative defaults; confirm with the user/stakeholder:
   Task/recipient: named task and initiating user under existing delivery permissions.
   Events: accepted, pending, completed, failed; meanings follow actual state commits.
   Delivery: existing in-product channel plus persistent task history if already supported.
   Timing trial: show completion within 5 seconds of observed committed completion.
   Payload: task identity, truthful state, known result/error, and permitted next action.
   Ordering: correlate by task and revision; late pending cannot replace completed.
   Absence: missing result remains unknown/pending, never fabricated success.
   Evidence: source event, delivery/render observation, return-to-task replay, owner.
   Status: proposed timing and delivery design; no new channel permission assumed.
   ```

   Ask at most three groups about recipient/task decisions; permitted channels
   and return behavior; and timing, failure, or ordering constraints. Continue to design.
   If no timing target exists, then propose the illustrative trial and confirm
   with the user/stakeholder before asserting delivery attainment.
   State every assumption and proposed default to the user before building; ask at most
   three questions, and stop for the user's reply only when a decision goes beyond the
   smallest version.

3. Design/Implement: Read [event-to-message patterns](./references/design-patterns.md)
   when handling deferred, replayed, or out-of-order feedback.
   If the user leaves the screen, then provide the agreed retrieval route instead
   of relying on a transient message they cannot see.
   If a message claims success, then tie it to the actual business completion event,
   not merely a queued request; preserve distinct pending and failed outcomes.
   Build the smallest version that meets the request; list larger extensions as offers
   and add them only with the user's yes.

4. Verify: Drive accepted, delayed, completed, and failed traces through the
   agreed channel; inspect payloads and delivery with task correlation retained.
   If event evidence exists without recipient-visible delivery, then mark the
   communication gap instead of using backend logs as proof of receipt.

5. Report: Return the message matrix, changed handlers/copy, timing evidence,
   retrieval behavior, and unresolved delivery gaps.
   If only transport acceptance is observed, then limit the claim to transport;
   do not claim display, reading, or comprehension without corresponding evidence.

## Specification patterns

- **Feedback:** After `{business_event}`, deliver `{truthful_message_and_action}`
  to `{recipient}` via `{channel}` within `{confirmed_interval}`, measured from
  `{event_anchor}` to `{agreed_delivery_observation}`.
- **Return path:** For `{task}` after `{departure_or_disconnect}`, expose
  `{current_outcome_and_history}` at `{retrieval_point}`, verified through
  `{late_delivery_duplicate_and_out_of_order_traces}`.

Use the illustrative timing trial when a target is absent and confirm with the
user/stakeholder. Ask the user whether acceptance means queued, delivered, rendered, or acknowledged.

## Rules of thumb

- Do distinguish request acceptance from task completion in user messages;
  an immediate receipt must not consume the later completion feedback obligation.
- Do correlate visible feedback with the exact task, not just the active screen;
  a delayed result for an earlier task can otherwise instruct the wrong next action.
- Don't let late progress replace a terminal message; the user would lose the
  decision-relevant outcome even though every event was technically delivered.
- Do give missed transient feedback an agreed retrieval point; a toast's lifetime
  is not a guarantee that a returning user can learn the outcome.
- Don't turn duplicate delivery into duplicate next-action prompts; keep a stable
  outcome reference so replay does not suggest that the task itself happened again.
- Do test what information arrives before the user must choose the next action;
  a correct message delivered after that choice does not satisfy its communication purpose.

## Verification

Use interaction integration, event replay, and message-render inspection categories.
Retain accepted and committed event anchors, task keys, revisions, delivery points,
message copy, and return-path observations. Exercise delay, duplicate, reordered,
failed, and absent outcomes. Distinguish transport acceptance, visible presentation,
and user acknowledgement. Verify no stale success remains after a failure trace.

## Done checklist

- [ ] Map distinct business events to truthful messages and intended recipients.
- [ ] Anchor timing to the agreed source and recipient-visible observation.
- [ ] Exercise progress, completion, and failure for the same task identity.
- [ ] Verify a late or duplicate event does not overwrite a newer outcome.
- [ ] Retrieve the outcome after leaving and returning to the task.
- [ ] Distinguish queued, delivered, displayed, and acknowledged evidence.
- [ ] Inspect that next-action wording matches the actual task outcome.

## Failure modes

- Calling the task complete when only queue acceptance occurred.
- Showing a delayed result on the wrong task or replacing it with old progress.
- Equating a transport receipt with a user-visible message.
- Losing the only failure explanation when a transient banner disappears.
- Replaying a notification as if it were a new task outcome.

## References

- Read [event-to-message patterns](./references/design-patterns.md) when selecting
  event anchors, replay behavior, or a durable retrieval route.
- Read [export-notification example](./references/worked-example.md) when testing
  departures and stale progress without inventing a completed result.
