# advent of code 2015
# day 13

# part 1
import itertools

input = open('solutions/2015/day-13/input.txt', 'r').read()

def arrangeSeats(input, partTwo = False):
    happinessDict = {}
    for i in input.split('\n'):
        fromSeat = i.split(' ')[0]
        toSeat = i.split(' ')[10].replace('.', '')
        if i.split(' ')[2] == 'lose':
            happiness = -int(i.split(' ')[3])
        else:
            happiness = int(i.split(' ')[3])
        if fromSeat in happinessDict.keys():
            happinessDict[fromSeat][toSeat] = happiness
        else:
            happinessDict[fromSeat] = {toSeat: happiness}
    orders = list(itertools.permutations(list(happinessDict.keys())))
    def arrHappiness(arrangement, n):
        arrangement = list(arrangement) + [arrangement[0]]
        return(sum([happinessDict[arrangement[i]][arrangement[i + 1]] + happinessDict[arrangement[i + 1]][arrangement[i]] for i in range(n)]))
    if partTwo == False:
        return(max([arrHappiness(i, 8) for i in orders]))
    else:
        happinessDict['Me'] = {}
        for k in happinessDict.keys():
            happinessDict[k]['Me'] = 0
            happinessDict['Me'][k] = 0
        orders = list(itertools.permutations(list(happinessDict.keys())))
        return(max([arrHappiness(i, 9) for i in orders]))

arrangeSeats(input)

# part 2
arrangeSeats(input, partTwo = True)