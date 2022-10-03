# import thrad modul
from threading import Thread, current_thread

# using Name attribut
print("Current Thread Name Is : ", current_thread().name)

# using getName() method
print("Current Thread Name Is : ", current_thread().getName())
