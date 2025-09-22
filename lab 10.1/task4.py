"""Greeting utilities for students.

This module provides simple reusable functions to greet one or more students.
"""


def greet_student(name):
    """Print a welcome greeting for a single student.

    Args:
        name (str): The student's name to greet.
    """
    print("Welcome", name)


def greet_students(students):
    """Greet each student in a list using ``greet_student``.

    Args:
        students (list[str]): A list of student names to greet.
    """
    for name in students:
        greet_student(name)


if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie"]
    greet_students(students)
