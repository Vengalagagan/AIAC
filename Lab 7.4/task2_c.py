def sort_list(data):
    # Separate numbers and strings
    numbers = [x for x in data if isinstance(x, (int, float))]
    strings = [x for x in data if isinstance(x, str)]
    
    # Sort each type separately
    sorted_numbers = sorted(numbers)
    sorted_strings = sorted(strings)
    
    # Return combined sorted list (numbers first, then strings)
    return sorted_numbers + sorted_strings

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))
