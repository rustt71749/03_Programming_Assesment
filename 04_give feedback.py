# Component 4
# compare user input for answer and actual answer
# give appropriate feedback based on input

# Number checking function:


def int_check(question, low, high):

    valid = False
    error = "Please enter an integer"
    while not valid:

        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# hardcoded numbers
EQUATION_NUMBER1 = 10
EQUATION_NUMBER2 = 1

# answer constants
ANSWER1 = EQUATION_NUMBER1 + EQUATION_NUMBER2
ANSWER2 = EQUATION_NUMBER1 - EQUATION_NUMBER2
ANSWER3 = EQUATION_NUMBER1 * EQUATION_NUMBER2
ANSWER4 = EQUATION_NUMBER1 // EQUATION_NUMBER2
ANSWER5 = EQUATION_NUMBER1 ** EQUATION_NUMBER2

# Compares user answer to actual answer

equation1 = int_check(input("What does {} + {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation1 != ANSWER1:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER1))
else:
    print("That answer is correct. Great job!")

equation2 = int_check(input("What does {} - {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation2 != ANSWER2:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER2))
else:
    print("That answer is correct. Great job!")

equation3 = int_check(input("What does {} x {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation3 != ANSWER3:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER3))
else:
    print("That answer is correct. Great job!")

equation4 = int_check(input("What does {} / {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation4 != ANSWER4:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER4))
else:
    print("That answer is correct. Great job!")

equation5 = int_check(input("What does {} ^ {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation5 != ANSWER5:
    print("Sorry, that answer is not correct. The answer is {}".format(ANSWER5))
else:
    print("That answer is correct. Great job!")
