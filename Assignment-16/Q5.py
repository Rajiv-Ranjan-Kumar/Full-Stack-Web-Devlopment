#Write a python program to check if all items in the tuple are the same
t1 = (10,10,10,10)
i = 1
while i < len(t1):
    print(t1[0] is t1[i])
    i += 1