
#string example
fname='Ajay'
lname='Kumar'
fullname=fname+lname
print('MyName is : '+fullname)
print(type(fullname))
#To store long string
address='''  
F-298, Sector-63, Noida
Uttarprades
PIN 201301
'''

print("My Address is \n--------------------"+address)
x=10
print(str(x))
print(int(x))
print(type(int(x)))
y=type(int(x))
print(y)


#Escapte Sequence
#weather="It's "kind of" Sunny"
weather="It\'s \"kind of\" Sunny"
print(weather)

#formatted string - f stands for formatted string followed with '
print(f'hi My first name is {fname} \nand my last name is {lname}')

#Method to remove whitspace from beginning and end of the string
fstring=fullname.strip()
print(fstring)

print(fullname.upper())
print(fullname.lower())

#String as set of characters
name='AjayBabu'
print(name[3:5])
print(name[:5])
print(name[2:])
print(name[-1:-3])
print(name[::-1]) # reverse order answer- ubaByajA
print(name[0:10:2]) #step over or increment by 2



#methods (please note strings are immutable)
quote="honest is the best policy"
print(quote.capitalize())
print(quote.find('is'))
print(quote.replace('is','are')) # do not change the origial one as strings are immutable
quote2= quote.replace('is','are')
print(quote2)

birth_year = input('What year were you born? ')
birth_year =  int(birth_year)
if birth_year < 2020 and birth_year > 1920:
    age = 2020 - int(birth_year)
    print(f'your age is: {age}')
else:
    print("Invalid age")

