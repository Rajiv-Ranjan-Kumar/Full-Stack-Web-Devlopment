# import thread module
from threading import Thread


# create sum() fumction
def sum(num1, num2):
    sum = 0
    for i in range(num1, num2):
        sum = sum + i
    print(sum)


# create thread object
t1 = Thread(target=sum, args=(1, 50))
t2 = Thread(target=sum, args=(50, 101))

# start thread using start attributs of thread
t1.start()
t2.start()
