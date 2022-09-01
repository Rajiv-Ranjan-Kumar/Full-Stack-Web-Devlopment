""" Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""

color = input("What is Your Favorite Colour : ")
match color :
    case color if "yellow" in color or "Yellow" in color or "YELLOW" in color :
        print("Monday")
    case color if "blue" in color or "Blue" in color or "BLUE" in color :
        print("Tuesday")
    case color if "orange" in color or "Orange" in color or "ORANGE" in color :
        print("Wednesday")
    case color if "white" in color or "White" in color or "WHITE" in color :
        print("Thursday")
    case color if "black" in color or "Black" in color or "BLACK" in color :
        print("Friday")
    case color if "red" in color or "Red" in color or "RED" in color :
        print("Saturday")
    case _ :
        print("Sunday")