#Write a python script to find next prime number of a given number
num = int(input("Enter the Number : "))
i = 2
if num == 0:
    num += 2
else :
    num += 1
while i < num :
    if num % i == 0 :
        num += 1
        continue
    else :
        i += 1
else :
    print("Next Prime Number = ",num)