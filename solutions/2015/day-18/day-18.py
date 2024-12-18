# advent of code 2015
# day 18

# part 1
input = open('day-18.txt', 'r').read()

def flickerLights(input, partTwo = False):
    def queryLight(r, c):
        if r in range(len(lightGrid)):
            if c in range(len(lightGrid[r])):
                return(lightGrid[r][c])
            else:
                return(0)
        else:
            return(0)
    def updateLight(r, c, partTwo):
        if partTwo == True and (r == 0 or r == 99) and (c == 0 or c == 99):
            return(1)
        neighborSum = sum([
            queryLight(r + 1, c + 1),
            queryLight(r + 1, c),
            queryLight(r + 1, c - 1),
            queryLight(r, c - 1),
            queryLight(r - 1, c - 1),
            queryLight(r - 1, c),
            queryLight(r - 1, c + 1),
            queryLight(r, c + 1),
        ])
        if lightGrid[r][c] == 1:
            if neighborSum == 2 or neighborSum == 3:
                return(1)
            else:
                return(0)
        else:
            if neighborSum == 3:
                return(1)
            else:
                return(0)
    def updateLights(lightGrid):
        return([[updateLight(r, c, partTwo = partTwo) for c in range(len(lightGrid[r]))] for r in range(len(lightGrid))])
    lightGrid = [[int(i) for i in r] for r in input.replace('#', '1').replace('.', '0').split('\n')]
    for i in range(100):
        lightGrid = updateLights(lightGrid)
    return(sum([i for row in lightGrid for i in row]))

flickerLights(input)

# part 2
flickerLights(input, partTwo = True)