from decimal import Decimal
from pricing import visit_price


def main():
    prices = [visit_price(Decimal("1000"), visit) for visit in range(1, 4)]
    print("Visits 1-3:", ", ".join(f"{price:.2f}" for price in prices))


if __name__ == "__main__":
    main()
