def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def sum_to_n_builtin(n):
    return sum(range(1, n + 1))


# Get user input
n = int(input("Enter a number to calculate sum from 1 to n: "))

# Calculate and display results using different methods
print(f"\nSum from 1 to {n} using for loop: {sum_to_n(n)}")
print(f"Sum from 1 to {n} using while loop: {sum_to_n_while(n)}")
print(f"Sum from 1 to {n} using built-in functions: {sum_to_n_builtin(n)}")