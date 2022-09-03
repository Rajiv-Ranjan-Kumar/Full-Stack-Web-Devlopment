#Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
num = int(input("Enter a number : "))
bin = 0
r = 0
c = 0
while num != 0:
    bin = bin * 10 + (num % 2)
    c += 1
    num = int(num/2)

while bin > 0 :
    r = r * 10 + (bin % 10)
    c -= 1
    bin = int(bin / 10)

if c == 0 :
    print("Binary = ", r)
else :
    for i in range(c) :
        r = r * 10
    print("Binary = ", r)