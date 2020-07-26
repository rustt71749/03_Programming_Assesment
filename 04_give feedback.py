# Component 4
# compare user input for answer and actual answer
# give appropriate feedback based on input

import random

# Integer checking function:


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

# Main routine
lowest = int_check("What is the lowest number you would like to use? ")
highest = int_check("What is the highest number you would like to use? ", lowest + 1)
questions = int_check("How many questions would you like? ", 1, 10)

# randomly generates numbers between user input
equation_number1 = random.randint(lowest, highest)
equation_number2 = random.randint(lowest, highest)

answer1 = equation_number1 + equation_number2
answer2 = equation_number1 - equation_number2
answer3 = equation_number1 * equation_number2
answer4 = equation_number1 // equation_number2

# Compares user answer to actual answer
question0 = "What does {} + {} equal? ".format(equation_number1, equation_number2)
equation1 = int_check(question0, -(highest*highest), highest*highest)

if equation1 != answer1:
    print("Sorry, that answer is not correct. The answer is {}.".format(answer1))
else:
    print("That answer is correct. Great job!")

question2 = "What does {} - {} equal? ".format(equation_number1, equation_number2)
equation2 = int_check(question2, -(highest*highest), highest*highest)

if equation2 != answer2:
    print("Sorry, that answer is not correct. The answer is {}.".format(answer2))
else:
    print("That answer is correct. Great job!")


question3 = "What does {} x {} equal? ".format(equation_number1, equation_number2)
equation3 = int_check(question3, -(highest*highest), highest*highest)

if equation3 != answer3:
    print("Sorry, that answer is not correct. The answer is {}.".format(answer3))
else:
    print("That answer is correct. Great job!")

question4 = "What does {} / {} equal ? ".format(equation_number1, equation_number2)
equation4 = int_check(question4, -(highest*highest), highest*highest)

if equation4 != answer4:
    print("Sorry, that answer is not correct. The answer is {}.".format(answer4))
else:
    print("That answer is correct. Great job!")
