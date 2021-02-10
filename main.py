# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import model.verifications as ver
import model.operations as op
import model.calculator as calc


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    calculator = calc.Calculator()

    while 1:
        calculator.request(calculator)
        calculator.calculate(calculator)



    # valid = False
    # input
    #while not valid:
    #    # get the first number
    #    try:
    #        x = float(input("Enter a number: "))
    #    except ValueError:
    #        print("Input is invalid, please try again: ")
    #    # get the operator
    #    operator = input("Enter an operator: ")
    #    while not ver.is_operator(operator):
    #        print("Input is invalid, please try again: ")
    #        operator = input("Enter an operator: ")
    #    # get the second number
    #    try:
    #        y = float(input("Enter a number: "))
    #    except ValueError:
    #        print("Input is invalid, please try again: ")
    #    # obtained all variables successfully
    #    valid = True
    # calculation
    #z = op.calculate(x, y, operator)
    # output
    #print(x, operator, y, "=", z)

