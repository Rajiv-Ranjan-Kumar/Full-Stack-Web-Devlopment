#Write a python script to check whether a given pair of numbers are co-Prime
#numbers or not.
num1 = int(input("Enter 1'st Number : "))
num2 = int(input("Enter 2'nd Number : "))
if num1 > num2:
    x = num1
else :
    x = num2

for i in range(2,x):
    if num1 % i == 0 and num2 % i == 0:
        print("Not Co-Prime Number")
        break
else :
    if num1 == 0 and num2 == 1 or num1 == 1 and num2 == 0:
        print("Not Co-Prime Number")
    else:
        print("Co-Prime Number")