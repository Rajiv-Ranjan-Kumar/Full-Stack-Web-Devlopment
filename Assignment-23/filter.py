l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def checkPrime(num):
    for e in range(2,num,1):
        if num % e != 0:
            return True
        return False

it = filter(checkPrime,l)
filterList = []

while True:
    try :
        filterList.append((next(it)))
    except StopIteration:
        break
print(filterList)