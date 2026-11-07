# IN this cheapter we will learn about first piller of oop which is inheritance.

# INHERITANCE:-
#               IN general terms inheritance means property or any thing which is inherited from parents to child.
# * it works between classes.
# * Inheritance  allows a class (child class) to inherit properties and behavior (attributes and properties) from another class (parent class).

# BENEFIT OF USING INHERITANCE IN CODE:
# 1. code reusabilty
# 2. organized structure of code
# 3. easy to maintain and extend the code.

# SYNTAX IN INHERITANCE:-
# * SYNTAX IS VERY SIMPLE JUST LIKE YOU TAKE PARAMETERS IN Function here you will take parametres but those parameters will be class.
class parent:
    def speak(self):
        print("i can speak")
class child(parent):
    pass
# * now the inherited class has all the power of parent class that means all the methods,attributes can be accessed by the instance of child class as well.
# * your child class objects has all the power to acess the attributes and methods of parents class.

# CONSTRUCTORS IN INHERITANCE:-
# * LET SAY YOU HAVE CREATED A PARENT CLASS WITH a constructor function inside it and then this class is inherited by another class then the constructor function of parent class will work for the child class as well.
class parent:
    def __init__(self,name):
        self.name = name
class child(parent):
    def display(self):
        print(f"my name is {self.name}")
# * now let say you need a new parameter in your child class you have to create a constructor function for you child class but the parameters that can be initiated in the parent class will be initiated using the super() function. super function will target the parent class.
class parent:
    def __init__(self,name):
        self.name = name
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def display(self):
        print(f"my name is {self.name} and i am  {self.age} years old")

# TYPES OF INHERITANCE:
# 1. SINGLE INHERITANCE:-
#                      all the inheritance we saw above was single inheritance where one child class is inherited from one parent class.
class bagfactory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
    def details(self):
        print("your bag details are :")
        print(self.material)
        print(self.zips)
        print(self.pockets)
class reebok(bagfactory):
    def __init__(self,material,zips,pockets,color):
        super().__init__(material,zips,pockets)
        self.color = color

    def details(self):
        print(self.color)
        return super().details()

bag1 = bagfactory("leather","2","3")
bag2 = reebok("leather","2","3","black")

# 2. MULTIPLE INHERITANCE:-
#                        * in multiple inheritance one child class can inherit from multiple parent classes.

# * multiple inheritance means there will be 2 parents class and only 1 child class and the child class will inherit all the attributes and methods of both parents classes.
# NOTE:-
# * if both the parent classes have same method name then the method of first parent class will be executed.
class Animal:
    def __init__(self,name):
        self.name = name
class Human:
    def __init__(self,id):
        self.id = id
class robot(Animal,Human):
    def __init__(self,name,id):
        Animal.__init__(self,name)
        Human.__init__(self,id)
robo = robot("sameer",661)

person = child("sameer", 20)
person.display()
bag1.details()
bag2.details()
print(f"robot name: {robo.name}, id: {robo.id}")
