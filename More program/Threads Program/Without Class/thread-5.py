# import thread module
from threading import Thread
from time import sleep


# create getDetail function
def getDetail():
    for i in range(2):
        name = input("Enter Your Name : ")
        age = int(input("Enter your Age :"))

        if age >= 18:
            print("Your Age is Comlited for Voting..")
        else:
            print("Your Age is not Comlited for Voting..")


# create Thread Object
t1 = Thread(target=getDetail)
t2 = Thread(target=getDetail)

# start thread
t1.start()
t2.start()
