import model.operations as op
import model.verifications as ver


# request method requests valid input characters or numbers until the '=' char is given
def request():
    problem = []
    char = 0
    # request valid input characters until '=' is entered
    while char != '=':
        char = input("Enter a character: ")
        # check if character is mathematically valid
        # add character to the problem if valid PROBLEM: how to see
        if ver.is_valid(problem, char):
            problem.append(char)
        else:
            print("Try again")
        print(problem)


class Calculator:
    problem = 'test'

    def __init__(self):
        problem = 'test'
