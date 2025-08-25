import csv

def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Check if all cells in the row are empty
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            # Count words in all cells
            for cell in row:
                word_count += len(cell.split())

    return total_rows, empty_rows, word_count

if __name__ == "__main__":
    file_path = input("Enter the CSV file path: ")
    try:
        total, empty, words = analyze_csv(file_path)
        print(f"Total rows: {total}")
        print(f"Empty rows: {empty}")
        print(f"Total words: {words}")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")