"""Write a python script to join 2 threads after printing completing the first Question.
"""
# import thread module
from threading import Thread


# create class
class UseJoinThreadMethod:

    # create disp1() method
    def disp1(self):
        for i in range(20):
            print("Hii.....")

    # create disp2() method
    def disp2(self):
        for i in range(10):
            print("Hello....")


# create class object
obj = UseJoinThreadMethod()

# create thread object
t1 = Thread(target=obj.disp1)
t2 = Thread(target=obj.disp2)

# start thread
t1.start()
t1.join()  # use join method
t2.start()
