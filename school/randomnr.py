# generate random floating point values
from random import seed
from random import random
from random import randint

def randomnumber():
# seed random number generator
    seed(1)
# generate random numbers between 0-1
    for _ in range(10):
        x = 6*random()
        print(x)

# call function
randomnumber()

def randomint():
# seed random number generator
    seed(1)

# generate some integers
    for _ in range(10):
        value = randint(0, 10)
        print(value)
# call function
randomint()