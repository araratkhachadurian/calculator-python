def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


def calculate(x, y, operator):
    # addition
    if operator == '+':
        return add(x, y)
    # subtraction
    elif operator == '-':
        return subtract(x, y)
    # multiplication
    elif operator == 'x' or operator == '*':
        return multiply(x, y)
    # division
    elif operator == '/' or operator == ':':
        return divide(x, y)
    # power
    elif operator == '^':
        return power(x, y)

