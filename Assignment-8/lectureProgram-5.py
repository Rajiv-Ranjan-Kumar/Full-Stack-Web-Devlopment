'''write a program to ask user to enter an even number at most three times
if the user failed to enter an even number in all three chances then he has
lost the game. if user enter an even number, then no more chancege will be
given and announced him a winner.'''
i = 1
while i <= 3 :
    num = int(input("Enter a Even Number : "))
    if num % 2 == 0 :
        break
    i += 1
if num % 2 == 0 :
    print("You are winner...")
else :
    print("you are lost the game")