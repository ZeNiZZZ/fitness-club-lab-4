from decimal import Decimal
from branch_stats import branch_summary


def main():
    visits = [
        ("A", Decimal("1000.00")),
        ("A", Decimal("1000.00")),
        ("B", Decimal("980.00")),
    ]
    for branch in ("A", "B"):
        print(f"Branch {branch}:", branch_summary(visits, branch))


if __name__ == "__main__":
    main()
