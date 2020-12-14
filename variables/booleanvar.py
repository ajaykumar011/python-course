#Everthing is true expect zero
x=0
y="Hello"
print(bool(x))   #false
print(bool(y))   #true

print(bool(["apple", "cherry", "banana"])) #true

#Checking with If else
if x:
    print("This is true")
else:
    print("This is false")

#functions returns false with emtpy, blank or zero or None Value

print(bool([]))
print(bool(""))
print(bool({}))
print(bool(None))

#functions can also return true false

x="awesome"
def myfunc():
    global x  # to make the varible global
    x="fantastic"
    #return x
    return True

myfunc()
if myfunc():
    print("Function returns True")
else:
    print("Function returns False")

print("Value of x is " +x)

#The isinstance() function returns True if the specified object is of the specified type, otherwise False.
z=200
print(isinstance(z, int))