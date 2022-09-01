#Write a python script to print first N odd natural numbers
num = int(input("Enter Number Of Term : "))
i = 1
while i <= num :
    if i % 2 != 0:
        print(i)
    i += 1