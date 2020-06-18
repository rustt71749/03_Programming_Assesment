# Component 4
# compare user input for answer and actual answer
# give appropriate feedback based on input

# hardcoded numbers
EQUATION_NUMBER1 = 10
EQUATION_NUMBER2 = 1

ANSWER1 = EQUATION_NUMBER1 + EQUATION_NUMBER2
ANSWER2 = EQUATION_NUMBER1 - EQUATION_NUMBER2


guess = ""


while guess != ANSWER1:
    equation1 = int(input("What does {} + {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
equation2 = int(input("What does {} - {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
equation3 = int(input("What does {} x {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))
equation4 = int(input("What does {} / {} equal? ".format(EQUATION_NUMBER1, EQUATION_NUMBER2)))



