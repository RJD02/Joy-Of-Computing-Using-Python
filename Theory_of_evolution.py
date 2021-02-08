"""
Theory of evolution, we have a data containing 0s and 1s. We need to interpret if the data provided has a chance
.of evolving or not based on given condition.
"""
import random

def evolve(x):
    # randint(a, b) generates random integers in range [a, b]
    index = random.randint(0, len(x) - 1)
    p = random.randint(1, 100)
    print(p)
    if p == 1:
        if x[index] == '0':
            x[index] = '1'
        else:
            x[index] = '0'

# x = []
with open("in.txt", "r") as input:
    # x.append(input.read())
    x = input.read()
    x = list(x)
    
for i in range(10000):
    evolve(x)
    
print(x)
