#class defination with one self and one get_date function. self is also using default values if 
# No parameter passes from the user
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.image = i
    def get_data(self):
        print(f'{self.real}+{self.image}j')

#class and object calling
p1 = ComplexNumber()
p1.get_data()

p2 = ComplexNumber(4,5)
p2.get_data()

p3 = ComplexNumber(4)
p3.get_data()

# Create another ComplexNumber object  and create a new attribute 'attr'
p4 = ComplexNumber(5)
p4.attr = 10
print(p4.real, p4.image, p4.attr)
#Output: 5 0 10

# Any attribute of an object can be deleted anytime, using the del statement. 
del p4.attr 
print(p4.real, p4.image, p4.attr) #this will throws an error as the p4.attr is deleted

del p1 # Object deletion