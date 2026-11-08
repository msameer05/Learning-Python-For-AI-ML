# In this cheapter we will learn about secound piller of oops which is polymorphism.
# POLYMORPHISM.
#             polymorphism is a greek word which means many forms.
# * In programming it allows the same interface or method name to behave differently depending on the object or content it is acting upon.

# TYPES OF POLYMORPHISM:-
# * polymorphism can be achieved in python in two ways will if we talk about compile time language there are three 3 ways but python does not support method over-loading and operator overloading is also not supported in python but we can achieve polymorphism in python by two ways which are as follows:-

class Animal:
    def speak(self):
        print("animals will not speak")
class humans:
    def speak(self):
        print("we are humans we can speak")

obj = Animal()
obj2 = humans()

obj.speak()
obj2.speak()

# * method overloading means having same name method inside a class but in python the latest definition will override the previous one.

# METHOD OVER-RIDING:-
#                   * THIS is where a child class over-rides a method of the parent class and python decides at runtime whicih method call based the object type. This is called run time polymorphism.
class Animal:
    def sound(self):
        print("animals will make sound")
class Dog(Animal):
    def sound(self):
        print("dog will bark")
obj = Animal()
obj2 = Dog()

obj.sound()
obj2.sound()

#                                   OVER-RIDING
class Animal:
    a = 12
    def __init__(self,name):
        self.name = name
    def details(self):
        print(f"your name is {self.name} and your age is {self.a}")
class Humans(Animal):
    b = 20
    def details(self):
        print(f"you info is {self.name}")
obj = Humans("sameer")
obj.details()    # this will call the child class method because it is over-riding the parent class method.

# when we are doing inheritance and parent and child classes have same method name so the child class method will override the parent class method and this is called method over-riding.