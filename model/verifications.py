# Function that determines whether a variable is a number
def is_digit(char):
    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' \
            or char == '7' or char == '8' or char == '9':
        return True


def is_float(char):
    try:
        float(char)
        return True
    except ValueError:
        return False


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
        return True


# does not yet accept brackets
def is_valid(problem, char):
    # check if entered character is a possible option
    if not is_valid_character(char):
        print("error: invalid character")
        return False
    # check if entered character is a possible starting character
    if (not problem) and (not is_valid_start(char)):
        print("error: invalid starting character")
        return False
    # after an operator you can only enter a number
    if is_operator(problem[-1]):
        if char.isdigit():
            return True
        else:
            print("error: operator after operator")
            return False
    return True


def is_valid_character(char):
    # digits 0 to 9
    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' \
            or char == '7' or char == '8' or char == '9':
        return True
    # operators +, -, *, /, ^, (, )
    if char == '+' or char == '-' or char == '*' or char == '/' or char == '^' or char == '(' or char == ')' \
            or char == '.':
        return True
    return False


def is_valid_start(char):
    # digits 0 to 9
    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' \
            or char == '7' or char == '8' or char == '9':
        return True
    # operators -, (
    if char == '-' or char == '(':
        return True
    return False
