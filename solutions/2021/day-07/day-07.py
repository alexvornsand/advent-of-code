# advent of code
# day 7

# part 1
import statistics
positions = [int(x) for x in open('day-07.txt', 'r').read().split(',')]


def calculateFuelCosts(positions, partTwo=False):
    def evaluateAlignment(positions, destination):
        if partTwo is False:
            return(sum([abs(pos - destination) for pos in positions]))
        else:
            return(sum([abs(pos - destination) * (abs(pos - destination) + 1) / 2 for pos in positions]))
    startValue = statistics.median(positions)
    startCost = evaluateAlignment(positions, startValue)
    startL1Cost = evaluateAlignment(positions, startValue - 1)
    startP1Cost = evaluateAlignment(positions, startValue + 1)
    while(startCost != min([startCost, startL1Cost, startP1Cost])):
        if startL1Cost == min([startCost, startL1Cost, startP1Cost]):
            startCost = startL1Cost
            startValue = startValue - 1
            startL1Cost = evaluateAlignment(positions, startValue - 1)
        else:
            startCost = startP1Cost
            startValue = startValue + 1
            startP1Cost = evaluateAlignment(positions, startValue + 1)
    print(startCost)


calculateFuelCosts(positions)

# part 2
calculateFuelCosts(positions, partTwo=True)
