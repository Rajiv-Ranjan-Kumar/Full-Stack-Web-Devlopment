#Write a python script to print first N terms of a Fibonacci series
from re import A


num = int(input("Enter a Number : "))
a = -1
b = 1
c = 0
for i in range(num):
    c = a + b
    print(c , end=" ")
    a = b
    b = c