"""Write a python script to create a Phone class with 2 methods to print the features
(calling and sms).
"""


# create class Phone
class Phone:
    # create calling instance method
    def calling(self):
        print("Calling.....")

    # create sms instance method
    def sms(self):
        print("send sms...")


# create object of Phone class
p = Phone()
p.calling()
p.sms()
