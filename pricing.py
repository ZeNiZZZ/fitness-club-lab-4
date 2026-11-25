from decimal import Decimal, ROUND_HALF_UP


def visit_price(rate: Decimal, visit: int) -> Decimal:
    if rate < 0 or visit < 1:
        raise ValueError("Rate must be nonnegative and visit must be positive")
    factor = Decimal("0.98") if visit >= 3 else Decimal("1")
    return (rate * factor).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
