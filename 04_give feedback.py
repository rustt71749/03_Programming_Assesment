# Component 4
# compare user input for answer and actual answer
# give appropriate feedback based on input

# hardcoded numbers
EQUATION_NUMBER1 = 10
EQUATION_NUMBER2 = 1

# answer constants
ANSWER1 = EQUATION_NUMBER1 + EQUATION_NUMBER2
ANSWER2 = EQUATION_NUMBER1 - EQUATION_NUMBER2
ANSWER3 = EQUATION_NUMBER1 * EQUATION_NUMBER2
ANSWER4 = EQUATION_NUMBER1 / EQUATION_NUMBER2

# compares user answer to actual answer
equation1 = int(input("What does {} + {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation1 != ANSWER1:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER1))
else:
    print("That answer is correct. Great job!")

equation2 = int(input("What does {} - {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation2 != ANSWER2:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER2))
else:
    print("That answer is correct. Great job!")

equation3 = int(input("What does {} x {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation3 != ANSWER3:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER3))
else:
    print("That answer is correct. Great job!")

equation4 = int(input("What does {} / {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
if equation4 != ANSWER4:
    print("Sorry that answer is not correct. The answer is {}".format(ANSWER4))
else:
    print("That answer is correct. Great job!")