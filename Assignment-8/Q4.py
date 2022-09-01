#Write a python script to print first 10 odd natural numbers
c = 1
i = 1
while c <= 10 :
    if i % 2 != 0 :
        print(i)
        c += 1
    i += 1