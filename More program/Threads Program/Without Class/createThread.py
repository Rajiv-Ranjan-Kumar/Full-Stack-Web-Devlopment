# import thread modul
from threading import Thread

# create function


def disp():
    for i in range(10):
        print("Thread Start....")


# create thread object
t = Thread(target=disp)

# start thread using start() attributs of Thread class
t.start()
