"""Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)"""

#given tuple
tuple1 = (11, [22, 33], 44, 55)
#print Original tuple
print("Given Tuple:")
print(tuple1)
#find the index of 22 and change the value of 22 into 222
for e in tuple1:
    if type(e) != int:
        for i in range(len(e)):
            if e[i] == 22:
                e[i] = 222
#output
print("Modified Tuple")
print(tuple1)