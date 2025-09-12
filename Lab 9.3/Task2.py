# Define a class to represent an SRU student
class sru_student:  # Create a class named sru_student to model student data
    # Initialize the student's basic details
    def __init__(self, name, roll_no, hostel_status):  # Constructor method that runs when creating a new student object
        # Store the student's name
        self.name = name  # Assign the passed name parameter to the instance variable name
        # Store the student's roll number
        self.roll_no = roll_no  # Assign the passed roll_no parameter to the instance variable roll_no
        # Store the student's hostel status (Yes or No)
        self.hostel_status = hostel_status  # Assign the passed hostel_status parameter to the instance variable hostel_status
        # By default set fee status to not paid
        self.fee_paid = False  # Initialize fee_paid as False (not paid) by default

    # Method to update the fee payment status
    def fee_update(self, status):  # Define a method to update the fee payment status
        # Update fee status based on the given True/False value
        self.fee_paid = status  # Set the fee_paid status to the value passed as parameter

    # To print the details of student's 
    def display_details(self):  # Define a method to display all student information
        # Print the student's name
        print(f"Name: {self.name}")  # Display the student's name using f-string formatting
        # Print the student's roll number
        print(f"Roll No.: {self.roll_no}")  # Display the student's roll number using f-string formatting
        # Print the student's hostel status
        print(f"Hostel Status: {self.hostel_status}")  # Display the student's hostel status using f-string formatting
        # Print fee status as Paid or Not Paid based on boolean value
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Not Paid'}")  # Display fee status using conditional expression (ternary operator)


# The Code below takes input from the user 

# Ask user to enter student name
name = input("Enter name: ")  # Prompt user to enter student name and store it in name variable
# Ask user to enter roll number
roll_no = input("Enter roll number: ")  # Prompt user to enter roll number and store it in roll_no variable
# Ask user to enter hostel status (Yes/No)
hostel_status = input("Hostel status (Yes/No): ")  # Prompt user to enter hostel status and store it in hostel_status variable
# Ask if fee is paid (y/n)
fee_paid = input("Fee paid? (y/n): ").lower() == 'y'  # Prompt user for fee status, convert to lowercase, and check if it equals 'y' (returns True/False)

student = sru_student(name, roll_no, hostel_status)  # Create a new student object using the constructor with user inputs
# Update the fee status using the user's input
student.fee_update(fee_paid)  # Call the fee_update method to set the fee status based on user input
# Display all stored details of the student
student.display_details()  # Call the display_details method to print all student information
