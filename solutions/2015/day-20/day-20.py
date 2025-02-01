# advent of code 2015
# day 20

# part 1
from math import sqrt
from functools import reduce

input = open('solutions/2015/day-20/input.txt', 'r').read()

def findHouse(input, partTwo = False):
    def factorNumber(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
    if partTwo == False:
        minimum = int(input) / 10
        n = 1
        while True:
            if sum(factorNumber(n)) > minimum:
                return(n)
            else:
                n += 1
    else:
        minimum = int(input) / 11
        n = 1
        while True:
            factors = factorNumber(n)
            largeFactors = len([x for x in factors if x > 50])
            if sum(sorted(list(factors))[largeFactors:]) > minimum:
                return(n)
            else:
                n += 1

findHouse(input)

# part 2
findHouse(input, partTwo = True)