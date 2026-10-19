# NOW IN THIS CHEAPTER WE WILL LEARN ABOUT DICTIONARIES:-
# KEY VALUE STORAGE:-
#                   A dictionary stores data as key : value pairs
# like a real dictionaries where you look up a word (key) to find its meaning (value)
# dictionary:-
dictionary = {"a" : 10 , "b" : 20}

# for example:-
person = {"name" : "sameer" , "age" : 20 , "city" : "abbottabad"}
print(person["name"]) #prints values "sameer"
person["age"] = 21   # update the value of age 20 to 21
person["course"] = "python"  # adds new pairs of key and value
del person["city"]   # delete the pair of city
for key,val in person.items():
    print(key,"-",val)


d = {1:10,2:20,3:30,4:40}
# METHODS:-
# 1.FROMKEYS:-
q = d.fromkeys([11,22,33], 50) 
print(q)  #create and add new pairs

# 2. GET:-
d.get(1) #prints value

# 3.ITEMS:-
print(d.items())  # returns key-value pairs as list of tuples

# 4.keys:-
print(d.keys()) #print a list

# 5.value:-
print(d.values())  #print all values

# 6.set_defult
d.setdefault(4,4000)

# 7.pop:-
d.pop(4) #remove the last by defult

# 8.popitem:-
d.popitem()

# 9. CLEAR:-
d.clear()  # clear all the dictionary

# traversing:-
for i in d:
    print(f"{i} : {d[i]}")

# lets do some practice questions:-
# Q1. merge two dictionaries in to one
d1 = {"a" : 10, "b" : 20, "c" : 30}
d2 = {"d" : 40, "e" : 50, "f" : 60}
for i in d2:
    d1[i] = d2[i]
print(d1)

# Q2 sum all values in dictionaries
d1 = {"a" : 10, "b" : 20 ,  "c" : 30}
sum = 0
for i in d1:
    sum += d1[i]
print(sum)

# Q3. count the frequancy of each elements in a list using a dictionary
l = ["a", "b","a", "c" , "b" , "a" , "c"]
d = {}
for i in l:
    if i in d.keys():
        d[i] = d[i]+1
    else:
        d[i]=1
print(d)

# Q4. continue two dictionary , adding values for comming keys
d1 = {"a" : 10, "b" : 20, "c" : 30}
d2 = {"c" : 40, "e" : 50, "f" : 60}  
for i in d2:
    if i in d1.keys():
        d1[i] = d1[i]+d2[i]
    else:
        d1[i] = d2[i]
print(d2)