# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
try:
    print(x)
except NameError: # if you know the exception you can use this #optional
    print("NameError Exception ocurred") #optional
except:  #default
    print("An Exception occurred")
else: #if not exception occurs
    print("Nothing went wrong")
finally: #The finally block, if specified, will be executed regardless if the try block raises an error or not.
    print("I will run even if exception happens or not")

#Exception Raising- 
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero") #Raise an error and stop the program if x is lower than 0: