# import thread modul
from threading import Thread


# create class
class Mythread(Thread):

    # create run() method
    def run(self):
        print("My Thread Class..")


# create object of My Thread Class
my = Mythread()

# start thread
my.start()
