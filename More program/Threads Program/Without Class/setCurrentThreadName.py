# import thread module
from threading import Thread, current_thread

# using name attribut
print("Default Thread Name : ", current_thread().name)

current_thread().name = "Rajiv Thread"

print("Set Thread Name : ", current_thread().name)

print()

# using detName() method
print("Default Thread Name : ", current_thread().name)

current_thread().setName("Rajiv Singh Thread")

print("Default Thread Name : ", current_thread().name)
