"""
Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""
print("   1. For Check isosceles triangle or not")
print("   2. For Check right angled triangle or not")
print("   3. For Check equilateral triangle or not")
print("   4. For Exit")
print("")
c = int(input("Enter Your Choice : "))
l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
h = int(input("Enter Height : "))
match c :
    case 1 :
        if l == b or b == h or l == h :
            print("Isosceles Triangle")
        else :
            print("Not Isosceles Triangle")
    case 2 :
        if l == b + h or b == l + h or h == l + b :
            print("Right Angled Triangle")
        else :
            print("Not Right Angle Triangle")
    case 3 :
        if l == b == h :
            print("Equilateral Triangle")
        else :
            print("Not Equilateral Triangle")
    case 4 :
        print("Thank You...")
        exit
    case _ :
        print("Wrong Options")