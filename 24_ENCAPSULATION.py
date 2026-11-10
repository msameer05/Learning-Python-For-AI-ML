# In this cheapter we will learn about third piller of oop which s encapsulation.
# ENCAPSULATION.
#    *encapsulation means putting data (variables) and code (function) togather in one place inside a class.
#    *it also means hidinng the internal details of how things work and only showing what is needed.
#    * it keeps data safa from being changed by mistake.
#    * it makes your code clean and easy to use.
#    * it gives control over what others can access or changed.

# ACCESS MODIFIERS IN PYTHON:-
# Access modifers means how we give access to our attributes and methods to the object or inherit classes.
# There are three types of access modifiers in Python:

# 1. Public attributers and methods:
#     * Public attributes and methods are accessible from anywhere, both inside and outside the class.
class factory:   #public class attributes 
    def __init__(self,type,tyre,color):
        self.type = type  # public object attributes
        self.tyre = tyre
        self.color = color

obj = factory("car","4","red")
obj.name = "bus"
print(obj.name)
print(obj)

# 2. Protected attributes and methods:
#     * Protected attributes and methods are accessible within the class and its subclasses, but not from outside the class.
class factory:
    def __init__(self,type,tyre,color):
        self._type = type  # protected object attributes
        self._tyre = tyre
        self._color = color
obj = factory("car","5","red")
print(obj._type)

# 3. Private attributes and methods:
#     * Private attributes and methods are only accessible within the class itself and not from outside the class or its subclasses.
class factory:
    def __init__(self,type,tyre,color):
        self.__type = type  # private object attributes
        self.__tyre = tyre
        self.__color = color

    def details(self):
        return f"Type: {self.__type}, Tyre: {self.__tyre}, Color: {self.__color}"
    
obj = factory("car","4","red")
print(obj.details())

# class demo
class demo:
    def __init__(self):
        self.__private_variable = 42  # Private variable

    def __private_method(self):  # Private method
        return "This is a private method."

    def public_method(self):
        return f"Accessing private variable: {self.__private_variable}, and calling private method: {self.__private_method()}"

obj = demo()
print(obj.public_method())
