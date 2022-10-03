# import thread module
from threading import Thread
from time import sleep


# ctreate list
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l2 = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]


# create disp() function
def disp(list):
    for e in list:
        print(e)
        sleep(1)


# create thread object
t1 = Thread(target=disp, args=(l1,))
t2 = Thread(target=disp, args=(l2,))


# thread start using start attribut of thread
t1.start()
t2.start()
