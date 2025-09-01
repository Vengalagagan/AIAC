def classify_age_nested_loops():
    # Outer loop for multiple age classifications
    while True:
        try:
            age = int(input("Enter the age of the person (or -1 to exit): "))
            
            # Inner loop for age validation and classification
            if age == -1:
                print("Exiting the program...")
                break
            elif age < 0:
                print("Invalid age: Age cannot be a negative number.")
                continue
            
            # Nested conditional structure using loops
            age_ranges = [
                (0, 12, "Child"),
                (13, 19, "Teen"), 
                (20, 59, "Adult"),
                (60, 150, "Senior")
            ]
            
            # Loop through age ranges to find classification
            for min_age, max_age, category in age_ranges:
                if min_age <= age <= max_age:
                    print(f"Age {age}: {category}")
                    break
            else:
                print(f"Age {age}: Very Senior (over 150)")
                
        except ValueError:
            print("Invalid input: Please enter a valid number.")
            continue

# Call the function
classify_age_nested_loops()