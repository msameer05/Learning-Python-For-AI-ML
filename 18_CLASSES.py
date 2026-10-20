# IN THIS CHEAPTER WE WILL LEARN ABOUT CLASSES:-
# CLASSES:-
#         A class is a blueprint for creating objects
# think of a class like the blueprint of a house. identifies what the house needs
# an object is the house built is the actual house built using needs.

# example:-
#  A Car Factory  
# 1.body types
# 2.tyers
# 3.engin types
#  a car factory is an objects and the other is classes you can make from a farrari , bike , jeep etc:-

# SYNTAX:-
# * A class is also created with a basic keyword class and a name in front of it
class car:
    brand = "toyota"
# * Creating a class is a super simple now lets see what is inside class

# There are two(2) types inside class attributes and methods
# 1.ATTRIBUTES:-
#               VARIABLE defines inside the class
# 2.METHODS:-
#           FUNCTION defines inside a class
class Animal:
    species = "dog" # attributes

    def make_sound(self):
        print("bark")  # methods

# ACCESSING ATTRIBUTES AND METHODS:-
# * A class is initialized only one time when we first run the program. and for attributes and methods we have to first access the class and then attributes and methods.
class Animal:
    type = "cat"

    def sound(self):
        print("meow")
print(Animal().type) # access attributes
Animal().sound()  # call methods