# Component 5 trial 2
# compare user input for answer and actual answer
# give appropriate feedback based on input
# shortened length of code

import random

# Number checking function


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

<<<<<<< HEAD

=======
>>>>>>> a55528c2f96bb2f163b5215ea8b430be8a2d7fda
# Main routine
lowest = int_check("What is the lowest number you would like to use? ")
highest = int_check("What is the highest number you would like to use? ", lowest + 1)
questions = int_check("How many questions would you like? ", 1, 10)

# list for questions and answers to be used at end of game
right = 0
wrong = 0

<<<<<<< HEAD
game_history = []

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

    if answer == correct_answer:
        feedback = "Your answer of {} was correct. Great job!".format(answer)
        print(feedback)
        right += 1
    else:
        feedback = "Sorry, your answer was not correct. The answer was {}.".format(correct_answer)
        print(feedback)
        wrong += 1

    equation_answer = "Equation {}: {} {}".format(item, display_equation, feedback)
    game_history.append(equation_answer)

print()
print("| | | | | Results | | | | |")

for item in game_history:
    print(item)
=======
# list for questions and answers to be used at end of game
right = 0
wrong = 0

game_history = []

# Start quiz
for item in range(1, questions + 1):
# operation list 
  operations = ["+", "-", "*"]
  
#randomly chooses operation
  operation = random.choice(operations)

  question = "What does {} {} {} equal? ".format(equation_num1, operation, equation_num2)
  
  correct_answer = eval(question)
  
  answer = int_check(question, -(highest*highest), (highest*highest)

  if answer == correct_answer:
    print("That answer is correct. Great job!")
    right += 1
  else:
    print("Sorry, that answer is not correct. The answer is {}.".format(correct_answer))
    wrong +=1

  equation_answer = "Equation {}: {}".format(item, answer)
  game_history.append(equation_answer)

print()
print(||||| Answers |||||)

for item in game_history:
  print(item)
>>>>>>> a55528c2f96bb2f163b5215ea8b430be8a2d7fda
