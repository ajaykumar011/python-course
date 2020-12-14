#for loop

friends=["Raja","Khaja","Deepak","Rajkumar","Shankar"]
for x in friends:
    #print(x)
    pass

laptop = {
    "brand": "HP",
    "colour": ["black","red","white"],
    "cpu": "i5",
    "bluetooth": True,
    "year": 2020,
    "weightkg": 1.2
    }

#Loop in Dictonary
print("Looping in Dictionary:")
for x in laptop:
    print(x) #Print the keynames
    print(laptop[x]) #Print the vaules

#another method -Recommended method
print("Another method of printing all values, keys, items(both)")
for x in laptop.values():
    if x == "i5":
        print(x)
        break
for y in laptop.keys():
    print(y)
for x, y in laptop.items():
    print(x,y)

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue  #donot print banana and continue back to loop
  print(x)

#range
for x in range(1,5):
    print(x)
#range with increment
for x in range(1,20,2): #increment of 2
    print(x)

for x in [1,4,6,7,8]:
    print(x)

#Nested Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

