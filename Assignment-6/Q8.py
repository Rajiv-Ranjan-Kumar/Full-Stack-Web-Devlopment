"""Write a python script to check whether a given quadratic equation has two real &
    distinct roots, real & equal roots or imaginary roots"""
a = int(input("Enter Operant of X^2 with Sign: "))
b = int(input("Enter Operant of X with Sign: "))
c = int(input("Enter Constant with Sign: "))
d = b*b - (4*a*c)
if d > 0 :
    print("Real and Distinct Roots")
elif d == 0 :
    print("Real and Equal Roots")
else :
    print("Imaginary Root")