#a = 10
#b = 5
a = input("Enter first name (A): ")
b = input("Enter second number (B): ")

if b > a:
    print("B is greater than a")
elif a ==  b:
    print("Equal")
else:
    print("A is greater than b")

#oneline command
if a>b: print("A is big boss")
#This technique is known as Ternary Operators, or Conditional Expressions.
print("B is bigboss") if b > a else print("A is bigboss")

#Unary Operators
a = 310
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# AND and OR
c = 350

if a >100 and a <300:
    print ("both conditions are true")
if a >100 or a <300:
    print ("any condition is true")
