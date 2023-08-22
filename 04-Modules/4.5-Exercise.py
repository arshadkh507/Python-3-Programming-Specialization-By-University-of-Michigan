# Use a for statement to print 10 random numbers.

import random

howmany = 10
for counter in range(howmany):
    arandom = random.random()
    print(arandom)


# Repeat the above exercise but this time print 10 random numbers between 25 and 35.

for counter in range(howmany):
    randomNumber = random.randrange(25, 35)
    print(randomNumber)
