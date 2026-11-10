# In this cheeapter we will learn about last and fourth piller of oops which is abstraction.
# ABSTRACTION:-
# * abstruction does not exist in python  but we can achieve it using a library we will see what is library later.
# * abstraction is used to simplifying complex system by focusing on essential features and hiding unneccessary details.
# * it is used to define a common interface for different subclasses

# ABSTRACTION CLASSES AND METHOD :-
# * abstruction classes are classes that contain one or more abstraction method 
# * also  subclasses mudt provide the implementation.

from abc import ABC , abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        print("dog says woof")
class cat(animal):
    def make_sound(self):
        print("cat  says meow")

# that all about abstraction 
