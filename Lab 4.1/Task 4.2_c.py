import csv
import os
def analyze_csv(file_path):
    try:
        if not os.path.exists(file_path):
            return None, "File not found"
        
        total_rows = 0
        empty_rows = 0
        total_words = 0
        non_empty_rows = 0
        
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            
            for row in csv_reader:
                total_rows += 1
                if not row or all(not field.strip() for field in row):
                    empty_rows += 1
                else:
                    non_empty_rows += 1
                    for field in row:
                        if field.strip():
                            words = field.strip().split()
                            total_words += len(words)
        
        return {
            'total_rows': total_rows,
            'empty_rows': empty_rows,
            'total_words': total_words,
            'non_empty_rows': non_empty_rows
        }, None
        
    except Exception as e:
        return None, f"Error reading file: {str(e)}"

def display_analysis(analysis, file_name):
    print(f"\n{'='*50}")
    print(f"CSV File Analysis: {file_name}")
    print(f"{'='*50}")
    
    if analysis:
        print("             Final Analysis is")
        print(f"• Total number of rows: {analysis['total_rows']}")
        print(f"• Number of empty rows: {analysis['empty_rows']}")
        print(f"• Total number of words: {analysis['total_words']}")
        print(f"• Non-empty rows: {analysis['non_empty_rows']}")
    else:
        print("Analysis failed!")

def create_sample_csv():
    sample_data = [
        ['Name', 'Age', 'City', 'Occupation'],
        ['John Doe', '25', 'New York', 'Software Engineer'],
        ['Jane Smith', '30', 'Los Angeles', 'Data Analyst'],
        ['Bob Johnson', '35', 'Chicago', 'Project Manager']
    ]
    
    with open('sample.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(sample_data)
    
    print("Sample CSV file 'sample.csv' created successfully!")

def main():
    print("CSV File Analysis Program")
    print("="*30)
    if not os.path.exists('sample.csv'):
        print("Sample CSV file not found. Creating one...")
        create_sample_csv()
    file_path = 'sample.csv'
    analysis, error = analyze_csv(file_path)
    
    if error:
        print(f"Error: {error}")
    else:
        display_analysis(analysis, file_path)
    while True:
        print(f"\n{'='*50}")
        print("Options:")
        print("1. Analyze another CSV file")
        print("2. Create new sample CSV")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            file_path = input("Enter the path to your CSV file: ").strip()
            if file_path:
                analysis, error = analyze_csv(file_path)
                if error:
                    print(f"Error: {error}")
                else:
                    display_analysis(analysis, file_path)
            else:
                print("Invalid file path!")
                
        elif choice == '2':
            create_sample_csv()
            
        elif choice == '3':
            print("Thank you for using CSV Analysis Program!")
            break
            
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
