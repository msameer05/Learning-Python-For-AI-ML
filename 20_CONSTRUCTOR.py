# IN THIS CHEAPTER WE WILL LEARN ABOUT THE CONTRUCTOR IN OOPS:-
# CONSTRUCTOR:-
#           * you saw last example where we want materials ,zips and pockets from the user to create objects

# * if we talk about a function we can ask the use using parameters for that we use constructors

#                       *A constructor is a method that runs automatically when we call and this 
#                               constructor function will target the objects location

class student:
    def __init__(self,name):  # that  __init__  is the contructor
        self.name = name  # instance attributes
s = student("sameer")  # create an object with value
print(s.name)   # accessing the attributes

# * To target the object location we use self keyword
# SELF :-  ---------->  target the location of object

# * for clear understanding watch the code carefully.we will create the bag factory and will create multiple objects where self will target the specific location of the object

class bags:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
Reebook = bags("leather", 3, 2)
Cumpus = bags("polyster", 2, 4)
print(Reebook.material)
print(Cumpus.material)

