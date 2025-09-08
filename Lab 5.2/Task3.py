def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using plain recursion (0-indexed).

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n >= 2

    Args:
        n: The index in the sequence (must be non-negative).

    Returns:
        The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    # Guard against invalid input: Fibonacci is not defined for negative indices
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # Base cases stop the recursion:
    # - When n is 0, the result is 0
    # - When n is 1, the result is 1
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case: sum of the two previous Fibonacci numbers
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Simple demo: compute and print a few Fibonacci numbers
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")


