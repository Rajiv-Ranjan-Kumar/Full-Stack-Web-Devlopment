#Write a python script to print first N odd natural numbers in reverse order
num = int(input("Enter a number : "))
for i in range(num):
    if (num-i) % 2 != 0 :
        print(num-i)