# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person: #Parent Class
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def welcome(self):
        print("Welcome to Home " + self.firstname , self.lastname)
class Student(Person): #child class of Parent 'Person'
    pass


p1 = Person("Ajay", "Kumar")
p1.welcome()

p2= Student("Sushil", "Kumar")
p2.welcome()
