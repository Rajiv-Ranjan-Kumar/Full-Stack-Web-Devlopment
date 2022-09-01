#Write a python script to print first N even natural numbers in reverse order
num = int(input("Enter Number of Term : "))
i = 0
while i < num :
    if (num - i) % 2 == 0 :
        print(num-i)
    i += 1