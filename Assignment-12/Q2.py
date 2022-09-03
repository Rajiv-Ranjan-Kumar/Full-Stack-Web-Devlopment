#Write a python script to check whether a given number is Prime or not
num = int(input("Enter the Number : "))
i = 2
while i < num :
    if num % i == 0 :
        print("Not Prime Number")
        break
    i += 1
else :
    if num == 0 or num == 1 :
        print("Not Prime Number")
    else :
        print("Prime number")
