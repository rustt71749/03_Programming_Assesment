# Final Quiz
# add statement generator
# add instructions
# add if user wants to keep playing at end of quiz

import random

# String Checker by Miss Gottshalk
# Checks user input (either full word or first letter of word)


def string_checker(question, to_check):
    valid = False
    while not valid:
        # ask user question and change response to lowercase
        response = input(question).lower()

        # check response is in list OR that it's the first letter of an item in the list
        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        # if item not in list, print error
        print("Sorry, that response in invalid")

# Integer checking function


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

# Prints out statements and applies characters around them


def statement_generator(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()

# asks user if they have played and if not displays instructions otherwise continues to quiz


def instructions():
    instruction = string_checker("Would you like to see the instructions? ", ["yes", "no"])

    if instruction == "yes":
        print()
        print("| | | | | Quiz Instructions | | | | |")
        print()
        print("This is a simple math based quiz")
        print("Answer every question as best you can")
        print()
        print("Good luck!")
        print()
    else:
        return ""

# Main routine
statement_generator("| | | | | Welcome to The Math Quiz | | | | |", "-")
print()
instructions()

# gets user input for numbers and questions
lowest = int_check("What is the lowest number you would like to use? ")
highest = int_check("What is the highest number you would like to use? ", lowest + 1)

questions = int_check("How many questions would you like? ", 1, 10)
print()


# list for questions and answers to be used at end of game
right = 0
wrong = 0

quiz_history = []

# operation list
operations = ["+", "-", "*"]

# Start quiz
for item in range(1, questions + 1):

    # randomly generates numbers between user input
    equation_num1 = random.randint(lowest, highest)
    equation_num2 = random.randint(lowest, highest)

    # randomly chooses operation
    operation = random.choice(operations)

    # generates equations and equation answers from randomly generated operations and numbers
    display_equation = "What does {} {} {} equal? ".format(equation_num1, operation, equation_num2)
    equation = "{} {} {}".format(equation_num1, operation, equation_num2)
    correct_answer = eval(equation)

    print()
    # generates answer for any equation generated
    answer = int_check(display_equation, -(highest * highest), (highest * highest))

    # compares user answer to actual answer
    if answer == correct_answer:
        feedback = "* Your answer of {} was correct. Great job! *".format(answer)
        print()
        statement_generator(feedback, "*")
        print()
        right += 1
        result = "Correct"
    else:
        feedback = "~ Sorry, your answer was  incorrect. The answer was {}. ~".format(correct_answer)
        print()
        statement_generator(feedback, "~")
        print()
        wrong += 1
        result = "Incorrect"

    # takes round number, equation, user answer, and result to be printed out in quiz history
    equation_answer = "Equation {}: {} =?   Your answer: {}  |  {}".format(item, equation, answer, result)
    quiz_history.append(equation_answer)

# calculates quiz stats
percent_r = right / questions * 100
percent_w = wrong / questions * 100

# prints game history
print()
print("| | | | | Quiz History | | | | |")
print()
for item in quiz_history:
    print(item)

# prints game statistics
print()
print("| | | | | Quiz Stats | | | | |")
print()
print("Answers Correct: {} | {:.0f}%".format(right, percent_r))
print("Answers Incorrect: {} | {:.0f}%".format(wrong, percent_w))
print()

# if user wants to do quiz again user can redo it without having to re run the code
go_again = string_checker("Would you like to do the quiz again? ", "")

if go_again == "":

