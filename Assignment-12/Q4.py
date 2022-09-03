#Write a python script to print all Prime numbers between two given numbers (both
#values inclusive)
num1 = int(input("Enter 1'st Number : "))
num2 = int(input("Enter 2'nd Number : "))
for i in range(num1 , num2+1):
    for j in range(2 , i):
        if i % j == 0 :
            break
    else :
        if i == 0 or i == 1:
            continue
        else :
            print(i , end=" ")