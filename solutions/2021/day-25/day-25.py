# advent of code 2021
# day 25

# part 1
import copy

cucumberGrid = [[d for d in l] for l in open('input.txt', 'r').read().rstrip().splitlines()]

def findLandingSpace(cucumberGrid):
    cucumberDict = {}
    blankDict = {}
    for r in range(len(cucumberGrid)):
        for c in range(len(cucumberGrid[r])):
            cucumberDict[(r, c)] = cucumberGrid[r][c]
            blankDict[(r, c)] = '.'
    i = 1
    while(True):
        nextDict = copy.deepcopy(blankDict)
        for r in range(len(cucumberGrid)):
            for c in range(len(cucumberGrid[r])):
                if cucumberDict[(r, c)] == '>':
                    if c + 1 == len(cucumberGrid[0]):
                        nextC = 0
                    else:
                        nextC = c + 1
                    if cucumberDict[(r, nextC)] == '.':
                        nextDict[(r, nextC)] = '>'
                    else:
                        nextDict[(r, c)] = '>'
                elif cucumberDict[(r, c)] == 'v':
                    nextDict[(r, c)] = 'v'
        stage2Dict = copy.deepcopy(nextDict)
        nextDict = copy.deepcopy(blankDict)
        for r in range(len(cucumberGrid)):
            for c in range(len(cucumberGrid[r])):
                if stage2Dict[(r, c)] == 'v':
                    if r + 1 == len(cucumberGrid):
                        nextR = 0
                    else:
                        nextR = r + 1
                    if stage2Dict[(nextR, c)] == '.':
                        nextDict[(nextR, c)] = 'v'
                    else:
                        nextDict[(r, c)] = 'v'
                elif stage2Dict[(r, c)] == '>':
                    nextDict[(r, c)] = '>'
        if nextDict == cucumberDict:
            break
        else:
            cucumberDict = copy.deepcopy(nextDict)
            i += 1
    return(i)

findLandingSpace(cucumberGrid)