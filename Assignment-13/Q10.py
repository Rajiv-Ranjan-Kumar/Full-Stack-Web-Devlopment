#Write a Python script to create a list, where each element of the list is a digit of a given number.
num = int(input("Enter a Number : "))
list = []
while num != 0:
    r = num % 10
    list.append(r)
    num = int(num / 10)
list.reverse()
print(list)