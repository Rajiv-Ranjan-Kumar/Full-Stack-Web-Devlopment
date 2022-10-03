# import thread module
from threading import Thread


# create Thread Child Class
class MyThread(Thread):

    # create constructor
    def __init__(self):
        Thread.__init__(self)
        print("Child Thread Constructor")


# create object
my = MyThread()
my.start()
