class Double:
    x = 5
    

p1=Double()
#print(p1.x)

#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
    def myfunc(self):
        print("Hello my name is: " + self.name)
        if self.age >= 18 and self.age <=100:
            print("You are a Voter")
        else:
            print("Sorry ! Non-Voter or Invalid age")

#Object creation by calling the Class 'Person'
#p1 = Person("Ajay",40)
user_name=input("Enter your name: ")
user_age = input("Enter your age: ")
user_age=int(user_age)
p1=Person(user_name,user_age)  #Object p1 is defined and parameters are sent to class, user_name will become name and user_age will become age in class

print(p1.name) #Object name with class variable
print(p1.age)
p1.myfunc() # calling the function via object p1 and p1 is from class Person.
