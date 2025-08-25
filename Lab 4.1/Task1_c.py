import random


def generate_indian_mobile_number() -> str:
    """Generate a 10-digit Indian mobile number starting with 6, 7, 8, or 9."""
    first_digit = str(random.choice([6, 7, 8, 9]))
    remaining_digits = "".join(str(random.randint(0, 9)) for _ in range(9))
    return first_digit + remaining_digits


if __name__ == "__main__":
    print(generate_indian_mobile_number())


