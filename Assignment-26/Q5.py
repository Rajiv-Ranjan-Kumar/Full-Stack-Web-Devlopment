"""Write a python script to create 2 threads to add all the values from 1 to 100"""
# import thread module
from threading import Thread, current_thread


# create class
class Add:
    total_sum = 0  # create class variable

    # create sum() method
    def sum(self, num1, num2):
        sum = 0
        for i in range(num1, num2):
            sum = sum + i
        Add.total_sum = Add.total_sum + sum
        print(current_thread().name, " = ", sum)

    # create class method
    @classmethod
    def disp(cls):
        print("Total Sum = ", cls.total_sum)


# create class object
obj = Add()

# create thread object
t1 = Thread(target=obj.sum, args=(1, 50))
t2 = Thread(target=obj.sum, args=(50, 101))

# start thread
t1.start()
t2.start()

# call class method
Add.disp()
