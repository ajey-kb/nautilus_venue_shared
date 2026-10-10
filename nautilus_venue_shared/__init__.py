"""nautilus_venue_shared — Python helpers shared across custom Nautilus
venue adapters (nautilus_nado, nautilus_bitget).

Sibling to venue-core (the Rust crate serving the same role on the Rust
side).  Promotes helpers that would otherwise duplicate across each
adapter's `utils.py` + `providers.py`:

    * `precision_from_increment(inc) -> int` — decimal places from a tick
    * `format_increment(inc, precision) -> str` — Nautilus-safe decimal format
    * `stub_currency(symbol) -> Currency` — placeholder base currency builder

Keep this package tiny.  Venue-specific logic belongs in each adapter.
"""
from nautilus_venue_shared.helpers import (
    format_increment,
    precision_from_increment,
    stub_currency,
)

__all__ = [
    "format_increment",
    "precision_from_increment",
    "stub_currency",
]
