# Now in this cheapter we will learn about while loops:-
# WHILE LOOPS:-
#             the while loop keep running as long as a condition is True
# you use it when you do not know how many times you will need to repeat
# FOR EXAMPLE:-
count = 1
while count <= 5:
    print(count)
    count += 1

# be carefull because i said before already this loop needs condition if conditions is always true the loop will be infinte 
# for example
###############################################################################
# while True:
#     print("hello world")
###############################################################################
# this loop will run forever because the the condition will be always true

# let practice some questions of it
# Q1. seperate each digit of a number and print on a new line:-
num = int(input("Q1 : enter your number : "))
while num > 0 :
    print(num % 10)
    num = num // 10
print(num)


# Q2. Accept a number and print it reverse
n = int(input("Q2 : enter your number : "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print(rev)


# Q3. check if a number is palindrome (equal to its reversed):-
n = int(input("Q2 : enter your number : "))
s = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if s == rev:
    print("palindrome")
else:
    print("not a palindrome")


# Q4. build a number gussing game computer picks a random number user gusing until correct
import random
comp = random.randint(1,100)
while True:
    user = int(input("enter your guessing number : "))
    if user == comp:
        print("congretulations , you have won!")
        break
    elif user < comp:
        print("go little higher : ")
    elif user > comp:
        print("go little lower")
    else:
        print("invalid options")