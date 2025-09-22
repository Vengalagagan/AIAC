"""Compute the area of a rectangle and print an example result.

This module defines a function to calculate the area of a rectangle given its
length and breadth, following PEP 8 style and Google-style docstrings.
"""


def area_of_rectangle(length: float, breadth: float) -> float:
    """Return the area of a rectangle.

    Args:
        length: The length of the rectangle.
        breadth: The breadth (width) of the rectangle.

    Returns:
        float: The computed area (``length * breadth``).

    Raises:
        ValueError: If either ``length`` or ``breadth`` is negative.
    """

    if length < 0 or breadth < 0:
        raise ValueError("length and breadth must be non-negative")
    return length * breadth


if __name__ == "__main__":
    print(area_of_rectangle(10, 20))

