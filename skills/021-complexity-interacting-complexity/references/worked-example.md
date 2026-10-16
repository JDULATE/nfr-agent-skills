# Coupled flags and callback reentry

This synthetic model uses illustrative flags, states, and acceptance defaults;
confirm with the user/stakeholder before adopting them.

## Filled inputs

| Field | Value |
| --- | --- |
| Operation | save(fresh, refresh_enabled, notify_enabled) |
| Initial persistent state | store=old |
| Initial cache state | cache=old |
| Initial notification state | [] |
| Supported flag values | refresh and notify independently false or true |
| Required persistence | store becomes fresh |
| Required refresh | cache becomes fresh only when refresh is enabled |
| Required notification | [saved:fresh] when notify is enabled, otherwise [] |
| Old refresh callback | set cache=fresh, then call save again with unchanged flags |
| Trace boundary | stop exploration when save reenters with identical arguments |
| Evidence owner | save-feature maintainer role |

## Before interaction ledger

The source edges are save->persist, save->notify when enabled,
save->refresh when enabled, and refresh->save.
The repeated-state stop is a fixture inspection guard, not production behavior.

| refresh / notify | Activated path | State at fixture stop | Reasoning obligation |
| --- | --- | --- | --- |
| false / false | save->persist | store=fresh, cache=old, notices=[] | no callback reentry |
| false / true | save->persist->notify | store=fresh, cache=old, notices=[saved:fresh] | notification path only |
| true / false | save->persist->refresh->save | store=fresh, cache=fresh, notices=[] | reachable save reentry; termination unresolved |
| true / true | save->persist->notify->refresh->save | store=fresh, cache=fresh, notices=[saved:fresh] | reentry could repeat notification; termination unresolved |

These paths establish reachable feedback in the supplied model.
They do not measure human effort or claim an observed production infinite loop.

## Remediation

Replace the refresh callback with a cache update that never invokes save.
Use the explicit phase sequence in the design sketch.
Do not remove required persistence or notification.
The order change places notification after refresh; this fixture permits that
order and has no notification observer reading intermediate cache state.

## After carried state

Each run resets store=old, cache=old, and notices=[].

| refresh / notify | Terminal state | Reentry result |
| --- | --- | --- |
| false / false | store=fresh, cache=old, notices=[] | absent |
| false / true | store=fresh, cache=old, notices=[saved:fresh] | absent |
| true / false | store=fresh, cache=fresh, notices=[] | absent |
| true / true | store=fresh, cache=fresh, notices=[saved:fresh] | absent |

The modeled save reentry obligation is removed while the named effects remain.

## Failing control

Reattach a refresh->save subscription without changing the facade.
The true/false case again reaches the repeated save state.
A facade method count would miss the restored feedback; the trace catches it.

## Limits

The ledger covers only these flags and subscriptions.
It does not establish behavior of asynchronous delivery, notification failure,
or additional subscribers. Static edge totals alone would not explain the
difference because changing edge meaning can matter without reducing the total.
