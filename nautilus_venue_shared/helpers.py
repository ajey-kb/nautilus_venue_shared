"""Venue-agnostic helpers for building Nautilus `CryptoPerpetual` instruments.

Previously duplicated across:
    * nautilus_nado/adapter/utils.py (precision_from_increment, format_increment)
    * nautilus_bitget/adapter/utils.py (same two helpers)
    * nautilus_nado/adapter/providers.py :: NadoInstrumentProvider._stub_currency
    * nautilus_bitget/adapter/providers.py :: BitgetInstrumentProvider._stub_currency

Promoted here when a 3rd venue adapter (Phase 11+) would've forced a
3-way clone.  Keeping these ~5-15 lines in one place prevents the
drift risk flagged in the 2026-10-10 tech-debt audit.
"""
from __future__ import annotations

from decimal import Decimal


def precision_from_increment(inc: Decimal) -> int:
    """Return the decimal precision implied by a tick/lot increment.

    Example: Decimal("0.0001") → 4; Decimal("1") → 0.
    """
    if inc <= 0:
        return 0
    s = f"{inc:f}".rstrip("0")
    if "." not in s:
        return 0
    return len(s.split(".")[1])


def format_increment(inc: Decimal, precision: int) -> str:
    """Format a Decimal increment with explicit precision.

    Avoids `1e-6` scientific notation which Nautilus's Price/Quantity
    constructors reject.
    """
    return f"{inc:.{precision}f}"


def stub_currency(symbol: str):
    """Build a placeholder base currency for an instrument.

    Nautilus requires a `Currency` for `CryptoPerpetual.base_currency` but
    we don't need real ISO4217 metadata — just an identifier.  Falls back
    to a crypto placeholder if the symbol doesn't already exist in
    Nautilus's currency table.
    """
    from nautilus_trader.model.objects import Currency
    from nautilus_trader.core.rust.model import CurrencyType
    try:
        return Currency.from_str(symbol)
    except Exception:
        return Currency(
            code=symbol,
            precision=8,
            iso4217=0,
            name=symbol,
            currency_type=CurrencyType.CRYPTO,
        )
