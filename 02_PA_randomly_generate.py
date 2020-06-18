# Component 2 - randomly generate numbers

# randomly generate numbers between low and high

import random

LOW = 1
HIGH = 6

for item in range(1, 20):
    equation_numbers = random.randint(LOW, HIGH)
    print(equation_numbers, end="\t")
    equation_numbers2 = random.randint(LOW, HIGH)
    print(equation_numbers2, end="\t")