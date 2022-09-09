"""Write a python program to create a function to check whether a given number is even
or odd"""
def check_even_or_odd(num):
    print("Even Number" if num % 2 == 0 else "Odd Number")

check_even_or_odd(int(input("Enter a Number : ")))