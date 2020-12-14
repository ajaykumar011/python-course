def my_func():
    print("hello World")

def convert(text):
    return text.upper()

def my_sum(x,y):
    return x+y


my_func()
x=convert("love") #Arguments are often shortened to args in Python documentations.
print(x)
print(my_sum(10,20))

#If the number of arguments is unknown, add a * before the parameter name:
#Argument as List
def my_func2(*kids):
    print("The youngest child is " + kids[2])

my_func2("Email","Tobis","Linus")

#argument as key=value syntax
def my_func3(child3, child2, child1):
    print("The youngest child id " + child3)

my_func3(child1 = "Toko", child2 = "b2", child3 = "choti")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")