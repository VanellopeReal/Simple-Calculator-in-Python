def calculator():
    if choose == 5:
        quit() #Exit Program
    else:
        print("\nOops! There not an option with this number to select.\n  ")
        return #Finish Function
    number1 = float(input("\nInsert the First Number: "))
    number2 = float(input("Insert the Second Number: "))
    if choose == 1:
        resultado = number1+number2
        print("\n{:.2f} + {:.2f} = {:.2f}\n".format(number1, number2, resultado))
    elif choose == 2:
        resultado = number1 - number2
        print("\n{:.2f} - {:.2f} = {:.2f}\n".format(number1, number2, resultado))
    elif choose == 3:
        resultado = number1 * number2
        print("\n{:.2f} * {:.2f} = {:.2f}\n".format(number1, number2, resultado))
    elif choose == 4:
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