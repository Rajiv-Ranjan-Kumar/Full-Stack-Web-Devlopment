#Write a python script to calculate sum of first N natural numbers
num = int(input("Enter a Number : "))
sum = 0
while num != 0 :
    r = num % 10
    num = int(num / 10)
    sum = sum + r
print("Sum of All Digit = " ,sum)