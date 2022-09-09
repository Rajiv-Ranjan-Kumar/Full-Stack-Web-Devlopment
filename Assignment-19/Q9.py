"""Write a python program to create a function to check whether a number falls in a
given range."""

def check_range(num , ran):
    print(num in range(ran+1))

check_range(int(input("Enter a Number : ")),int(input("Enter Range : ")))