def calculator():
    if choose == 5:
        quit() #Exit Program
    elif choose >=6 or choose <= 0:
        print("\nOops! There not an option with this number to select.\n  ")
        return #Finish Function
    number1 = float(input("\nInsert the First Number: "))
    number2 = float(input("Insert the Second Number: "))
    if choose == 1:
        if number1 == 0 or number2 == 0:
            print("\nIf you add 0 you will receive the same value that you had get before.\n")
            return
        resultado = number1+number2
        print("\n{:.2f} + {:.2f} = {:.2f}\n".format(number1, number2, resultado))
    elif choose == 2:
        if number1 == 0 or number2 == 0:
            print("\nYou cant use 0 to subtraction method because there's no value to subtract.\n")
            return
        resultado = number1 - number2
        print("\n{:.2f} - {:.2f} = {:.2f}\n".format(number1, number2, resultado))
    elif choose == 3:
        if number1 == 0 or number2 == 0:
            print("\nEvery multiply to 0 is equal to 0.\n")
            return
        resultado = number1 * number2
        print("\n{:.2f} * {:.2f} = {:.2f}\n".format(number1, number2, resultado))
    elif choose == 4:
        if number1 == 0 or number2 == 0:
            print("\nYou cant use 0 to division method because it will return the same number.\n")
            return
        resultado = number1 / number2
        print("\n{:.2f} / {:.2f} = {:.2f}\n".format(number1, number2, resultado))
active = True
while active == True:
    print("What is Your Choose?"
          "\n1 - Addition"
          "\n2 - Subtraction"
          "\n3 - Multiplication"
          "\n4 - Division"
          "\n5 - Exit")
    choose = int(input("\n"))
    calculator()