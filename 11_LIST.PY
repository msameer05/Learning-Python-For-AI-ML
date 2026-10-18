# IN THIS CHEAPTER WE WILL LEARN ABOUT LISTS IN PYTHON:-
# LIST:-
#       list has order nature . order nature you can access any elements at any point of time.
#       mutable nature you can change any values on your list
#       it can store duplicates you can have duplicates value
list = []
# for example:-
a = [1,2,3,4,5]
print(a[1])


fruits = ["apple" , "banana" , "mango"]
print(fruits[0])
print(fruits[-1])
print(fruits[0:2])
fruits[1] = "grapes"
print(fruits)

# TRAVERSING ON LIST:-
#                   run loops on list
b = [10,20,30,40,50]
# traversing on values
for i in b :
    print(i)
# traversing on index
for i in range(0,len(b)):
    print(b[i])
print(f"{i} : {a[i]}")

# KEY LIST METHODS:-
lst = [3,1,4,1,5]
print(lst.append(2))
print(lst.insert(1,2))
print(lst.remove(3))
print(lst.pop())
print(lst.sort())
print(lst.reverse())
print(len(lst))

# LETS DO SOME PARACTICE QOUESTIIONS

# Q1. print all positive and negative elements seperately.
l = [3,-1,4,-5,9]
pos = []
neg = []
for i in l:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print(f"the positive number are : {pos} and the negative number is : {neg}")

# Q2. find the mean average of all list elements:-
li = [10,20,30,40]
sum = 0
avg = 0
for i in li:
    sum += i
avg = sum/4
print(avg)


# Q3. fimd the greatest elements and print its index.
lis = [4,8,2,9,1]
larg =lis[0]
index = 0
for i in range(len(lis)):
    if lis[i] > larg:
        larg = lis[i]
        index = i
print(larg)

# Q4. find the secound greatest elements
lists = [4,8,2,9,1]
larg = lists[0]
sec_larg = lists[0]
for i in lists:
    if i > larg:
        sec_larg= larg
        larg = i
    elif i > sec_larg:
        sec_larg = i 
print(sec_larg)

# Q5. cheack if the lists is sorted
a = [ 10,20,30,40,50]
for i in range(len(a)-1):
    if a[i] > a[i+1]:
      print("not sorted")
      break
else:
    print("sorted")