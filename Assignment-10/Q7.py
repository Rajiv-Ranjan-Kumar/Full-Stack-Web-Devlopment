#Write a python script to print first N even natural numbers in reverse order
num = int(input("Enter a Number : "))
for i in range(num):
    if (num-i) % 2 == 0 :
        print(num-i)