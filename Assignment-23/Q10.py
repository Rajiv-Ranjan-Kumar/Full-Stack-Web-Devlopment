# Define a function which calculates HCF of two numbers. Define and apply a
# decorator to check whether two given numbers are co-prime or not

# Decorator function
def co_prime(HCF_func):
    def check_coPrime(a, b):
        l1 = list()  # Empty list
        l2 = list()  # Empty list
        # collect factor
        for e in range(2, a):
            if a % e == 0:
                l1.append(e)
        for e in range(2, b):
            if b % e == 0:
                l2.append(e)

        x = len(l1) if l1 <= l2 else len(l2)
        # check co-prime
        for e in range(x):
            if l1[e] == l2[e]:
                print("Number %d and %d is not co-prime" % (a, b))
                break
        else:
            print("Number %d and %d is co-prime" % (a, b))
        HCF_func(a, b)
    return check_coPrime

# normal function


@co_prime
def HCF(a, b):
    r = 0
    if b > a:
        temp = a
        a = b
        b = temp
    while b > 0:
        r = a % b
        if r > b:
            a = r
        else:
            a = b
            b = r
    else:
        print("HCF = ", a)


print("Enter Two Number : ")
a, b = int(input()), int(input())
HCF(a, b)
