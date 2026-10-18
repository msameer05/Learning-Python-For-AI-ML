# NOW IN THIS CHEAPTER WE LEARN ABOUT FUNCTIONS IN PYTHON PROGRAMMING LANGUAGE:-
# FUNCTIONS :-
#           A function is a reusable block of code with a name
# instead of writing the same logic 10 times, you write it once as a function and call it 10 times
# FOR EXAMPLE:-
def greet():
    print("hello, welcome to python")
greet()   # this is the calling function

# APPROCHES :-
# 1. primitive approch
# 2. fuctional approach
# 3. oop approach

# two more things in fuctions is 
# 1. parameter:-
#               parametr are the values you accept while calling the function
# 2. arguments:-
#               arguments are the value you provide to parameters while calling the function
# FOR EXAMPLE:-
def addition(a,b):  # a and b is the parameters
    print(a + b)
addition(13,25)  # 13 and 25 is an arguments

# TYPES OF ARGUMENTS:-
# 1. positional arguments:-
#                           order matters
def add(a,b):
    return a+b
add(5,3)

# 2. DEFULT ARGUMENTS:-
#                       work even without passing a matter
def greet(name = "guest"):
    print(f"hello {name}")
greet()
greet("sameer")

# 3. KEYWORD ARGUMENTS :-
#                       Pass in any order
def info(name,age):
    print(f"{name} is {age}")
info(age = 25, name = "sameer")