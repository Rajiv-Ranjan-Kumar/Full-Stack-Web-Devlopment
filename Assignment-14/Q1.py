#Write a Python script to create a list of first N natural numbers.
num = int(input("Enter a Number : "))
list = []
for i in range(1,num+1):
    list.append(i)
print(list)