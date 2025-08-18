def factorial_iterative(n):
    """Calculate factorial using iterative approach"""
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
def main():
    print("Factorial Calculator")
    print("=" * 20)
    try:
        num = int(input("Enter a number to calculate factorial: "))
        iterative_result = factorial_iterative(num)
        recursive_result = factorial_recursive(num)
        
        # Display results
        print(f"\nFactorial of {num}:")
        print(f"Iterative method: {iterative_result}")
        print(f"Recursive method: {recursive_result}")
        
        # Show the calculation breakdown
        if isinstance(iterative_result, int):
            print(f"\nCalculation: {num}! = ", end="")
            for i in range(num, 0, -1):
                if i == 1:
                    print(f"{i} = {iterative_result}")
                else:
                    print(f"{i} × ", end="")
                    
    except ValueError:
        print("Error: Please enter a valid integer!")
    except RecursionError:
        print("Error: Number too large for recursive calculation!")

if __name__ == "__main__":
    main()