# advent of code
# day 15

# part 1

grid = open('day-15.txt', 'r').read().split('\n')[:-1]


def findLowestRiskPath(grid, partTwo=False):
    if partTwo is True:
        widerGrid = grid.copy()
        for i in range(4):
            for r in range(len(grid)):
                rowExpansion = ''.join(
                    [str(((int(x) + i) % 9) + 1) for x in grid[r]])
                widerGrid[r] = widerGrid[r] + rowExpansion
        longerGrid = widerGrid.copy()
        for i in range(4):
            for r in range(len(grid)):
                rowExpansion = ''.join(
                    [str(((int(x) + i) % 9) + 1) for x in widerGrid[r]])
                longerGrid.append(rowExpansion)
        grid = longerGrid
    map = dict([(str(r) + '-' + str(c), int(grid[r][c]))
               for r in range(len(grid)) for c in range(len(grid[r]))])
    positions = list(map.keys())
    cumulativeMap = {'0-0': 0}
    indexSums = [int(position.split('-')[0]) + int(position.split('-')[1])
                 for position in positions]
    indexOrder = [i[0]
                  for i in sorted(enumerate(indexSums), key=lambda x:x[1])]
    updatePositions = [positions[x] for x in indexOrder]
    for position in updatePositions:
        r = int(position.split('-')[0])
        c = int(position.split('-')[1])
        parents = [str(r - 1) + '-' + str(c),
                   str(r) + '-' + str(c - 1)]
        if r != 0 and c != 0:
            cumulativeMap[position] = min(
                [cumulativeMap[parent] + map[position] for parent in parents])
        elif r != 0:
            cumulativeMap[position] = cumulativeMap[parents[0]] + map[position]
        elif c != 0:
            cumulativeMap[position] = cumulativeMap[parents[1]] + map[position]
    print(cumulativeMap[str(len(grid[0]) - 1) + '-' + str(len(grid[0]) - 1)])


findLowestRiskPath(grid)

# part 2
findLowestRiskPath(grid, partTwo=True)
