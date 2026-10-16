# Locale-boundary decisions

Use supplied conventions; this guide does not define real regional requirements.

| Observed evidence | Intervention and trade-off | How to verify |
| --- | --- | --- |
| A translated button string is compared in a business condition. | Introduce a stable operation/resource key. Existing references need migration. | Change the displayed text and verify the selected operation stays the same. |
| Messages are assembled from translated fragments. | Use complete templates with named placeholders. Catalogues need placeholder contracts. | Reorder the placeholders in a second supplied resource and inspect preserved meaning. |
| UI decimal formatting changes machine output. | Keep presentation formatting separate from canonical serialization. Two output paths must be maintained. | Compare the same canonical amount's display and machine representation. |
| A date is ambiguous after formatting. | Declare the canonical type and confirmed display convention. Existing user input may need disambiguation. | Round-trip the known date under that convention without guessing another one. |
| A missing key silently looks like successful locale support. | Make missing/fallback behavior explicit and expose unsupported surfaces. Users may see a deliberate limitation. | Remove a required resource and inspect the reported outcome. |
| One audience's locale changes another view. | Bind locale to each rendering context when audience choices differ. Context must travel through formatting calls. | Render plain, alternate, then plain and verify the final plain output remains unchanged. |

## Resource boundary sketch

```text
operation = "export"
display = resource(locale, "export_summary").format(
  amount=display_amount(canonical_amount, locale),
  date=display_date(canonical_date, locale))
machine_payload = {
  operation: operation,
  amount_minor: canonical_amount,
  date: canonical_date
}
```

The same canonical values feed both outputs, but only the human display uses
the supplied locale formatters.

## Review boundary

Mechanism tests can establish key lookup, placeholder binding, and representation
preservation. They cannot approve real wording or a cultural convention.
Ask for qualified wording and renderer-based review before making those claims.
