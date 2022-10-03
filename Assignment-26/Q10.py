"""Write a python script to check whether a given number is prime or armstrong number
using 2 different threads"""

# import thread module
from threading import Thread


# create class
class CheckPrimeOrArmstrong:
    # create prime() method
    def prime(self, num):
        for i in range(2, num):
            if num % i == 0:
                print("%d Is Not Prime Number" % num)
                break
        else:
            print("%d Is Prime Number" % num)

    # create armstrong() method
    def armstrong(self, num):
        count_digit = len(str(num))
        sum = 0
        for i in str(num):
            sum = sum + int(i)**count_digit
        if num == sum:
            print("%d Is Armstrong" % num)
        else:
            print("%d Is Not Armstrong" % num)


# create class object
obj = CheckPrimeOrArmstrong()

# create threads
t1 = Thread(target=obj.prime, args=(11,))
t2 = Thread(target=obj.armstrong, args=(11,))

# start thread
t1.start()
t2.start()
