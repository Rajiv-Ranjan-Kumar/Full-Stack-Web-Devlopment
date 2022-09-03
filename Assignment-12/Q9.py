# Write a python script to calculate LCM of two numbers
num1 = int(input("Enter 1'st Number : "))
num2 = int(input("Enter 2'nd Number : "))
lcm = 1
i = 2
while i <= num1 or i <= num2:
    if num1 % i == 0 and num2 % i == 0 :
        lcm = lcm * i
        num1 = int(num1 / i)
        num2 = int(num2 / i)
    elif num1 % i == 0 :
        lcm = lcm * i
        num1 = int(num1 / i)
    elif num2 % i == 0 :
        lcm = lcm * i
        num2 = int(num2 / i)
    else:
        i += 1
print("LCM = ",lcm)