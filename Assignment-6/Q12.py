"""
Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
"""
x = complex(input("Enter a Complex Number for Check Greater Number Real and Imaginary Part :"))
real = x.real
imag = x.imag
if real != imag :
    if real > imag :
        print("Real = ",real)
    else :
        print("Imag = ",imag)
else :
    print("Both are Equal")