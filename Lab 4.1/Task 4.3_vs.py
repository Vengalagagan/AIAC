def analyze_csv_input():
    print("Enter CSV data (end input with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    total_rows = len(lines)
    empty_rows = 0
    non_empty_rows = 0
    total_words = 0

    for row in lines:
        # Consider a row empty if all fields are empty after stripping spaces
        fields = [field.strip() for field in row.split(",")]
        if all(f == "" for f in fields):
            empty_rows += 1
        else:
            non_empty_rows += 1
            # Count words in non-empty fields
            for field in fields:
                total_words += len(field.split())

    print("\n             Final Analysis is")
    print(f"•\tTotal number of rows: {total_rows}")
    print(f"•\tNumber of empty rows: {empty_rows}")
    print(f"•\tTotal number of words: {total_words}")
    print(f"•\tNon-empty rows: {non_empty_rows}")

if __name__ == "__main__":
    analyze_csv_input()