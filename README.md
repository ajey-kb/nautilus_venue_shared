# nautilus_venue_shared

Tiny Python helpers used by multiple custom nautilus_trader venue adapters
([nautilus_nado](https://github.com/ajey-kb/nautilus_nado),
[nautilus_bitget](https://github.com/ajey-kb/nautilus_bitget)). Sibling to
the Rust `venue-core` crate (which lives in nautilus_nado's workspace).

Scope is intentionally tiny — if a helper only makes sense for one adapter,
it stays in that adapter's `utils.py`.

Current contents:
- `precision_from_increment(inc)` — decimal places from a Decimal tick
- `format_increment(inc, precision)` — Nautilus-safe decimal format (no sci notation)
- `stub_currency(symbol)` — placeholder `Currency` for `CryptoPerpetual.base_currency`

## Install

```bash
pip install -e /path/to/nautilus_venue_shared
```

Or add to a sibling package's pyproject deps:
```toml
dependencies = ["nautilus_venue_shared @ file:///home/akb/trading/nautilus_venue_shared"]
```
