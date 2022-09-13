# Use iter and next method to access all the elements of a given set using while loop
l = [2,4,6,10,12,14,16,18,20] #list

# iter function
it = iter(l)

#use While Loop
while True:
    try:
        print(next(it)) #use next function
    except:
        break