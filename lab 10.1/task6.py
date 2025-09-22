def grade(score):
    # Use a clear elif ladder to map score ranges to letter grades
    if score >= 90:       # 90–100
        return "A"
    elif score >= 80:     # 80–89
        return "B"
    elif score >= 70:     # 70–79
        return "C"
    elif score >= 60:     # 60–69
        return "D"
    else:                 # Below 60
        return "F"

if __name__ == "__main__":
    # Prompt the user for a numeric score and print the corresponding grade
    try:
        user_input = input("Enter the score (0-100): ")  # Read input as string
        score_value = float(user_input)                   # Convert to number (allows decimals)

        # Optional bounds check; clamp or report invalid
        if score_value < 0 or score_value > 100:
            print("Please enter a score between 0 and 100.")
        else:
            print(f"Grade: {grade(score_value)}")
    except ValueError:
        # Handle non-numeric input
        print("Invalid input. Please enter a numeric value.")
