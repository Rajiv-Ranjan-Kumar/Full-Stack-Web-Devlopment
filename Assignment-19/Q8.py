# Write a python program to multiply all the numbers in a list.
def multiplyOfListElements(list):
    mul = 1
    for i in list :
        mul = mul * i
    return mul

m = multiplyOfListElements([10,20,30,15,40,50])
print("Sum of List Elements = ", m)