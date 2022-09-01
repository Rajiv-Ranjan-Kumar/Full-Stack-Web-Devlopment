"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
"""
num = int(input("Enter a Number : "))
match num :
    case num if num % 2 == 0 :
        print("Sourav Shukla")
    case num if num % 2 != 0 and num < 0 :
        print("print Prateek Jai")
    case num if num % 2 != 0 :
        print("Aditya Choudhary")
    case _ :
        print("Thank you")