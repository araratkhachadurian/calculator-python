import model.operations as op
import model.verifications as ver


class Calculator:
    problem = []
    answer = 0

    def __init__(self):
        problem = []

    @staticmethod
    def request(self):
        entered_dot = False
        self.problem = []
        # request valid input characters until '=' is entered
        while 1:
            char = input("enter a character: ")
            if char == '=':
                self.calculate(self)
            # keep track of dot added to make sure no more than 1 dot can be in a number
            if self.problem:
                if self.problem[-1].isdigit() and char == '.' and not entered_dot:
                    self.problem.append(char)
                    entered_dot = True
            # cannot enter another '.' if one has been entered to a digit
            if not entered_dot or ((not char == '.') and entered_dot):
                if char.isdigit():
                    self.problem.append(char)
                elif ver.is_valid(self.problem, char):
                    self.problem.append(char)
                    entered_dot = False
            print(self.problem)

    # method which calculates a mathematically valid problem according to the following steps
    # 1 - sort problem according to mathematical priority
    # 2 - solve problem chronologically
    @staticmethod
    def calculate(self):
        problem = self.reformat_digits(self)
        print(problem)
        if problem[1] == "+":
            self.answer = problem[0] + problem[2]
        elif problem[1] == "-":
            self.answer = problem[0] - problem[2]
        elif problem[1] == "*":
            self.answer = problem[0] * problem[2]
        elif problem[1] == "/":
            self.answer = problem[0] / problem[2]
        elif problem[1] == "^":
            self.answer = pow(problem[0], problem[2])
        print(problem, "=", self.answer)
        # clear problem
        self.problem = []

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
