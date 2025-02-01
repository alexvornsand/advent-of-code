# advent of code 2015
# day 17

# part 1
import itertools

input = open('solutions/2015/day-17/input.txt', 'r').read()

def combineJugs(input, partTwo = False):
    jugs = [int(x) for x in input.split('\n')]
    if partTwo == False:
        combinations = [item for sublist in [list(itertools.combinations(jugs, i)) for i in range(len(jugs) + 1)] for item in sublist]
        return(len([x for x in combinations if sum(x) == 150]))
    else:
        for i in range(len(jugs) + 1):
            combinations = list(itertools.combinations(jugs, i))
            if len([x for x in combinations if sum(x) == 150]) > 0:
                return(len([x for x in combinations if sum(x) == 150]))

combineJugs(input)

# part 2
combineJugs(input, partTwo = True)