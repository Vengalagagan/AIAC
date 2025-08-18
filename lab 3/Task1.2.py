def compute_factorial(number: int = 5) -> int:
    """Return the factorial of `number`. Uses 5 as the default value.

    Raises:
        ValueError: If `number` is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    product: int = 1
    for factor in range(2, number + 1):
        product *= factor
    return product


if __name__ == "__main__":
    # Uses the default value (5) when no argument is provided
    print(f"Factorial of 5 = {compute_factorial()}")


