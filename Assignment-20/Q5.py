"""Write a python program to create a function to find the Min of three numbers.
"""
def min_number(num1,num2,num3):
    t = (num1,num2,num3)
    return min(t)

print("Enter Three Number : ")
print("Min Number = ",min_number(int(input()),int(input()),int(input())))