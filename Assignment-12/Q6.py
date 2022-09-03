#Write a python script to print first N prime numbers
num = int(input("Enter a Number : "))
if num == 0 or num == 1:
    print("not found prime number")
else :
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=" ")