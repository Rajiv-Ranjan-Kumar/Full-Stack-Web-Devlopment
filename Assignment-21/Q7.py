#Write a recursive python function to print squares of first N natural numbers
def squareNeturalNo(num):
    if num <= 0:
        return 1
    else:
        squareNeturalNo(num - 1)
        print("%d = %d" %(num,num ** 2))

squareNeturalNo(int(input("Enter a Number : ")))