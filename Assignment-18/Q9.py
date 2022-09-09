"""Write a python program to merge two python dictionaries into one dictionary."""
d1 = {10:'A',20:'B'}
d2 = {30:'C',40:'D'}
d2.update(d1)
print(d2)