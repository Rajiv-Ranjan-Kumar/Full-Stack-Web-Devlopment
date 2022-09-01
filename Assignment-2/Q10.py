"""
Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)
"""
from datetime import datetime
x = datetime.now()
print("Date :",end=" ")
print(x.day,x.month,x.year,sep='-')
print("Time :",end=" ")
print(x.hour,x.minute,sep=':',end="")
print("pm")