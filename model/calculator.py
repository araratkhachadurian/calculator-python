import model.operations as op
import model.verifications as ver


class Calculator:
    problem = 'test'
    answer = 0

    def __init__(self):
        problem = 'test'

    @staticmethod
    def request(self):
        self.problem = []
        # request valid input characters until '=' is entered
        while 1:
            char = input("Enter a character: ")
            if char == '=':
                self.calculate(self)
            # first character must be a digit
            if (not self.problem) and char.isdigit():
                self.problem.append(char)
            # next characters must be mathematically valid
            elif self.problem and ver.is_valid(self.problem, char):
                self.problem.append(char)
            else:
                print("Try again")
            print(self.problem)

    # method which calculates a mathematically valid problem according to the following steps
    # 1 - sort problem according to mathematical priority
    # 2 - solve problem chronologically
    @staticmethod
    def calculate(self):
        problem = self.reformat_digits(self)
        print(problem)
        # clear problem
        self.problem = []
        # save answer (after calculation)

    # reformat problem by converting consecutive digit characters into one float number
    # example: '1' '1' '2' '+' '3' '4' '5' '6' -> '112' '+' '3456'
    @staticmethod
    def reformat_digits(self):
        # convert consecutive digits into one number
        # example: '1' '1' '2' '+' '3' '4' '5' '6' -> '112' '+' '3456'
        sorted_problem = []
        i = 0
        while i < len(self.problem):
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
