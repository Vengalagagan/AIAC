import csv
import sys

def analyze_csv(csv_content):
    """
    Analyze CSV content and return statistics
    """
    lines = csv_content.strip().split('\n')
    
    total_rows = len(lines)
    empty_rows = 0
    total_words = 0
    non_empty_rows = 0
    
    for line in lines:
        # Check if line is empty or contains only commas
        if not line.strip() or line.strip().replace(',', '').strip() == '':
            empty_rows += 1
        else:
            non_empty_rows += 1
            # Count words in non-empty rows
            words = line.split(',')
            total_words += len(words)
    
    return {
        'total_rows': total_rows,
        'empty_rows': empty_rows,
        'total_words': total_words,
        'non_empty_rows': non_empty_rows
    }

def print_analysis(stats):
    """
    Print the analysis results in the required format
    """
    print("             Final Analysis is")
    print(f"•\tTotal number of rows: {stats['total_rows']}")
    print(f"•\tNumber of empty rows: {stats['empty_rows']}")
    print(f"•\tTotal number of words: {stats['total_words']}")
    print(f"•\tNon-empty rows: {stats['non_empty_rows']}")

def main():
    print("CSV File Analysis Program")
    print("=" * 40)
    print("Enter CSV data (press Enter twice to finish):")
    print("Example format:")
    print("Name,Age,City,Occupation")
    print("John Doe,25,New York,Software Engineer")
    print("")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    if not lines:
        print("No data entered!")
        return
    
    csv_content = '\n'.join(lines)
    
    # Analyze the CSV content
    stats = analyze_csv(csv_content)
    
    # Print the analysis
    print("\n" + "=" * 40)
    print_analysis(stats)

if __name__ == "__main__":
    main()
