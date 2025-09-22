#refactor the below code with explaining about the errors fixed to run it.
def calc_average(marks):
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average   # Typo here

marks = [85, 90, 78, 92]
print("Average Score is ", calc_average(marks))

# The function calc_average is defined to calculate the average of a list of marks.
# The function takes a list of marks as an argument and returns the average of the marks.
# The function uses a for loop to iterate through the list of marks and add them up.
# The function then divides the total by the number of marks to get the average.
# The function returns the average.
# The function is called with the list of marks as an argument and the average is printed.

