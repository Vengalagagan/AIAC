from typing import List, Optional, Tuple
DEFAULT_SLABS: List[Tuple[Optional[float], float]] = [
    (50, 0.50),
    (100, 0.75),
    (100, 1.20),
    (None, 1.50),  
]
def calculate_bill(units_consumed: float,
                   slabs: List[Tuple[Optional[float], float]] = DEFAULT_SLABS
                   ) -> Tuple[float, List[Tuple[float, float, float]]]:
    if units_consumed < 0:
        raise ValueError("Units consumed cannot be negative.")

    remaining_units: float = units_consumed
    breakdown: List[Tuple[float, float, float]] = []

    for slab_units, rate in slabs:
        if remaining_units <= 0:
            break

        if slab_units is None:
            units_in_this_slab = remaining_units
        else:
            units_in_this_slab = min(remaining_units, slab_units)

        cost_for_slab = units_in_this_slab * rate
        breakdown.append((units_in_this_slab, rate, cost_for_slab))
        remaining_units -= units_in_this_slab

    total_cost = sum(cost for _, _, cost in breakdown)
    return total_cost, breakdown


def _print_breakdown(units_consumed: float, total_cost: float,
                     breakdown: List[Tuple[float, float, float]]) -> None:
    print("\nBill Breakdown")
    print("=" * 30)
    print(f"Units Consumed: {units_consumed}")
    print("-" * 30)
    for idx, (units_billed, rate, cost) in enumerate(breakdown, start=1):
        print(f"Slab {idx:>2}: {units_billed:>8.2f} units @ {rate:.2f} = {cost:.2f}")
    print("-" * 30)
    print(f"Total Amount: {total_cost:.2f}")


def main() -> None:
    print("Electricity Bill Calculator (Slab-wise)")
    print("-" * 40)
    try:
        raw = input("Enter units consumed: ").strip()
        if not raw:
            print("No input provided.")
            return
        units = float(raw)
        total, details = calculate_bill(units)
        _print_breakdown(units, total, details)
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()


