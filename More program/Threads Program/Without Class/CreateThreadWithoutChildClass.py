# import thread module
from threading import Thread


# create class
class HelloHii:

    # create hello() method
    def hello(self, str):
        print("hello.... ", str)

    # create hii() method
    def hii(self, str):
        print("Hiii.... ", str)


# create object
h1 = HelloHii()

# create thread
t1 = Thread(target=h1.hello, args=('Rajiv..',))
t2 = Thread(target=h1.hii, args=('Supriya..',))

# start thread
t1.start()
t2.start()
