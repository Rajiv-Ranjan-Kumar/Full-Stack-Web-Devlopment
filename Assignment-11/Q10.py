# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

num = int(input("Enter Decimal Number : "))
c , r , octal = 0 , 0 , 0
if num < 8 :
    print("Octal Number = " , num)
else :
    while num > 0 :
        r = r * 10 + (num % 8)
        c += 1
        num = int(num / 8)

    while r > 0 :
        octal = octal * 10 + (r % 10)
        c -= 1
        r = int(r / 10)

    if c == 0:
        print("Octal Number = " , octal)
    else :
        for i in range(c):
            octal = octal * 10
        print("Octal Number = " , octal)