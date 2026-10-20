# IN THIS CHEAPTER WE LEARN ABOUT ATTRIBUTES AND METHODS IN OOPS:-
# ATTRIBUTES AND METHODS:-

# TYPES OF ATTRIBUTES:-
# 1.CLASS ATTRIBUTES:-
#                   A normal variable created inside a class is a class attributes
# 2.INSTANCE ATTRIBUTES:-
#                       A attributes created using an instance like self.name, self.age etc. it is known as instance attributes
class car:
    wheels = 4  # class attributes
    def __init__(self, color):
        self.color = color   # object/intance attributes

# TYPES OF METHODS:-
# 1.INSTANCE METHOD:-
#                   An instance method work with instance (object) of the class. this method can access and modify instance attributes
# 2. CLASS METHODS:-
# 3. STATIC METHODS:-

class Animal:
    a = 12 # class attributes
    def __init__(self, name):
        self.name = name   # object/instance attribute
    def hello(self):   # instance/object method  ------> it can captures the location of object
        print(f"how are you my name is {self.name}")
    @classmethod
    def details(self):  # class method ------> it  can capture the location of a class
        print(f"how are you my name is {self.a}")
    @staticmethod
    def speak():  # static method  --------> it can not target any location
        print("hello how are you a am static method")
obj = Animal("lion")
obj.details()