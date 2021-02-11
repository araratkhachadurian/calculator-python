import model.calculator as calc


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    calculator = calc.Calculator()

    while 1:
        calculator.request(calculator)
        calculator.calculate(calculator)
