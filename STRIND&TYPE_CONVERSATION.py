#In this chapter we will learn about the String and Type conversion in python
#how a string works internally ?
#                             Each character in a string is represented by a unique number
#                             called its Unicode code point.thats why string use more memory
#                             than other data types like integers or floats.
ord('A') #returns 65
char = chr(65) #returns 'A'

# STRING INDEXING :-
#                  Every character in a string has a positive number called an index and a negative number called a negative index.POSITIVE counts from left to right starting from 0 and NEGATIVE counts from right to left starting from -1.
a = "Hello"
# H   e   l   l   o
# 0   1   2   3   4 --> positive index
#-5  -4  -3  -2  -1 --> negative index
print(a[0]) #H
print(a[-1]) #o

# STRING SLICING :-
#                  Slicing cuts out a piece of a string [start : stop : step] and returns a new string. The start index is inclusive and the stop index is exclusive. The step index is optional and defaults to 1.
a = "Sameer"
print(a[1:4]) #ame (index 1,2,3 - stop index 4 is exclusive)
print(a[::-1]) #reemaS (reverses the string)

#EXAMPLE OF STRING SLICING:-
A = "HELLO HOW ARE YOU"
print(A[6:9]) #HOW (index 6,7,8 - stop index 9 is exclusive)
print(A[14:17]) #YOU (index 14,15,16 - stop index 17 is exclusive)
print(A[0:5]) #HELLO (index 0,1,2,3,4 - stop index 5 is exclusive)


#TYPE CONVERSION :-
#                  Type conversion is the process of converting one data type to another. In python, we can convert between different data types using built-in functions like
#  int()   ---> whole numbers
a = 10.5
a = int(a) #converts float to int
print(a) #10


#  float() ---> decimal numbers
b = 10
b = float(b) #converts int to float
print(b) #10.0


#  str()   ---> text
c = 10
c = str(c) #converts int to string
print(c) #10


#  bool()  ---> True or False
e = 0
e = bool(e) #converts int to boolean
print(e) #False


#Implicit (automatic) type conversion:-
#                                     python converts automatically when needed.
a = 12
print(a/2) #6.0 (int is converted to float automatically)
#int + int --> float


#Explicit (manual) type conversion:-
#                                   you have to tell python to convert
a = 12
a = str(a) #converts int to string
print(a) #12
print(type(a)) #<class 'str'>