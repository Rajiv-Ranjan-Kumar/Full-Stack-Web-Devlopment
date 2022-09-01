#Write a python script to swap data of two variables
num1 = int(input("Enter First Number For Swaping : "))
num2 = int(input("Enter Second Number For Swaping : "))
print("Without Swaping")
print("Num1 = %d And Num2 = %d" %(num1,num2))
num1 += num2
num2 = num1 - num2
num1 = num1 - num2
print("After Swaping")
print("Num1 = %d And Num2 = %d" %(num1,num2))