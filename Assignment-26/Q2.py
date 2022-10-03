"""Write a python script to create a user account class with 2 instance variables (userid
and balance). Create 3 user objects and add all the users using operator
overloading.
"""


class UserAccount:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.balance = balance

    def __add__(self, other):
        users = self.user_id + other.user_id
        total_balance = self.balance + other.balance
        return users, total_balance


ua1 = UserAccount('RA123', 12000)
ua2 = UserAccount('RA124', 15000)
ua3 = UserAccount('RA125', 18000)
ua1.user_id, ua1.balance = ua1+ua2
print(ua1 + ua3)
