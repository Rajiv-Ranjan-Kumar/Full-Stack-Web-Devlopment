#Write a python script to calculate sum of squares of first N natural numbers
num = int(input("Enter a number : "))
sum = 0
for i in range(num):
    sum = sum + ((i+1)**2)
print(sum)