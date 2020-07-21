num1 = 4
num2 = 9

operation = "+"

question = "{} {} {}".format(num1, operation, num2)
answer = eval(question)

print(question)
print(answer)