filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
    with open('line_count.txt', 'w') as out_file:
        out_file.write(f"Number of lines: {num_lines}\n")
    print(f"Number of lines: {num_lines}")
except FileNotFoundError:
    print("File not found.")