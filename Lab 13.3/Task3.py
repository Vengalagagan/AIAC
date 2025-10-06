class Student:
    """Represents a student with a name, age, and a collection of marks."""

    def __init__(self, name, age, *marks):
        """Initialize a Student.

        Accepts marks either as positional values (e.g., 80, 75, 92) or
        a single iterable (e.g., [80, 75, 92]).
        """
        self.name = name
        self.age = age

        # Allow both Student(name, age, 80, 75, 92) and Student(name, age, [80, 75, 92])
        if len(marks) == 1 and isinstance(marks[0], (list, tuple)):
            self.marks = list(marks[0])
        else:
            self.marks = list(marks)

    def details(self):
        """Print the student's basic details in a readable format."""
        print(f"Name: {self.name} | Age: {self.age}")

    def total(self):
        """Return the total of all marks."""
        return sum(self.marks)


if __name__ == "__main__":
    name_input = input("Enter student's name: ").strip()
    age_input = input("Enter student's age: ").strip()

    # Parse age as integer
    age_value = int(age_input)

    marks_input = input("Enter marks (comma or space separated): ").strip()
    # Support both comma and space separated entries
    parts = marks_input.replace(",", " ").split()
    marks_values = [int(p) for p in parts] if parts else []

    student = Student(name_input, age_value, marks_values)
    student.details()
    print(f"Marks: {student.marks} | Total: {student.total()}")

