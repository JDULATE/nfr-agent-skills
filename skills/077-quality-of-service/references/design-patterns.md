# Class-treatment decisions

Select a mechanism for independently required classes at a real shared bottleneck.
Ask the user for classification authority, eligibility windows and progress policy.

## Decision table

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Favored work repeatedly gets every dispatch while another eligible class must progress | Reserve dispatch opportunities or a worker share for the lower class | Favored-class capacity falls; simultaneous promises may be infeasible | Trace dispatch and completion for both classes under sustained contention |
| Separate ingress queues converge on a saturated pool | Apply per-class concurrency reservations at that pool | Idle reservations can waste capacity | Exercise the downstream pool directly and check each class's complete result |
| One class admits more work than its permitted queue can hold | Bound that class's admission and apply its approved rejection policy | Rejected work still fails any contract requiring admission | Compare per-class offered/admitted/rejected counts and promised waits/progress |
| Borrowed capacity delays a returning reserved class | Cap borrowing or use revocable work only where interruption is safe | Noninterruptible work can delay return of a reservation | Start reserved demand while borrowed work is active; inspect return delay and effects |

## Non-preemptive reservation sketch

Pseudocode; pattern is an owner-approved sequence of class opportunities.
A slot count alone is not a completion guarantee: task duration and capacity matter.

~~~text
dispatch_on_free_worker(pattern, cursor, queues):
    preferred = pattern[cursor]
    cursor = next_cyclic_position(pattern, cursor)
    if queues[preferred].has_eligible_work():
        return queues[preferred].pop(), cursor
    borrower = permitted_borrower(preferred, queues)
    if borrower exists:
        return queues[borrower].pop(), cursor
    return idle, cursor
~~~

Apply this only if the maximum borrowed work and required return delay are compatible.
For noninterruptible long work, reserve capacity rather than promising immediate
preemption. Recheck downstream contention before calling a dispatch policy sufficient.

## Assignment and acceptance

Derive class entitlement from trusted policy, not a caller's urgent label.
Keep permission to access data separate from preferential resource treatment.
Retain each class's admitted, rejected, completed and unfinished work, eligibility
intervals and queue/service observations. Check each obligation independently;
aggregate success cannot compensate for a failed class.
Zero completions alone establish neither no scheduling nor a cause of failure.
