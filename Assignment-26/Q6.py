""" Write a python script to create 5 threads to fill a list with random numbers till 100."""

# import thread module
from threading import Thread


# create class
class StoreRandomNumber:
    # create class Variable
    list = list()

    # create store()method
    def store(self, num1, num2):
        for i in range(num1, num2):
            StoreRandomNumber.list.append(i)

    # create class method
    @classmethod
    def disp(cls):
        print(cls.list)


# create class object
srn = StoreRandomNumber()

# create thread object
t1 = Thread(target=srn.store, args=(1, 10))
t2 = Thread(target=srn.store, args=(10, 40))
t3 = Thread(target=srn.store, args=(40, 65))
t4 = Thread(target=srn.store, args=(65, 95))
t5 = Thread(target=srn.store, args=(95, 101))

# start thread
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# call class method
StoreRandomNumber.disp()
