# Component 4
# compare user input for answer and actual answer
# give appropriate feedback based on input

import random

# Number checking function:


def int_check(question, low=None, high=None):
    # error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)

    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not low
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# adds questions to incorrect and correct lists to be displayed later
incorrect_answer = []
correct_answer = []

# Main routine
lowest = int_check("What is the lowest number you would like to use? ")
highest = int_check("What is the highest number you would like to use? ", lowest + 1)
questions = int_check("How many questions would you like? ", 1, 10)

# randomly generates numbers between user input
equation_num1 = random.randint(lowest, highest)
equation_num2 = random.randint(lowest, highest)

# randomly chooses operation for equation and gives correct answer
operation = "+", "-", "*"
question = "What does {} {} {} equal? ".format(equation_num1, operation, equation_num2)
answer = eval(question)

