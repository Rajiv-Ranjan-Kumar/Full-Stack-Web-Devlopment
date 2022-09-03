#Write a python script to calculate sum of cubes of first N natural numbers
num = int(input("Enter a number : "))
sum = 0
for i in range(num):
    sum = sum +((i+1)**3)
print("Sum of cubes = ",sum)