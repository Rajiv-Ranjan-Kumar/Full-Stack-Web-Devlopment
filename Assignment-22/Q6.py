#Write a recursive python function to calculate the factorial of a number.
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

print("Factorial = ",factorial(int(input("Enter a Number : "))))