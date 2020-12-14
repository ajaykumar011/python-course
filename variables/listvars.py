name=["Soma", "Ajay","Vijay","Loko","Susil","Prince","Vicky"]
print(name)
#accesing via positive index
print(name[0])
print(name[2:4]) #Prints 0,1,2(index) to before 4th index. 4th index not include only =(0,1,2,3)
print(name[:3])
print(name[4:])
print('Negative Index range: ' + str(name[-4:-1])) #This example returns the items from "Loko" (-4) to, but NOT included. "Vicky" (-1):
#Answer- Negative Index range: ['Loko', 'Susil', 'Prince']

#accessing via negative index -1 (last item), -2 (second last item)
print('Last item in list is ' + name[-1])

#List allows duplicate values
months=["Jan","Feb","Jan","Nov","Dec","April"]
#Checking items if exists by using If and 'In list'
if "Nov" in months:
    print("Item Exists")
else: 
    print("Item not Exists")

#list allows multiple types
aspirants=["Ajay",40,True,"CloudComputing"]

#list showing type and len
print(type(aspirants))
print('Length of List is ' + str(len(aspirants)))

#Reassigning contents of list
months=["Jan","Feb","March"]
print(months)

#List as constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#List change and Replace items
gf=["Riya","Sona","Pinki","Puja","Jaggu","JS","Sadhu"]
gf[-2]="Suman"
gf[0:2]=["Toko","Moko"]
print(gf)
print(len(gf))

#List insert new item without replacing them
gf.insert(1,"Rubana")  #1 stands for 2nd itmes
print(gf)
print(len(gf))

#appending to the list after the last item
gf.append("Jannu")
print(gf)

#remove the item by itemname and pop the item by indexnum
gf.remove("Moko") #remove the item name
gf.pop(-1)  #removes the last item
print(gf)
print(gf.index("Rubana"))
print(gf.count("Jannu"))

#list the elements via loop
for i in range(len(gf)):
    print(gf[i])

#find the items in list and append to new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:  #Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name. (Optional)
    newlist.append(x)

print(newlist)

#another method to copy one list to another
#newlist2 = [x for x in fruits if "apple" in fruits] #checks the list for apple 
newlist2 = [x for x in fruits if "a" in x] #checks the items for letter containing 'a'
#newlist = [x for x in fruits if x != "apple"]
print(newlist2)

#examples
newlist = [x for x in fruits]
print(newlist)
#newlist = [x.upper() for x in fruits]
print(newlist)

newlist.sort()
newlist.sort(key=str.lower)  #Perform a case-insensitive sort of the list
newlist.reverse() #descending sort
print(newlist)

#copy the list to new one via copy function
newlist2=newlist.copy()
print(newlist2)

#Join 2 list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
list1 = list1+list3
print(list3)
print(list1)