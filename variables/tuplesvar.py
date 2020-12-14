# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.It allows duplicate values.

friends=("Raju","sachin","Sushil","Mandeep","Raju","Rishav")
print(friends)
print(type(friends))
print(len(friends))

#multiple datatypes
t1=("hello",1,True,30.4)
print(t1)

#access tuples are like list acess
print(t1[0:3])
print(t1[3])
print(t1[-2])

#changing values in tuple is not possible as tuples are immutable (no change after creation)
#But we can change it by backdoor method means changing the tuple to list and create tuple from list.
friends2=list(friends)
print(type(friends2))

#append only work work when converted to list and converted back to tuple
tuple1 = ("apple","banana","cheery")
y = list(tuple1)
y.append("guava")
tuple1 = tuple(y)
print(tuple1)

#Tuples are unchangeable, so you cannot remove items from it
#removing from the tuple with the same conversion method
flowers = ("Rose","Lotus","Jasmine","Sunflower")
y = list(flowers) 
y.remove("Jasmine") #y.pop(2)  #both are used to remove
flowers = tuple(y)
print(flowers)

#The del keyword can delete the tuple completely:
#del flowers

for i in range(len(flowers)):
    print(flowers[i])

tuple1 = ("a", "b" ,"c","a","c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#count the number "a"
x=tuple3.count("a")
print(x)

#Get the index of the element
y=tuple3.index('b')
print(y)