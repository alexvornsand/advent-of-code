# advent of code 2015
# day 8

# part 1
input = open('day-08.txt', 'r').read()

def countDifference(input, partTwo = False):
    if partTwo == False:
        return(sum([len(l) - len(eval(l)) for l in input.split('\n')]))
    else:
        return(sum([2 + len(l.replace('\\', '\\\\').replace('\"', '\\\"')) - len(l) for l in input.split('\n')]))

countDifference(input)

# part 2
countDifference(input, partTwo = True)