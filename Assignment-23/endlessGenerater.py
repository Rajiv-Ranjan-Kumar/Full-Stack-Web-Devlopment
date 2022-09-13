#we can create a generater object , which
#is capable of producing endless iterator.
def fibGenrater():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

it = fibGenrater()
l = list()
while True:
    choice = input("Do you want to continew (Y/N) : ")
    if choice in ('Y','y'):
        l.append(next(it))
    elif choice in ('N','n'):
        print(l)
        break
    else:
        print('Please Enter Y/N')