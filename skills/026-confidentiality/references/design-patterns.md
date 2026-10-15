# Disclosure-boundary practices

Use the confirmed field/recipient policy for all in-scope paths, not just the main screen.

## Recipient-specific views

- Use when an allowed operation returns fields with different recipient permissions.
- Trade-off: narrower payloads need maintained view contracts; dropping required
  fields can break the legitimate function and must be exposed as a policy conflict.
- Verify: construct synthetic protected markers, capture emitted/received views,
  and check both forbidden absence and the approved recipient's useful subset.

## Cache and stored-view isolation

- Use when a response, export, or preview may be reused across scopes or policy states.
- Trade-off: policy-aware reuse can reduce cache sharing; a broad shared key can
  expose a previously authorized view to a now-forbidden recipient.
- Verify: populate under an allowed context, retrieve from another scope or after
  policy change, and inspect actual contents rather than relying on origin checks.

## Error, log, and diagnostic paths

- Use when protected values can escape through failure output outside normal serialization.
- Trade-off: less diagnostic content can limit investigation; agree the permitted
  diagnostic recipients/fields rather than silently forwarding the original payload.
- Verify: send markers through exceptions, validation errors, logs, trackers, and
  redirects/capture paths in scope; inspect what the recipient can actually read.

## Delayed delivery and copied output

- Use when queues, exports, or third parties retain views after live policy changes.
- Trade-off: revalidation, expiry, or invalidation needs a confirmed copy policy;
  changing the live serializer cannot retract previously disclosed contents.
- Verify: exercise stored/queued views around the policy transition and report
  observable recipients separately from uninspectable or already-delivered copies.
