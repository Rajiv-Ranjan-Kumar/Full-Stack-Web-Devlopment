"""Write a python script to create a calculator with 4 basic operations, and handle a
maximum number of exceptions."""


# create class
class Calculater:
    # create inputNumber() method
    def inputNumber(self):
        num1 = num2 = choice = 0
        try:
            num1 = int(input("\t\tEnter 1'st Number : "))
            num2 = int(input("\t\tEnter 2'nd Number : "))
            choice = int(input("\t\tEnter Your Choice : "))
        except ValueError:
            print("\t\t\tPlease Enter Only Number")
            self.inputNumber()
        return (num1, num2, choice)

    # create calculater() method
    def calculater(self, choice, num1, num2):
        match choice:
            case 1:
                print("\t\tSum = ", num1+num2)
            case 2:
                print("\t\tSub = ", num1-num2)
            case 3:
                print("\t\tMul = ", num1*num2)
            case 4:
                try:
                    print("\t\tDiv = ", num1/num2)
                except ZeroDivisionError:
                    print("\t\t\tDivision is Not Posible")
            case 5:
                try:
                    print("\t\tRemender = ", num1 % num2)
                except ArithmeticError:
                    print("\t\t\tRmender Calculation Not Posible")
            case 6:
                print("\t\t(Num1)^num2 = ", num1**num2)
            case _:
                print("\t\tWrong Choice")

    # create Disp() Method
    def disp(self):
        print("\t\t ----------------------------")
        print("\t\t|         Calculater         |")
        print("\t\t ----------------------------")
        print("\t\t 1. for Addition.")
        print("\t\t 2. for Substraction.")
        print("\t\t 3. for Multiplication.")
        print("\t\t 4. for Divistion.")
        print("\t\t 5. for find Remender.")
        print("\t\t 6. for find Number1^Number.")
        print("\t\t------------------------------")


# create object
obj = Calculater()
obj.disp()
num1, num2, choice = obj.inputNumber()
obj.calculater(choice, num1, num2)
input("\t\tExit for Press Enter")
