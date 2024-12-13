# advent of code 2022
# day 23

# part 1
map = [[d for d in r] for r in open('input.txt', 'r').read()[:-1].split('\n')]

def plantTrees(map, partTwo=False):
    def nextPos(pos, turn):
        seq = turn % 4
        r, c = pos
        nLoc = (r - 1, c)
        N = nLoc in grid
        neLoc = (r - 1, c + 1)
        NE = neLoc in grid
        eLoc = (r, c + 1)
        E = eLoc in grid
        seLoc = (r + 1, c + 1)
        SE = seLoc in grid
        sLoc = (r + 1, c)
        S = sLoc in grid
        swLoc = (r + 1, c - 1)
        SW = swLoc in grid
        wLoc = (r, c - 1)
        W = wLoc in grid
        nwLoc = (r - 1, c - 1)
        NW = nwLoc in grid
        n = any([NW, N, NE])
        e = any([NE, E, SE])
        s = any([SE, S, SW])
        w = any([SW, W, NW])
        checks = ['n', 's', 'w', 'e']
        checksDict = {'n': nLoc, 's': sLoc, 'w': wLoc, 'e': eLoc}
        if not any([n, s, w, e]):
            return(pos)
        for check in checks[seq:] + checks[:seq]:
            if eval(check) is False:
                return(checksDict[check])
        return(pos)
    def move(grid, turn):
        newPositions = {pos: nextPos(pos, turn) for pos in grid.keys()}
        newInvalidPositions = list(set([pos for pos in newPositions.values() if list(newPositions.values()).count(pos) > 1]))
        newGridCoords = [newPositions[pos] if newPositions[pos] not in newInvalidPositions else pos for pos in newPositions]
        newGrid = {}
        for coord in newGridCoords:
            newGrid[coord] = '#'
        return(newGrid)
    grid = {}
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == '#':
                grid[(r, c)] = '#'
    if partTwo is False:
        for i in range(10):
            grid = move(grid, i)
        return((max([pos[0] for pos in grid]) - min([pos[0] for pos in grid]) + 1) * (max([pos[1] for pos in grid]) - min([pos[1] for pos in grid]) + 1) - len(grid))
    else:
        i = 0
        while(True):
            nextGrid = move(grid, i)
            i += 1
            if nextGrid == grid:
                return(i)
            else:
                grid = nextGrid.copy()
            
plantTrees(map)

# part 2
plantTrees(map, True)