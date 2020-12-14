#setting default parameter is not passed from function call.
def my_country(country = "India"):
    print("Hey you are from " + country)

my_country()
my_country("Sweden")


#Passing entire list as arguements, fruits is passed as food variable in function
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
my_function(fruits)

# Function definitions cannot be empty, but if you for some reason have a function definition with no content, 
# put in the pass statement to avoid getting an error.
def myfunction():
  pass

