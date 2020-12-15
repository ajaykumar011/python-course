# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

#Convert JSON to Python

import json
#some Json
x = '{"Name":"Ajay", "Age":40, "City":"Delhi"}'

#parse x
y = json.loads(x)

#the result is a Python dictionary
print(y)
print(y["Age"])
print(y.get("Age"))

for x in y.values():
    print(x)
for y in y.keys():
    print(y)


