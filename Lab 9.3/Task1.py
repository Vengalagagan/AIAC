def calculate_even_odd_sums(numbers_input):
    """
    Calculate the sum of even and odd numbers from a space-separated string of numbers.
    This function takes a string of space-separated numbers, converts them to integers,
    and calculates the sum of even numbers and the sum of odd numbers separately.
    Args:
        numbers_input (str): A string containing space-separated numbers.
                            Example: "1 2 3 4 5 6"
    Returns:
        tuple: A tuple containing two integers:
            - even_sum (int): Sum of all even numbers in the input
            - odd_sum (int): Sum of all odd numbers in the input
    
    Example:
        >>> result = calculate_even_odd_sums("1 2 3 4 5 6")
        >>> print(result)
        (12, 9)  # even_sum=12 (2+4+6), odd_sum=9 (1+3+5)
    """
    numbers = numbers_input.split()
    even_sum = 0
    odd_sum = 0
    
    for n in numbers:
        n = int(n)
        if n % 2 == 0:
            even_sum = even_sum + n
        else:
            odd_sum = odd_sum + n
    
    return even_sum, odd_sum

# Example usage
if __name__ == "__main__":
    numbers = input("Enter numbers: ")
    even_sum, odd_sum = calculate_even_odd_sums(numbers)
    print("Sum of even numbers:", even_sum)
    print("Sum of odd numbers:", odd_sum)
