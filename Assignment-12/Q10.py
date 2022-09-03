# Write a python script to calculate HCF of two numbers
num1 = int(input("Enter 1'st Number : "))
num2 = int(input("Enter 2'nd Number : "))
r = 1
if num1 < num2 :
    x = num1
    num1 = num2
    num2 = x
while r != 0 :
    r = num1 % num2
    if r > num2 :
        num1 = r
    else :
        num1 = num2
        num2 = r
print("HCF = ",num1)