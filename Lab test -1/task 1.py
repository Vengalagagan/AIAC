def classify_age(age: int) -> str:
    """
    Return an age group label for the given age.

    Groups (inclusive ranges):
    - 0–12  -> "Child"
    - 13–17 -> "Teen"
    - 18–24 -> "Young Adult"
    - 25–44 -> "Adult"
    - 45–64 -> "Middle Aged"
    - 65+   -> "Senior"

    Args:
        age: The person's age. Accepts int or float-like values.

    Returns:
        Age group label as a string.

    Raises:
        TypeError: If age is not a number.
        ValueError: If age is negative.
    """

    # Basic type/validity checks to make the function more robust.
    # We accept int/float (e.g., 20.0) but not strings like "20".
    if not isinstance(age, (int, float)):
        raise TypeError("age must be a number (int or float)")

    if age < 0:
        raise ValueError("age cannot be negative")

    # Convert to integer to avoid floating-point edge cases (e.g., 17.9 -> 17).
    age = int(age)

    # Compare against inclusive upper bounds in ascending order.
    if age <= 12:
        return "Child"
    elif age <= 17:
        return "Teen"
    elif age <= 24:
        return "Young Adult"
    elif age <= 44:
        return "Adult"
    elif age <= 64:
        return "Middle Aged"
    else:
        return "Senior"


if __name__ == "__main__":
    # Example usage: prompt user, classify, and print the result.
    try:
        raw = input("Enter age: ")
        # Try parsing to float first to allow inputs like 21.0
        age_value = float(raw)
        print(classify_age(age_value))
    except Exception as exc:
        print(f"Error: {exc}")


