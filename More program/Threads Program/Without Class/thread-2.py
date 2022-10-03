# import thread modul
from threading import Thread


# create hii() function
def hii():
    for i in range(10):
        print("Hiii...")


# create hello() function
def hello():
    for i in range(10):
        print("Hello.....")


# create thread object
t1 = Thread(target=hii)
t2 = Thread(target=hello)

# start thread using strat attributs o thread
t1.start()
t2.start()
