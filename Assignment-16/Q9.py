#Write a python program to print the value 20 from given nested tuple
#tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

#Given tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
#find the value 20 in given nested tuple and print it
for e in tuple1:
    for i in range(len(e)):
        if e[i] == 20:
            print(e[i])