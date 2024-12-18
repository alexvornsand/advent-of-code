# advent of code 2022
# day 12

# part 1
import string

grid = [[p for p in r] for r in open('input.txt', 'r').read().split('\n')[:-1]]


def measureRoute(grid, partTwo=False):
    letters = {l: list(string.ascii_lowercase).index(l) for l in list(string.ascii_lowercase)}
    letters['S'] = 0
    letters['E'] = 25

    heightGrid = [[letters[p] for p in r] for r in grid]

    gridDict = {}
    for r in range(len(heightGrid)):
        for c in range(len(heightGrid[0])):
            gridDict[(r, c)] = heightGrid[r][c]

    neighborGrid = {}
    for cell in gridDict.keys():
        pos = list(cell)
        navigableNeighbors = []
        if pos[0] > 0: # North
            if gridDict[(pos[0] - 1, pos[1])] <= gridDict[tuple(pos)] + 1:
                navigableNeighbors.append((pos[0] - 1, pos[1]))
        if pos[1] > 0: # West
            if gridDict[(pos[0], pos[1] - 1)] <= gridDict[tuple(pos)] + 1:
                navigableNeighbors.append((pos[0], pos[1] - 1))
        if pos[0] < len(heightGrid) - 1: # South
            if gridDict[(pos[0] + 1, pos[1])] <= gridDict[tuple(pos)] + 1:
                navigableNeighbors.append((pos[0] + 1, pos[1]))
        if pos[1] < len(heightGrid[0]) - 1: # East
            if gridDict[(pos[0], pos[1] + 1)] <= gridDict[tuple(pos)] + 1:
                navigableNeighbors.append((pos[0], pos[1] + 1))
        neighborGrid[cell] = navigableNeighbors.copy()
    
    inverseNeighborGrid = {}
    for coord in neighborGrid.keys():
        for neighbor in neighborGrid[coord]:
            if neighbor in inverseNeighborGrid.keys():
                inverseNeighborGrid[neighbor].append(coord)
            else:
                inverseNeighborGrid[neighbor] = [coord]
                
    unvisitedNodes = [key for key in gridDict.keys()]
    distanceDict = {key: 999999999 for key in gridDict.keys()}
    initialNode = [(r,c) for r in range(len(heightGrid)) for c in range(len(heightGrid[0])) if grid[r][c] == 'S'][0]
    terminalNode = [(r,c) for r in range(len(heightGrid)) for c in range(len(heightGrid[0])) if grid[r][c] == 'E'][0]
    currentNode = initialNode if partTwo is False else terminalNode
    distanceDict[currentNode] = 0

    while(True):
        if partTwo is False:
            for neighbor in neighborGrid[currentNode]:
                if neighbor in unvisitedNodes:
                    if distanceDict[neighbor] >= distanceDict[currentNode] + 1:
                        distanceDict[neighbor] = distanceDict[currentNode] + 1
            if currentNode == terminalNode:
                return(distanceDict[currentNode])
            else:
                currentNode = min(unvisitedNodes, key=distanceDict.get)  
        else:
            for neighbor in inverseNeighborGrid[currentNode]:
                if neighbor in unvisitedNodes:
                    if distanceDict[neighbor] >= distanceDict[currentNode] + 1:
                        distanceDict[neighbor] = distanceDict[currentNode] + 1
            if gridDict[currentNode] == 0:
                return(distanceDict[currentNode])
            else:
                currentNode = min(unvisitedNodes, key=distanceDict.get)  
        unvisitedNodes.remove(currentNode)

measureRoute(grid)

# part 2
measureRoute(grid, True)