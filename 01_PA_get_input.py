# Component 1 - get user input

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

lowest = int_check("What range do you want to play with? Low Number: ")
highest = int_check("High Number: ", lowest + 1)
rounds = int_check("How many rounds would you like to play? ", 1)
