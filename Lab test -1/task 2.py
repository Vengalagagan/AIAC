class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


def read_marks_input(text):
    raw = input(text).strip()
    if "," in raw:
        parts = [p.strip() for p in raw.split(",") if p.strip()]
    else:
        parts = [p.strip() for p in raw.split() if p.strip()]
    if not parts:
        return []
    marks = []
    for p in parts:
        try:
            marks.append(float(p))
        except ValueError:
            print(f"Warning: could not parse '{p}' as a number. Skipping.")
    return marks


if __name__ == "__main__":
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    marks = read_marks_input("Enter marks (comma-separated or space-separated): ")

    student = Student(name, roll_no, marks)
    print("\nStudent Details:")
    student.display_details()


