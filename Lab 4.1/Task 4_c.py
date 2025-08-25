import csv
import os
def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            return rows
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def count_total_rows(rows):
    if rows is None:
        return 0
    return len(rows)

def count_empty_rows(rows):
    if rows is None:
        return 0
    
    empty_count = 0
    for row in rows:
        if not row or all(cell.strip() == '' for cell in row):
            empty_count += 1
    
    return empty_count

def count_words_across_file(rows):
    if rows is None:
        return 0
    word_count = 0
    for row in rows:
        for cell in row:
            if cell and cell.strip():  # Check if cell is not empty
                # Split by whitespace and count words
                words = cell.strip().split()
                word_count += len(words)
    return word_count
def analyze_csv_file(filename):
    print(f"Analyzing CSV file: {filename}")
    print("-" * 50)
    rows = read_csv_file(filename)
    if rows is None:
        return
    total_rows = count_total_rows(rows)
    empty_rows = count_empty_rows(rows)
    total_words = count_words_across_file(rows)
    
    # Display results
    print(f"Total number of rows: {total_rows}")
    print(f"Number of empty rows: {empty_rows}")
    print(f"Total number of words: {total_words}")
    print(f"Non-empty rows: {total_rows - empty_rows}")
    
    return {
        'total_rows': total_rows,
        'empty_rows': empty_rows,
        'total_words': total_words,
        'non_empty_rows': total_rows - empty_rows
    }

def main():
    print("CSV File Analysis Program")
    print("=" * 50)
    
    # Default input - you can modify this filename
    default_filename = "sample.csv"
    
    # Check if default file exists
    if os.path.exists(default_filename):
        print(f"Using default file: {default_filename}")
        analyze_csv_file(default_filename)
    else:
        # If default file doesn't exist, ask user for input
        print(f"Default file '{default_filename}' not found.")
        user_filename = input("Please enter the path to your CSV file: ").strip()
        
        if user_filename:
            if os.path.exists(user_filename):
                analyze_csv_file(user_filename)
            else:
                print(f"File '{user_filename}' not found.")
        else:
            print("No filename provided. Exiting.")

if __name__ == "__main__":
    main()
