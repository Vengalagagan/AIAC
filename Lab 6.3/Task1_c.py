Students_name = str(input("Enter the number of students: "))
Roll_number = str(input("Enter the roll number of the student: "))
marks = int(input("Enter the marks of the student: "))  
print("----------Student Details----------")
print("Student-name: ", Students_name) 
print("Roll-number: ", Roll_number) 
print("Marks: ", marks) 
if (marks >= 90) :
    print("Grade:A")
elif (marks >= 75) :
    print("Grade:B") 
elif (marks >= 60) :
    print("Grade:C")
else :
    print("Fail")
    

    
    
    
    
    