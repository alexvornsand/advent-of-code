# advent of code 2022
# day 5

# part 1
import re

stacks = open('input.txt', 'r').read().split('\n\n')[0].split('\n')[:-1]
moves = open('input.txt', 'r').read().split('\n\n')[1].split('\n')[:-1]

def collectSupplies(stacks, moves, partTwo=False):
    stacksDict = {}
    for i in range(9):
        stacksDict[i + 1] = list(filter(lambda i: i != ' ', [stack[(4 * i + 1):(4 * i + 2)] for stack in stacks]))
        
    for move in moves:
        moveIds = re.search(r"(\b\d+\b).+(\b\d+\b).+(\b\d+\b)", move)
        n = int(moveIds.groups()[0])
        s = int(moveIds.groups()[1])
        d = int(moveIds.groups()[2])
        if partTwo is False:
            stacksDict[d] = stacksDict[s][:n][::-1] + stacksDict[d]
        else:
            stacksDict[d] = stacksDict[s][:n] + stacksDict[d]        
        stacksDict[s] = stacksDict[s][n:]
    return(''.join([stacksDict[i + 1][0] for i in range(9)]))

collectSupplies(stacks, moves)

# part 2
collectSupplies(stacks, moves, True)