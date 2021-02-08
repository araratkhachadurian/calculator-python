# Function that determines whether a variable is a number
def isNumber(x):
    return isinstance(x, (int, float))


def isOperator(char):
    if char == '+' or char == '-' or char == '*' or char == 'x' or char == '/' or char == ':' or char == '^':
        return True
    else:
        return False
