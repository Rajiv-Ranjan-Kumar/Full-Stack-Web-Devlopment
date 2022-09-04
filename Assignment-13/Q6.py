"""Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
"""
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]

#secondlist = secondlist + firstlist

for i in firstlist:
    secondlist.append(i)
print(secondlist)