"""Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides."""


# Decorator Function
def validity_triangle(perimeter_func):
    def check(a, b, c):
        if a == b+c or b == (a+c) or c == a+b:
            print("Valide Triangle")
            perimeter_func(a, b, c)
        else:
            print("Invalide Triangle")
    return check


# Normal Function
@validity_triangle
def perimeter(a, b, c):
    print("Perimeter = ", a+b+c)


# Input Sides
print("Enter Sides of Triangle : ")
x, y, z = int(input()), int(input()), int(input())
perimeter(x, y, z)
