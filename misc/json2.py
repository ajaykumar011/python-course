# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

#Convert from Python to JSON
import json

# a python object (dict):

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Python Dictionary String\n------------------------")
print(x)
# Convert into Json via Dump
y = json.dumps(x)

#the result is a JSON String
print("\nJSON String\n--------------------------")
print(y)


