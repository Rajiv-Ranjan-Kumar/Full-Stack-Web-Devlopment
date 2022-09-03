#Write a python script to calculate sum of first N even natural numbers
num = int(input("Enter a Number : "))
sum = 0
for i in range(num):
    if (i+1) % 2 == 0:
        sum = sum + (i+1)
print("Sum of All Even Numbers = ", sum)