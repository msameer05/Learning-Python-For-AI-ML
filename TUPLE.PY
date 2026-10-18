# IN THIS CHEAPTER WE WILL LEARN ABOUT TUPLE IN PYTHON
# TUPLE:-
#       A tuple is exactly like a list , execept you cannot change it once created
# use tuple for data that should stay constant
# like days of the week , coordinates, or config values
# FOR EXAMPLE:-
days = ("mon", "tue", "wed")
print(days[0])
# days[0] = " x"  ------>  givrs an typeError

TUPLE = ()

# Tuple methods:-
#               there are only two methonds in tuple
# 1. index()
# 2. count()
# for example:-
t = (1,2,3,2,1)
t.index(2)  # ------> first position of 2
t.count(2)  # ------> 2 appears twice in tuple

def student():
    return "sameer",21,"sameer@gmail.com"
info = student()
name ,age, mail =info
print(name)
print(age)
print(mail)
print(info)