# Write a python script to change the name of the Thread.
# import thread module
from threading import Thread, current_thread


# create class
class Mythread(Thread):
    # create getName()method
    def getName(self, str):
        print("{} Thread Name : " .format(str), current_thread().name)

    # create setName()method
    def setName(self, str):
        current_thread().name = str

    # create run metthod()
    def run(self):
        self.getName('Default')
        self.setName('Rajiv Thread')
        self.getName('Changed')


# create class object
obj = Mythread()

# start thread
obj.start()
