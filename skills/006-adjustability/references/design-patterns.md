# Parameter-application patterns

Read the actual consumer and its work boundary before choosing an intervention.
For a missing runtime surface, first use `configurability` to establish the value's
location, domain, default, and permitted caller; then use `adjustability` for application.
Show the consolidated proposal block before changing code or configuration.

## Make a hardcoded constant runtime-changeable

| Evidence / use when | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| A constant is embedded in an operation; no runtime reader/setter exists | Extract a scoped setting with the current constant as default, validate changes, and snapshot it at the agreed point of use | A process-local setting resets on restart; offer persistence rather than silently adding it | Observe unchanged default behavior, rejected updates retaining the previous value, new work using the changed value, and rollback through the same reader |

Use the smallest authorized interface: reuse an existing call path or add an
in-process setter under the caller's existing privileges. Offer authentication,
persistence, a new server, or response headers separately; obtain the user's yes
unless already authorized. A local setting does not require a new network route.

```python
class RuntimeSetting:
    def __init__(self, default, is_valid):
        self.is_valid = is_valid
        self.set(default)

    def set(self, value):
        if not self.is_valid(value):
            raise ValueError("outside agreed domain")
        self.value = value

setting = RuntimeSetting(existing_default, agreed_domain)

def run_unit(item):
    applied = setting.value
    result = existing_operation(item, applied)
    return result, applied
```

This is a sequential in-process sketch, not a concurrent-update guarantee or an
instruction to change an external response shape. Supply the inspected default,
domain predicate, and operation. The local return carries test/readback evidence;
adapt it to the existing interface. Running work keeps its captured value only
when that boundary is established by the code or confirmed by the user.

## Choose the application intervention

| Observed evidence | Intervention | Trade-off | How to verify |
| --- | --- | --- | --- |
| Saved changes are overridden or cached | Trace the winning source and refresh at the agreed application event | Inspection adds upkeep; retain only evidence needed to explain the applied value | Compare the consuming loop with the requested setting and probe work after refresh |
| A batch rereads a changing cap midway through work | Capture the value at its agreed start boundary | New requests wait until the next boundary | Update during active work; check that work's captured cap and later work separately |
| A changed value is described as faster without an operating trial | Compare candidate and former values under held input and arrangement | A fixture may omit workload variability | Repeat the baseline and inspect the desired effect and resource trade-offs separately |
| Restoring the file does not restore operating behavior | Reverse through the same reader, overrides, and application event | Reversal cannot undo completed effects | Start new work after reversal and check its applied value and emitted behavior |

## Applied value or applied revision?

| Evidence needed | Sufficient observation | How to verify |
| --- | --- | --- |
| One sequential consumer applies changes synchronously; no ambiguity about the value used | Applied-value readback from the consumer plus a behavior probe; no revision service | Apply a valid change, start the affected work, and match its captured value to the result |
| Asynchronous consumers, overlapping updates, repeated-value history, or partial application make change identity matter | Applied revision bound to the consumer/work snapshot, distinct from a requested revision | Delay a consumer or reorder updates; identify which revision each work unit actually used and expose pending application |

Use a revision only when value readback cannot answer the required application
question. An arbitrary settings-page value or saved revision is not a consumer
readback. Arrangement/ownership transfer belongs under `reconfigurability`.
