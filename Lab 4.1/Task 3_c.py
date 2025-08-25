def parse_student(student_record):
    first_name = student_record.get("name", {}).get("first", "").strip()
    last_name = student_record.get("name", {}).get("last", "").strip()
    full_name = (first_name + " " + last_name).strip()

    branch = student_record.get("academics", {}).get("branch", "").strip()
    sgpa_value = student_record.get("academics", {}).get("sgpa", None)

    # Decide how to display SGPA: drop trailing .0 if present
    if isinstance(sgpa_value, (int, float)):
        if float(sgpa_value).is_integer():
            sgpa_display = str(int(sgpa_value))
        else:
            sgpa_display = str(sgpa_value)
    else:
        # If not a number, fall back to raw string
        sgpa_display = str(sgpa_value) if sgpa_value is not None else ""

    return full_name, branch, sgpa_display


def main():
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    branch = input("Branch: ").strip()

    sgpa_raw = input("SGPA: ").strip()
    try:
        sgpa = float(sgpa_raw)
    except ValueError:
        sgpa = sgpa_raw  # Keep as string if user didn't enter a valid number

    student = {
        "name": {
            "first": first_name,
            "last": last_name,
        },
        "academics": {
            "branch": branch,
            "sgpa": sgpa,
        },
    }

    full_name, parsed_branch, sgpa_display = parse_student(student)

    print("Student Details:")
    print(f"Full Name: {full_name}")
    print(f"Branch: {parsed_branch}")
    # Match the example formatting without a space after colon for SGPA
    print(f"SGPA:{sgpa_display}")


if __name__ == "__main__":
    main()


