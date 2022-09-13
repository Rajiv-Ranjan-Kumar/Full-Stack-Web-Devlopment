# Write a recursive python function to print first N odd natural numbers
def oddNumber(num):
    if num > 0:
        oddNumber(num - 1)
        if num % 2 != 0:
            print(num)

oddNumber(int(input("Enter a Number : ")))