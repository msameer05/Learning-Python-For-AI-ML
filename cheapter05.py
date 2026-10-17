#NOW In this cheapter we will learn about the conditional statements in python. 
#CONDITIONAL STATEMENTS :-
# Conditional statements are used to perform different actions based on different conditions. The most common conditional statements in Python are if, elif, and else.
#first we will learn about the if statement.
#1. If Statement
#   The if statement is used to test a specific condition. If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.
x = 10
if x > 5:
    print("x is greater than 5")
#   In this example, the condition x > 5 is true, so the code block inside the if statement is executed and "x is greater than 5" is printed to the console.
#2. Elif Statement
#   The elif statement is used to test multiple conditions. If the first condition is false, the elif statement is checked. If the elif condition is true, the code block inside the elif statement is executed. If the elif condition is false, the code block is skipped.
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
#   In this example, the first condition x > 15 is false, so the elif statement is checked. The condition x > 5 is true, so the code block inside the elif statement is executed and "x is greater than 5 but not greater than 15" is printed to the console.
#3. Else Statement
#   The else statement is used to execute a code block if none of the previous conditions are true.
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is not greater than 5")
#   In this example, the first condition x > 15 is false, so the elif statement is checked. The condition x > 5 is true, so the code block inside the elif statement is executed and "x is greater than 5 but not greater than 15" is printed to the console. If both conditions were false, the code block inside the else statement would be executed and "x is not greater than 5" would be printed to the console.


#Now we will do some practice questions on conditional statements in python.
#Q1. you have to take input of age and tell the person can vote or not. (age >= 18)
age = int(input("Enter your age: "))
if age >= 18 :
    print("you can vote sir. thanks")
else:
    print("you can not vote sir. try next year thanks")

#Q2. Accept two numbers and print the greatest between them .
number_1 = int(input("please enter your first number : "))
number_2 = int(input("please enter your secound number : "))
if number_1 > number_2 :
    print(f"The greater number is {number_1}")
elif number_1 < number_2:
    print(f"the greater number is {number_2}")
else:
    print("invalid number")

#Q3. Accept gender from user and print a greeting messege.
gender = input("enter your gender please : ")
if gender == "M" or gender == "m":
    print("Hello sir! how can i help you :")
elif gender == "F" or gender == "f":
    print("Hello Mam! how can i help you :")
else :
    print("invalid gender")

#Q4. Accept a year cheack if it is a leap year or not ?
year = int(input("Enter your year please : "))
if year % 100 == 0 or year % 400 == 0 :
    print("it is a leap year")
elif year % 100 == 0 or year % 4 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")

#Q5. Accept temperature in c and print a description
temp = int(input("please enter your temperature : "))
if temp <= -5:
    print("freezing cold")
elif temp > 20 or temp <= 30:
    print("it a pleasent temperature here")
elif temp > 30 or temp >= 45:
    print("it is very hot temperature")
else:
    print("invalid")