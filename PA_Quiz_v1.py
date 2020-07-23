# Final Quiz
# add statement generator
# add instructions
# add if user wants to keep playing at end of quiz

import random

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

# function to print out statements and apply characters around them


def statement_generator(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char * len(statement))
    print()

# Main routine

# Intro / Rules

print("| | | | Welcome to Basic Facts Quiz | | | |")
print()
print("Answer every question as best as you can")
print()
print("Once you have entered your answer press the enter key to submit"
      "and move on to the next question")
print()

# gets user input for numbers and questions
lowest = int_check("What is the lowest number you would like to use? ")
highest = int_check("What is the highest number you would like to use? ", lowest + 1)
questions = int_check("How many questions would you like? ", 1, 10)

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

    # generates equations and equation answers
    display_equation = "What does {} {} {} equal? ".format(equation_num1, operation, equation_num2)
    equation = "{} {} {}".format(equation_num1, operation, equation_num2)
    correct_answer = eval(equation)

    answer = int_check(display_equation, -(highest * highest), (highest * highest))

    # compares user answer to actual answer
    if answer == correct_answer:
        feedback = "Your answer of {} was correct. Great job!".format(answer)
        print()
        print(feedback)
        print()
        right += 1
        result = "Correct"
    else:
        feedback = "Sorry, your answer was  incorrect. The answer was {}.".format(correct_answer)
        print()
        print(feedback)
        print()
        wrong += 1
        result = "Incorrect"

    #
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
