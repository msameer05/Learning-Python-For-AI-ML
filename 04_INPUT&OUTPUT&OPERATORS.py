#Now in this cheapter we will learn about input , output and operators in python programming language.

#OUTPUT :-
#        we have three methods to print an output in python programming language.
#BASIC :-
print("Hello World") #prints Hello World

#f-string :-
name = "Sameer"
age = 20
print(f"My name is {name} and I am {age} years old") #prints My name is Sameer and I am 20 years old

#multi-values method :-
name = "Sameer"
age = 20
print("My name is", name, "and I am", age, "years old") #prints My name is Sameer and I am 20 years old

##############################################################################################################

#INPUT input():-
#            remember input() function always takes input in string format so if you want to take input 
#            in integer format then you have to use int() function and if you want to take input in float
#            format then you have to use float() function.
name = input("Enter your name: ") #takes input in string format
age = int(input("Enter your age: ")) #takes input in integer format
print(f"hello {name} you are {age} years old") #prints hello Sameer you are 20 years old

##############################################################################################################

#NOW COMES TO OPERATORS :-
#                       THERE are 7 types of operators in python programming language.
#1. Arithmetic Operators
#                      numeric operations like addition, subtraction, multiplication, division, modulus,
#                      exponentiation and floor division are performed using arithmetic operators.
#number have three types in python programming language.
#1. int :- 
#        integer numbers like 1, 2, 3, 4
#2. float :-
#           decimal numbers like 1.1, 2.2, 3.3, 4.4
#3. complex :-
#            complex numbers like 1+2j, 3+4j
#OPERATORS :-
        #  (+) Addition
print(10 + 5) #prints 15

        #  (-) Subtraction
print(10 - 5) #prints 5

        #  (*) Multiplication
print(10 * 5) #prints 50

        #  (/) Division
print(10 / 5) #prints 2.0

        #  (%) Modulus
        #            modulus is a mathematical operation that returns the remainder of a division.
print(10 % 5) #prints 0

        #  (**) Exponentiation
        #                    exponentiation is a mathematical operation that raises a number to the power
        #                     of another number.
print(10 ** 5) #prints 100000

        #  (//) Floor Division
        #                    floor division is a division in which the result is rounded down to the nearest integer.
print(10 // 5) #prints 2

#rules that first operation will be performed first in python programming language:-
              # () Parentheses
              # ** Exponentiation
              # * , /, //, % Multiplication, Division, Floor Division, Modulus
              # + , - Addition, Subtraction
print(3 + 4 * 2)#prints 11
print(15 // 4 + 15 % 4) #prints 4
print(3 + 2 ** 2 * 5 - 1) #prints 22

##############################################################################################################

#2. Assignment Operators
#    Assignment operators are used to assign values to variables.
# = Assignment
x = 5
print(x) #prints 5

# += Addition Assignment X = X + 3
x += 3
print(x) #prints 8

# -= Subtraction Assignment X = X - 3
x -= 3
print(x) #prints 5

# *= Multiplication Assignment  X = X * 3
x *= 3
print(x) #prints 15

# /= Division Assignment     X = X / 3
x /= 3
print(x) #prints 5.0

# %= Modulus Assignment      X = X % 3
x %= 3
print(x) #prints 2

# **= Exponentiation Assignment    X = X ** 2
x **= 2
print(x) #prints 4

# //= Floor Division Assignment     X = X // 2
x //= 2
print(x) #prints 2

##############################################################################################################

#3. Comparison Operators
#   Comparison operators are used to compare two values and return a boolean value (True or False).
#OPERATORS :-
# == Equal
print(5 == 5) #prints True
# != Not Equal
print(5 != 5) #prints False
# < Less Than
print(5 < 10) #prints True
# > Greater Than
print(5 > 10) #prints False
# <= Less Than or Equal To
print(5 <= 10) #prints True
# >= Greater Than or Equal To
print(5 >= 10) #prints False

##############################################################################################################

#4. Logical Operators
#   Logical operators are used to combine conditional statements.
# and Returns True if both statements are true
print(True and True) #prints True
print(True and False) #prints False
# or Returns True if one of the statements is true
print(True or False) #prints True
print(False or False) #prints False
# not Reverses the result, returns False if the result is true
print(not True) #prints False
print(not False) #prints True

print(15 > 3 and 10 == 10) or (4 != 4 and 2 < 1) #prints True
print((10 == 10 and 23 != 23) or (34 == 12 and bool("hello"))) #prints False
print(not (5 == 5 and 3 != 4) or (10 > 20))#prints False

##############################################################################################################

#5. Identity Operators
#   Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
# is Returns True if both variables are the same object
x = 5
y = 5
print(x is y) #prints True
# is not Returns True if both variables are not the same object
x = 5
y = 10
print(x is not y) #prints True

##############################################################################################################

#6. Membership Operators
#   Membership operators are used to test if a sequence is presented in an object.
# in Returns True if a sequence with the specified value is present in the object
x = [1, 2, 3, 4, 5]
print(3 in x) #prints True
# not in Returns True if a sequence with the specified value is not present in the object
x = [1, 2, 3, 4, 5]
print(6 not in x) #prints True

##############################################################################################################

#7. Bitwise Operators
#   Bitwise operators are used to compare (binary) numbers.
# & AND Sets each bit to 1 if both bits are 1
print(5 & 3) #prints 1
# | OR Sets each bit to 1 if one of two bits is 1
print(5 | 3) #prints 7
# ^ XOR Sets each bit to 1 if only one of two bits is 1
print(5 ^ 3) #prints 6
# ~ NOT Inverts all the bits
print(~5) #prints -6
# << Zero fill left shift Shift left by pushing zeros in from the right and let the left
#most bits fall off
print(5 << 1) #prints 10    
# >> Zero fill right shift Shift right by pushing zeros in from the left and let the right
#most bits fall off
print(5 >> 1) #prints 2

##############################################################################################################