import json

# Some Python dictionary converted to JSON:
x =  '{"name":"John", "age":30, "city":"New York"}'

# json object  to python  object 
y = json.loads(x)

# print(isinstance of json.dumps(y))

# python object to json  object 

w=json.dumps(y)


print(w)

# The result is a Python dictionary:
print(y["age"])


