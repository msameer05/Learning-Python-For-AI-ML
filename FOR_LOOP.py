# In this cheapter we learn about only for loops:-
#RANGE range():-
#               range() genetrates a sequance of number
# Think of it as saying "count from here to there"
#For loop with numbers:-
for i in range(10,21,1):
    print(i)

n = int(input("enter your number please"))
for i in range(n,(n*10)+1,n):
    print(i)

#lets do some range questions :-
# 1. 10-100
# 2. 23-56
# 3. 0-45
# range(start,stop,step):-
for i in range(10,101,1):
    print(i)
for i in range(23,57,1):
    print(i)
for i in range(46):
    print(i)
# note that we always have to add one extra number for  example if we want count to 20 we will write in loop 21.


# For loop with strings:-
a = "sameer"
for i in a:
    print(i)

# if we dont know lenght :-
A = "sameer"
for i in range(len(A)):
    print(A[i])

# Now we talk about three more functions we will use in loops:-
# 1.break
for i in range(1,11):
    if i == 5 :
        break
print(i)

# 2. else
# 3. continue
for i in range(1,11):
    if i == 3:
        continue
    print(f"signal {i} - passed")
else:
    print("reached home safely")

# Note that we only use else beneath the forth loop if nothing happen then else will execute
# also break stop all the program and continue only skip that part of the program  


# Now lets do some practice Questions:-
# 1. print "hello world "  n times :-
n = int(input("Q1. how many time you want to print : "))
for i in range(1,n+1,1):
    print("hello world")

# 2. print natural number from 1 to n :-
n = int(input("Q2 how much you want to print : "))
for i in range(1,n+1,1):
    print(i)

# Q3. reverse for loop print n down to 1 :-
n = int(input("Q3. how many time you want to print : "))
for i in range(n,0,-1):
    print(i)

# Q4. print the multiplication table of n number:-
n = int(input("Q4 Enter your table number : "))
for i in range(n,(n*10)+1,n):
    print(i)

# Q5. sum of first n natural numbers:-
n = int(input("Q5 enter your number : "))
sum = 0
for i in range(1,n+1):
    sum += i
print(f"the sum of first 10 natural number is { sum}")

# Q6. factorial of a number:-
n = int(input("Q6 enter your number that you want factorial of it : "))
f = 1
for i in range(1,n+1):
    f *= i
print(f)

# Q7. print sum of all even and odd number in a range seperatly:-
n = int(input("Q7 enter your number  : "))
evensum = 0
oddsum = 0
for i in range(1,n+1):
    if i % 2 == 0 :
        evensum += i
    else:
        oddsum += i 
print(f"the evensum is {evensum} and the oddsum is {oddsum} ")

# Q8. print all factors of a number:-
n = int(input("Q8 enter your number  : "))
for i in range (1,n+1):
    if n % i ==  0 :
        print(i)

# Q9. check if a number is perfect (sum of factors = the number of itself):-
n = int(input("Q9 enter you number : "))
s = 0
for i in range(1,n):
    if n % i == 0 :
        s += i
if s == n :
    print("perfect")
else:
    print("not a perfect number")

# Q10. check if number is prime:-
n = int(input("Q10 enter your number to check if prime or not : "))
count = 0
for i in range(1,n+1):
    if n % i == 0 :
        count += 1
if count == 2:
    print("its a prime number")
else:
    print("it is not a prime number")

# Q11. Reverse a string without using built in function:-
s = "Sameer"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev += s[i]
print(rev)

# Q12. check if a string is a palindrome:-
s = input("enter a name to check if it is a palindrome or not : ")
rev = ""
for i in range(len(s)-1,-1,-1):
    rev += s[i]
if s == rev:
    print("it is a palindrome")
else:
    print("not a palindrome")

# Q13.count letter , digit and special symbols in a string:-
let = "sad@%@34253^$GTW$FR"
count_digit = 0
count_letter = 0
count_symbol = 0 
for i in let:
    if i.isdigit():
        count_digit += 1
    elif i.isalpha():
        count_letter += 1
    else:
        count_symbol += 1
print(f"digits are { count_digit} , symbols are {count_symbol} , letter are {count_letter}")