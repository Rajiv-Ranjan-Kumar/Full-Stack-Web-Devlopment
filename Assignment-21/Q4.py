#Write a recursive python function to print first N odd natural numbers in reverse order
def oddReverceNo(num):
    if num < 0:
        return 1
    else:
        if num % 2 != 0 :
            print(num)
    oddReverceNo(num-1)

oddReverceNo(int(input("Enter a Number : ")))