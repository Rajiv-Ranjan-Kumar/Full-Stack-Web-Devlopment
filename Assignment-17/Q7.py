"""Write a python program to remove last item of the given set
thisset = {"Python", "Django", "JavaScript", “SQL”}
"""
thisset = {"Python", "Django", "JavaScript", "SQL"}
print(thisset)
x = ""
for e in thisset:
    x = e
thisset.remove(x)
print(thisset)