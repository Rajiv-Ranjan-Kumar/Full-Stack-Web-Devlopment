"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""

num = eval(input("Enter a Number : "))
match num :
    case num if num == 0 :
        print("Number Is Zero")
    case num if num > 0 :
        print("Number is Posetive")
    case num if num < 0 :
        print("Number is Nigetive")
    case _ :
        print("Please Enter Valid Number")