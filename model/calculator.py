import model.operations as op
import model.verifications as ver


class Calculator:
    problem = []
    answer = 0

    def __init__(self):
        problem = []

    @staticmethod
    def start(self):
        # boolean that answers whether a bracket is open
        bracket = False
        # boolean that answers whether a dot has been entered
        dot = False
        # problem list starts with 0
        self.problem = ['0']
        while 1:
            char = input("enter character: ")
            # start calculation after '=' is entered
            if char == '=' and not bracket and self.problem[-1] != '.':
                self.calculate2(self)
            # the first character must be a minus sign or a digit
            if self.problem[-1] == '0':
                if char == '(':
                    bracket = True
                    self.problem[-1] = char
                elif char == '-':
                    self.problem.append(char)
                elif ver.is_digit(char):
                    self.problem[-1] = char
            # next characters
            else:
                # if the entered character is a single digit
                if ver.is_digit(char):
                    # if the previous character is a float, combine character with it to form a single float
                    if ver.is_float(self.problem[-1]):
                        self.problem[-1] = self.problem[-1] + char
                    else:
                        self.problem.append(char)
                # if a dot is entered and the previous value is a float without a dot, add it
                if char == '.' and ver.is_float(self.problem[-1]) and not dot:
                    dot = True
                    self.problem.append(char)
                # if an opening bracket is entered, no is bracket open and the previous character is an operator, add it
                if char == '(' and ver.is_operator(self.problem[-1]) and not bracket:
                    bracket = True
                    self.problem.append(char)
                if char == ')' and ver.is_float(self.problem[-1]) and bracket:
                    bracket = False
                    self.problem.append(char)
                if ver.is_operator(char) and (ver.is_float(self.problem[-1]) or self.problem[-1] == ')'):
                    dot = False
                    self.problem.append(char)
            print(self.problem)


    @staticmethod
    def calculate(self):
        n = 0
        while n < len(self.problem)-2:
            if self.problem[n+1] == '.':
                x = self.problem[n]
                y = self.problem[n+2]
                self.problem[n] = float(x + '.' + y)
                del self.problem[n+1]
                del self.problem[n+1]
            n = n + 1
        while len(self.problem) != 1:
            if self.problem[1] == "+":
                self.problem[0] = float(self.problem[0]) + float(self.problem[2])
            elif self.problem[1] == "-":
                self.problem[0] = float(self.problem[0]) - float(self.problem[2])
            elif self.problem[1] == "*":
                self.problem[0] = float(self.problem[0]) * float(self.problem[2])
            elif self.problem[1] == "/":
                self.problem[0] = float(self.problem[0]) / float(self.problem[2])
            elif self.problem[1] == "^":
                self.problem[0] = pow(float(self.problem[0]), float(self.problem[2]))
            del self.problem[1]
            del self.problem[1]
        print(self.problem)
        self.problem = ['0']


    # reformat problem by converting consecutive digit characters into one float number
    # example: '1' '1' '2' '+' '3' '4' '5' '6' -> '112' '+' '3456'
    @staticmethod
    def reformat_digits(self):
        # convert consecutive digits into one number
        # example: '1' '1' '2' '+' '3' '4' '5' '6' -> '112' '+' '3456'
        sorted_problem = []
        i = 0
        while i < len(self.problem) - 1:
            # if the current character is a digit, convert consecutive digits into one number
            if self.problem[i].isdigit():
                n = i
                # temporary string to store consecutive digits
                temp = self.problem[n]
                # add consecutive digits to the string or a dot for decimals
                while self.problem[n + 1].isdigit() or self.problem[n + 1] == '.':
                    temp = temp + self.problem[n + 1]
                    n = n + 1
                    # if at the last digit, stop loop
                    if n == len(self.problem) - 1:
                        break
                sorted_problem.append(float(temp))
                # start from operator after the number
                i = n
            else:
                sorted_problem.append(self.problem[i])
            i = i + 1
        return sorted_problem
