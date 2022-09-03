# Write a python script to calculate factorial of a given number
num = int(input("Enter a Number : "))
fact = num
while num != 1:
    fact = fact*(num - 1)
    num -= 1
print("factorial = ",fact)