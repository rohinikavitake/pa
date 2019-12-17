import json
#converting json into python
x='{"name":"Johan","age":30,"city":"Newyork"}'
y = json.loads(x)
print(y["age"])
print(y["city"])
print(y["name"])

#converting pythonto json data
x={"name":"Johan","age":30,"city":"Newyork"}
y = json.dumps(x)
print(y)