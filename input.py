##### input = string
#The input function takes in whatever the user types and stores it as a string. 

name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))
# Hello there, Suji!


# If you want to interpret their input as something other than a string, 
# like an integer, 
# as in the example below, 
# you need to wrap the result with the new type to convert it from a string.

num = int(input("Enter an integer: "))
print("hello" * num)
# 5
# hellohellohellohellohello


# We can also interpret user input as a Python expression using the built-in function eval. This function evaluates a string as a line of Python.
result = eval(input("Enter an expression: "))
print(result)
# 2 * 3
# 6

# 3 > 5
# Flase


### EXAMPLE
"""
names =  # get and process input for a list of names
assignments =  # get and process input for a list of the number of assignments
grades =  # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
"""

### SOLUTION
names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))