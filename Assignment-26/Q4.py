"""Write a python script to create two Threads. First thread will print all Even numbers
and Second thread will print all Odd numbers till 100.
"""

# import threade module
from threading import Thread


# create class
class EvenOddNumber:

    # create evenNumber()method
    def evenNumber(sefl):
        print("All Even Number 1 to 100 : ")
        for i in range(2, 101, 2):
            print(i, end=" ")

    # create oddNumber()method
    def oddNumber(sefl):
        print("\n\nAll Odd Number 1 to 100 : ")
        for i in range(1, 101, 2):
            print(i, end=" ")


# create class object
eon = EvenOddNumber()

# create thread object
t1 = Thread(target=eon.evenNumber)
t2 = Thread(target=eon.oddNumber)

# start thread
t1.start()
t2.start()
