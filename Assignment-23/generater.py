from ast import Yield


def generater():#generater
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

it = generater()#generater/iterater object

#use next function for display data
"""print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))"""

#use for loop to display data
for e in generater():
    print(e)