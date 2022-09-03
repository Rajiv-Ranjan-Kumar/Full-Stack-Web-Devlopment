#Write a python script to calculate sum of digits of a given number
num = int(input("Enter a number : "))
sum = 0
while num != 0:
    sum = sum + (num % 10)
    num = int(num / 10)
print("Sum of Total Digit = " , sum)