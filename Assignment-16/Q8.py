#Write a python program to Sort a tuple of tuples by the second item.
#tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29)

#tuple
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
#print actual tuple
print("Actual Tuple = ",tuple1)
#convert tuple into list
tuple1 = [list(e) for e in tuple1]
#sorting the list
key = tuple1[1] # key value
for e in tuple1:
    if key[1] > e[1]:
        if tuple1.index(e) > tuple1.index(key):
            i = 0
            while i < len(tuple1):
                if tuple1[i] == e:
                    temp = tuple1[i-1]
                    tuple1[i-1] = e
                    tuple1[i] = temp
                i += 1
#convert list into tuple using tuple function
tuple1 = [tuple(e) for e in tuple1]
tuple1 = tuple(tuple1)
#output
print("Sorted Tuple = ",tuple1)