#Write a python script to print first N even natural numbers
num = int(input("Enter Number of Term : "))
i = 1
while i <= num :
    if i % 2 == 0 :
        print(i)
    i += 1