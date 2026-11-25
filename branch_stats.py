from decimal import Decimal
from typing import Iterable, Tuple


def branch_summary(
    visits: Iterable[Tuple[str, Decimal]], branch: str
) -> Tuple[int, Decimal]:
    amounts = [amount for location, amount in visits if location == branch]
    return len(amounts), sum(amounts, Decimal("0.00"))
