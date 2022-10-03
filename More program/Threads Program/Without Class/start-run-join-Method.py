# import thread module
from threading import Thread


# create thread child class
class MyThread(Thread):

    # create run() Method
    def run(self):
        for i in range(10):
            print("My Thread....")


# create object
my = MyThread()
my.start()
my.join()  # use join method

for i in range(10):
    print("Main Thread....")
