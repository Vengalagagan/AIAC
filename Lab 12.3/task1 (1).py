def linear_search(lst, value):
    """
    Searches for 'value' in 'lst' and returns its index if found. 
    Returns -1 if the value is not in the list.
    """
    for idx, item in enumerate(lst):
        if item == value:
            return idx
    return -1

# User input version
if __name__ == "__main__":
    print("Linear Search Program")
    print("=" * 30)
    
    # Get list from user
    print("Enter a list of numbers (separated by spaces):")
    try:
        user_input = input("List: ")
        test_list = [int(x) for x in user_input.split()]
        print(f"Your list: {test_list}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        exit()
    
    # Get search value from user
    try:
        search_value = int(input("Enter the number to search for: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        exit()
    
    # Perform search
    print(f"\nSearching for {search_value} in {test_list}")
    result = linear_search(test_list, search_value)
    
    if result != -1:
        print(f"Found {search_value} at index {result}")
    else:
        print(f"{search_value} not found in the list")