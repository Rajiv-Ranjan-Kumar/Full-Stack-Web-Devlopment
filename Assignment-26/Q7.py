"""Write a python script to create a clock where 1st thread will print the current time
every second and 2nd will print “1 Minute Completed” after every 1 minute.
"""
# import thrad and time module
from threading import Thread
from time import sleep, time, ctime, localtime


# create class
class Clock:
    current_sec = 1
    # create showTime()method

    def showTime(self):
        while True:
            current_time = localtime()
            sleep(1)
            Clock.current_sec = current_time.tm_sec
            print(current_time.tm_hour, current_time.tm_min,
                  current_time.tm_sec, sep=":")

    # create showMinuteMessage()method
    def showMinuteMessage(self):
        while True:
            if Clock.current_sec == 0:
                print("1 Minute complited")
                sleep(60)


t = Clock()
t1 = Thread(target=t.showTime,)
t2 = Thread(target=t.showMinuteMessage,)
t1.start()
t2.start()
