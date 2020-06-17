# Component 1 - get user input

# Number checking function:


def int_check(question, low=None, high=None):

    # error messages
    if low is not None and high is not None:
        error = "Please enter an integer that is 10, 25, 50, or 100 " \
                .format(low, high)
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
lowest = 1
highest = int_check("What is the highest number would you like to play with? ", lowest + 9)
rounds = int_check("How many rounds would you like to play? ", 1)
