#Write a Python script to remove all non int values from a list.
list = [10,20,"Rajiv",12.35,True,5+8j,30,45,50]
for y in range(len(list)):
    for x in list:
        if type(x) != int:
            list.remove(x)
print(list)
