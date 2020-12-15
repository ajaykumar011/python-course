# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person: #Parent Class
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def welcome(self):
        print("Welcome to Home " + self.firstname , self.lastname)
class Student(Person): #child class of Parent 'Person'
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        self.graduationyear = year
        
# p1 = Person("Ajay", "Kumar")
# p1.welcome()

p2= Student("Sushil", "Kumar", 2019)  #creating object p2 with 2 parent and one child parameters 2019 is sent to year variable and then self.graduationyear .
p2.welcome() #calling parent method to print firstname and lastname
print(p2.graduationyear) #calling 
