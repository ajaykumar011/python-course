# A set is a collection which is both unordered and unindexed.
# Sets are written with curly brackets.


# Note: Sets are unordered, so you cannot be sure in which order the items will appear.
# Duplicates not allowed in sets.

fruits = {"Mango","Guava","Mango","Pineapple","Grapes","Guava"}
print(fruits)
#Ans: {'Pineapple', 'Guava', 'Mango', 'Grapes'}

# as the Sets are unindexed hence we can retrive the value by index number but we can use loop

for x in fruits:
    print (x)

if "Mango" in fruits:
    print("Item avaialable")

#Once a set is created, you cannot change its items, but you can add new items.

fruits.add("PomeGranate")
fruits.remove("Guava") #remove will raise an error if the item does not exist 
fruits.discard("Guava") #this removes but will not raise an error if item does not exist
print(fruits)

#adding the element of one set to anotehr via update() method.
thisset = {"apple", "banana", "cherry","mango"}
tropical = {"pineapple", "mango", "papaya","apple"}
thisset.update(tropical)  #update method inserts into existing set
newset = thisset.union(tropical) #union() method returns a new set with all itesm from both
newset2 = thisset.difference(tropical) #Returns a set containing the difference between two or more sets


print("This set is updated by update method: " + str(thisset))
print("New set after Union: "+ str(newset))
print("Difference of set: " + str(newset2))

# Removes the items in this set that are also included in another, specified set
# the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
#answer - cherry, banana

#Interaction Example that returns a new set
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = a.intersection(b)
print(c)

#clear method clears the set and del keywor delete the set completely.
thisset.clear()
del thisset

#pop() also works here.