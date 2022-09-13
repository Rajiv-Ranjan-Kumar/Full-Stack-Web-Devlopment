#Write a recursive python function to print octal of a given decimal number
def octal(num):
    if num == 0:
        return 0
    else:
        return num % 8 + 10 * octal(num // 8)
    
print(octal(int(input("Enter a Number : "))))