"""
Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
"""
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Secon Number : "))
num3 = int(input("Enter Third Number : "))
if num1 > num2 and num1 > num3 :
    print(num1," Is a Grater")
elif num1 < num2 and num2 > num3 :
    print(num2," Is a Grater")
elif num1 < num3 and num2 < num3 :
    print(num3," Is a Grater")
else :
    print("All Are Equals")