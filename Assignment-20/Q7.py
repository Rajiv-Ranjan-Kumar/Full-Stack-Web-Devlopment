#Write a python program to access a function inside a function
def disp(i):
    print("Hello...")
    if i > 0:
        disp(i-1)
    else:
        exit

disp(5)