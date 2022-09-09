# Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}
from ctypes import Union


s1 = {"Java", "Python", "SQL"}
s2 = {"C", "Cpp", "NoSQL"}
s2 = s2.union(s1)
print(s2)