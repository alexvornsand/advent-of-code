# advent of code 2022
# day 8

# part 1
grid = [[int(x) for x in g] for g in open('input.txt', 'r').read().split('\n')[:-1]]

def findTreehouse(grid, partTwo=False):
    visible = (2 * (len(grid) - 1)) + (2 * (len(grid[0]) - 1))
    scenicScore = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            dirDict = {}
            dirDict['N'] = [grid[y][x] > grid[n][x] for n in range(y + 1, len(grid))]
            dirDict['E'] = [grid[y][x] > grid[y][e] for e in range(x)][::-1]
            dirDict['S'] = [grid[y][x] > grid[s][x] for s in range(y)][::-1]
            dirDict['W'] = [grid[y][x] > grid[y][w] for w in range(x + 1, len(grid[0]))]
            if any([all(dirDict['N']), all(dirDict['E']), all(dirDict['S']), all(dirDict['W'])]):
                visible += 1
            visibleTrees = {}
            for d in dirDict.keys():
                visibleTrees[d] = 0
                for v in dirDict[d]:
                    if v is True:
                        visibleTrees[d] += 1
                    else:
                        visibleTrees[d] += 1
                        break
            treeScore = visibleTrees['N'] * visibleTrees['E'] * visibleTrees['S'] * visibleTrees['W']
            if treeScore > scenicScore:
                scenicScore = treeScore
    if partTwo is False:
        return(visible)
    else:
        return(scenicScore)        

findTreehouse(grid)

# part 2
findTreehouse(grid, True)
