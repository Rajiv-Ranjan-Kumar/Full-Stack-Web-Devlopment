#Write a recursive python function to print cubes of first N natural numbers
def cubesNeturalNo(num):
    if num <= 0:
        return 1
    else:
        cubesNeturalNo(num - 1)
        print("%d = %d" %(num,num ** 3))

cubesNeturalNo(int(input("Enter a Number : ")))