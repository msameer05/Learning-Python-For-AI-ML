#In this chapter we will learn two things about python programming language. 
# COMMENTS AND VARIABLES
#COMMENTS: 
#         Comments are used to explain the code and make it more readable.
#         In Python, comments start with the '#' symbol. Anything after the
#         '#' on that line is ignored by the Python interpreter.

#This line is for printing hello world on the screen
print("Hello World")  # This is a comment after a line of code


#for multiple line comments, we can use triple quotes (''' or """) to enclose the comment text.
'''
This is a multiple line comment.
It can span across several lines.
'''

#VARIABLES:
#         Variables are used to store data in a program. In Python, you don't need
#         to declare the type of a variable explicitly. You can simply assign a value
#         to a variable, and Python will determine its type automatically.

#Some examples of variables in Python:
Same = 10  # An integer variable
name = "John"  # A string variable
price = 19.99  # A float variable
is_valid = True  # A boolean variable

print(Same)  # Output: 10
print(name)  # Output: John
print(price)  # Output: 19.99
print(is_valid)  # Output: True


#we have same cases to write correct variable names in python.
#1. camel case: 
#               The first letter of the first word is lowercase, and the first
#                letter of each subsequent word is uppercase. 
# Example: myVariableName
myVariableName = "same"

#2. Pascal case:
#                The first letter of each word is uppercase. 
# Example: MyVariableName
MyVariableName = "jhon"

#3. Snake case:
#                All letters are lowercase, and words are separated by underscores.
#  Example: my_variable_name
my_variable_name = "doe"