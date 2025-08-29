def factr(n):
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base cases
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factr(n - 1)

print(factr(5))
