#Write a recursive python function to print binary of a given decimal number.
def binary(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * binary(num // 2)
    
print(binary(int(input("Enter a Number : "))))