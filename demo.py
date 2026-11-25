from decimal import Decimal

from branch_stats import branch_summary
from pricing import visit_price


def main():
    prices = [visit_price(Decimal("1000"), visit) for visit in range(1, 4)]
    visits = list(zip(("A", "A", "B"), prices))
    print("Visits 1-3:", ", ".join(f"{price:.2f}" for price in prices))
    for branch in ("A", "B"):
        print(f"Branch {branch}:", branch_summary(visits, branch))

    assert prices == [Decimal("1000.00"), Decimal("1000.00"), Decimal("980.00")]
    assert branch_summary(visits, "A") == (2, Decimal("2000.00"))
    assert branch_summary(visits, "B") == (1, Decimal("980.00"))
    assert branch_summary(visits, "C") == (0, Decimal("0.00"))
    print("PASS")


if __name__ == "__main__":
    main()
