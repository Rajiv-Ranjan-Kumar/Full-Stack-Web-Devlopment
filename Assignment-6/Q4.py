"""
Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same.
"""
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
if num1 > num2 :
    print(num1," Is Greater")
elif num1 < num2 :
    print(num2," Is Greater")
else :
    print(num1,",",num2," Both Are Same")