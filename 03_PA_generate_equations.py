# Component 3 - generate equations
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

# Main routine
lowest = int_check("What is the lowest number you would like to play with? ")
highest = int_check("What is the highest number you would like to play with? ", lowest + 1)
rounds = int_check("How many rounds would you like to play? ", 1)

# generate numbers for equation between low and high
LOW = 1
HIGH = 6

for item in range(1):
    equation_number1 = random.randint(LOW, HIGH)
    equation_number2 = random.randint(LOW, HIGH)

equation1 = int(input("What does {} + {} equal?".format(lowest, highest)))