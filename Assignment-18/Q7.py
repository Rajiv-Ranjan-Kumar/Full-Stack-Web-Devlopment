"""Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries."""
d1 = {10:'A',20:'B'}
d2 = {30:'C',40:'D'}
d3 = {50:'E',60:'F'}
d4 = dict(d1=d1,d2=d2,d3=d3)
print(d4)