import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    non_empty_rows = 0

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Remove leading/trailing spaces and check if all fields are empty
            cleaned_row = [field.strip() for field in row]
            if all(field == '' for field in cleaned_row):
                empty_rows += 1
            else:
                non_empty_rows += 1
                # Count words in each field
                for field in cleaned_row:
                    total_words += len(field.split())

    print("Final Analysis is")
    print(f"•\tTotal number of rows: {total_rows}")
    print(f"•\tNumber of empty rows: {empty_rows}")
    print(f"•\tTotal number of words: {total_words}")
    print(f"•\tNon-empty rows: {non_empty_rows}")

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")
    analyze_csv(file_path)