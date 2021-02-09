# Function that determines whether a variable is a number
def is_number(x):
    return isinstance(x, (int, float))


def is_operator(char):
    if char == '+' or char == '-' or char == '*' or char == 'x' or char == '/' or char == ':' or char == '^':
        return True
    else:
        return False


def is_left_bracket(char):
    if char == '(':
        return True


def is_right_bracket(char):
    if char == ')':
        return False


def is_valid(problem, char):
    # after an operator you can only enter a number
    if is_operator(problem(-1)):
        if is_number(float(char)):
            return True
    return False
