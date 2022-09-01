#Write a python script to check whether a given number is a three digit number or not.
num = int(input("Enter a Number for Check Number is Three Digit or not : "))
c = 0
if num != 0 :
    num = int(num / 10)
    c += 1
if num != 0 :
    c += 1
    num = int(num / 10)
if num != 0 :
    c += 1
    num = int(num / 10)
print("Given Number Has Three Digit" if num == 0 and c == 3 else "Given Number Has not Three Digit")
