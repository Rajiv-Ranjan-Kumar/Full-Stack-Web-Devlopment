#Write a recursive python function to calculate sum of the digits of a given number
def sumOfDigit(num , sum = 0):
    if num == 0:
        return 0
    return num % 10 + sumOfDigit(num // 10)

print("Sum of Digit = ",sumOfDigit(int(input("Enter a Number : "))))