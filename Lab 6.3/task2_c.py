def print_multiples_for(n):
    for i in range(1, 11):
        print(n * i)

# Get user input
try:
    user_number = int(input("Enter a number to print its multiples: "))
    print_multiples_for(user_number)
except ValueError:
    print("Please enter a valid integer.")