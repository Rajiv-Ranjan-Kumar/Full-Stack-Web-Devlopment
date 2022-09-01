#Write a python script to display the number of days in a given month number
x = int(input("Enter Month Number : "))
match x :
    case 1 :
        print("31 Day's")
    case 2 :
        print("28 or 29 Day's")
    case 3 :
        print("31 Day's")
    case 4 :
        print("30 Day's")
    case 5 :
        print("31 Day's")
    case 6 :
        print("30 Day's")
    case 7 :
        print("31 Day's")
    case 8 :
        print("31 Day's")
    case 9 :
        print("30 Day's")
    case 10 :
        print("31 Day's")
    case 11 :
        print("30 Day's")
    case 12 :
        print("31 Day's")
    case _ :
        print("Envalid Day's Number")