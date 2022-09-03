#Write a python script to count digits in a given number
num = int(input("Enter a Number : "))
c = 0
while num != 0:
    num = int(num / 10)
    c += 1
print("Total Digit of Number = " , c)