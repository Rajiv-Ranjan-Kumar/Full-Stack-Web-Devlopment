#Write a Python script to print indices of all occurrences of a given element in a given list
list = [10,20,30,"Rajiv",True,12.60,5+6j]
for i in list:
    print(i,"\tIndex No. = ",list.index(i))