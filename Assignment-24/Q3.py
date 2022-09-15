"""
Write a python program to create 2 objects of the user class and assign different
values.
"""


# create class
class Laptop:
    pass


# create object
obj1 = Laptop()
obj2 = Laptop()

# set different values in different object
obj1.RAM = "4 GB"
obj1.CPU = 'i7'

obj2.RAM = '8 GB'
obj2.CPU = 'i9'

print(obj1.RAM, ":", obj1.CPU)
print(obj2.RAM, ":", obj2.CPU)
