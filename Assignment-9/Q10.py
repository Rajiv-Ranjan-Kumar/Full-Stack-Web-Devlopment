# Write a python script to print first 10 multiples of N
num = int(input("Enter a Number : "))
c = 1
i = 1
while c <= 10 :
    if i % num == 0 :
        print(i)
        c += 1
    i += 1