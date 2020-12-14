#Dictionary can contain even list in the keyvalue pair
#Dictionary do not allow duplicates, if this is entered previous values will be overwritten by last values.
#A dictionary is a collection which is unordered, changeable and does not allow duplicates.

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": ["red","darkblack","lightblack","yellow"]
}

laptop = {
    "brand": "HP",
    "colour": "black",
    "cpu": "i5",
    "year": 2000,
    "year": 2020  #this will overwrite the previous value
}

print(car)
print(car["brand"]) #or
var1 = car.get("brand") #get the value of the specific key

var2 = car.values()  #print all values of the dictionary
var3 = car.keys()  #print all keys of the dictionary
print(var1)
print(var2)
print(var3)

#checking the keys in the dict
if "cpu" in laptop:
    print("Yes Key exists")

#changing the values of a key of the dictionary
laptop["brand"]="Dell" #direct chaging 
laptop.update({"brand":"IBM"})  #changing by update method if exists or add new if not exist
car.update({"type":"SUV"})
print(laptop["brand"]) 
#or by print via get method
print(laptop.get("brand"))
print(car.get("type"))

#Loop in Dictonary
print("Looping in Dictionary:")
for x in laptop:
    print(x) #Print the keynames
    print(laptop[x]) #Print the vaules

#another method -Recommended method
for x in laptop.values():
    print(x)
for y in laptop.keys():
    print(y)
for x, y in laptop.items():
    print(x,y)

#Make a copy of a dictionary with the copy() or dict() method:
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
laptop2=laptop.copy()
laptop3=dict(laptop)
print(laptop2)
print(laptop3)

#Nested Dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# The pop() method removes the item with the specified key name:
# The del keyword removes the item with the specified key name:

del car["brand"]

# The clear() method empties the dictionary:
car.clear()

# The del keyword can also delete the dictionary completely:
del car
