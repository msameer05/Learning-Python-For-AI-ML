# IN THIS CHEAPTER WE WILL LEARN ABOUT OBJECTS IN OOPS:-
# OBJECTS:-
#         Objects are instances of classes
# example:-
# 1.whole house
# 2.farrari
# 3.jeep
# 4.bike

# LOOK AT THIS EXAMPLE:-
#                                                       ------------------------------> Materials 
#                                                       !
# BAG FACTORY -------------- REQUIREMENTS --------------------------------------------> Zips
#                                                       !
#                                                       ------------------------------> Pockets

# * for understanding objects first look at this example you have a bag factory and that factory requires materials of the bag, number of zips you need in that bag and number of pockets you need in your bag

# * so thir a level of a blueprint and using the blueprint reeback,campus and some other campanies provided their requiremnts and created their bags

# * thus these companies became objects who created their bags using blueprints

# SYNTAX:-
#       * IT IS VERY EASY TO CREATE OBJECTS YOU JUST TO CALL THE CLASS INSIDE A VARIABLE AND THAT variable become an object.
# * The objects has all the power of a class there a class object can cause attributes and methods of a class
class bags:
    name = "sameer"
    def details(self):
        print("hello , this is the company owner name who created bags.")
Reebook = bags()  # this is a object

class fruit:
    name = "apple"
f = fruit() # creating an object
print(f.name) # access the attributes