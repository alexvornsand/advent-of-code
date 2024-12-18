# advent of code 2015
# day 9

# part 1
import itertools

input = open('day-09.txt', 'r').read()

def getTravelDistance(input, partTwo = False):
    distances = {}
    for i in input.split('\n'):
        fromCity = i.split(' ')[0]
        toCity = i.split(' ')[2]
        distance = int(i.split(' ')[4])
        if fromCity in distances.keys():
            distances[fromCity][toCity] = distance
        else:
            distances[fromCity] = {toCity: distance}
        if toCity in distances.keys():
            distances[toCity][fromCity] = distance
        else:
            distances[toCity] = {fromCity: distance}
    orders = list(itertools.permutations(list(set([item for sublist in [[i.split(' ')[0], i.split(' ')[2]] for i in input.split('\n')] for item in sublist]))))
    def travelDistance(itin):
        return(sum([distances[itin[i]][itin[i + 1]] for i in range(7)]))
    travelDistances = [travelDistance(i) for i in orders]
    if partTwo == False:
        return(min(travelDistances))
    else:
        return(max(travelDistances))

getTravelDistance(input)

# part 2
getTravelDistance(input, partTwo = True)