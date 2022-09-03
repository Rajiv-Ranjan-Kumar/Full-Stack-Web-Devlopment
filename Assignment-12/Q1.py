#Write a python script to reverse a number.
num = int(input("Enter the number : "))
rev = 0
while num > 0 :
    rev = rev * 10 + (num % 10)
    num = int(num / 10)
print("Reverce Number = ", rev)