import requests

def function():
    pass
class Class1:
    pass
ob = requests
ob2 = function
ob3 = Class1

print(ob.__name__)
print(requests.__name__)
print(function.__name__)
print(ob2.__name__)
print(ob3.__name__)
print(Class1.__name__)
print(__name__)

mylist = []
for method in dir(mylist):
    print(f"\n{method}")
print(type(1))
print(type("text"))
print(type(mylist))
print(type(method))