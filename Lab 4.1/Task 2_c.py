def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers")
    else:
        print(f"The factorial of {number}={factorial(number)}")
except ValueError:
    print("Invalid input. Please enter an integer.")


