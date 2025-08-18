from typing import List, Optional, Tuple
DEFAULT_SLABS: List[Tuple[Optional[float], float]] = [
    (50, 0.50),
    (100, 0.75),
    (100, 1.20),
    (None, 1.50),
]
DEFAULT_UNITS: float = 250.0
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
    print("Electricity Bill (Default Consumption)")
    print("=" * 40)
    print(f"Units Consumed: {units_consumed}")
    print("-" * 40)
    for idx, (units_billed, rate, cost) in enumerate(breakdown, start=1):
        print(f"Slab {idx:>2}: {units_billed:>8.2f} units @ {rate:.2f} = {cost:.2f}")
    print("-" * 40)
    print(f"Total Amount: {total_cost:.2f}")
def main() -> None:
    units = DEFAULT_UNITS
    total, details = calculate_bill(units)
    _print_breakdown(units, total, details)
if __name__ == "__main__":
    main()


