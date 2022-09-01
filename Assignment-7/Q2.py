"""
Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
"""
print("=========================")
print("       Calculater        ")
print("=========================")
print("   1. For Additions      ")
print("   2. For Substraction   ")
print("   3. For Multiplication ")
print("   4. For Division       ")
print("=========================")
c = int(input("Enter Your Choice : "))
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
match c :
    case 1 :
        print("Sum = %d" %(num1+num2))
    case 2 :
        print("Sub = %d" %(num1- num2 if num1 > num2 else num2 - num1))
    case 3 :
        print("Mul = %d" %(num1 * num2))
    case 4 :
        print("Div = %d" %(num1 / num2 if num1 > num2 else num2 / num1))
    case _ :
        print("Wrong Options")