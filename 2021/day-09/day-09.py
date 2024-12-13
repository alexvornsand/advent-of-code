# advent of code
# day 9

# part 1
import numpy as np
depths = [[9] * (len(open('day-09.txt', 'r').read().split('\n')[0]) + 2)] + [[9] + [int(cell) for cell in row] + [9]
                                                                             for row in open('day-09.txt', 'r').read().split('\n')[:-1]] + [[9] * (len(open('day-09.txt', 'r').read().split('\n')[0]) + 2)]


def assessBasin(depths, partTwo=False):
    minima = []
    minimaLocations = []
    for r in range(1, len(depths) - 1):
        for c in range(1, len(depths[r]) - 1):
            neighbors = []
            neighbors.append(depths[r - 1][c])
            neighbors.append(depths[r][c - 1])
            neighbors.append(depths[r][c + 1])
            neighbors.append(depths[r + 1][c])
            if depths[r][c] < min(neighbors):
                minima.append(depths[r][c])
                minimaLocations.append([r, c])
    if partTwo is False:
        print(sum(minima) + len(minima))
    else:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        assignments = []
        for i in range(len(minimaLocations)):
            letterAssignment = letters[i // 26] + letters[i % 26]
            depths[minimaLocations[i][0]
                   ][minimaLocations[i][1]] = letterAssignment
            assignments.append(letterAssignment)
        updates = True
        loops = 0
        while updates is True:
            loops += 1
            updates = False
            for r in range(1, len(depths) - 1):
                for c in range(1, len(depths[r]) - 1):
                    if depths[r][c] in assignments:
                        if depths[r + 1][c] != 9 and depths[r + 1][c] not in assignments:
                            depths[r + 1][c] = depths[r][c]
                            updates = True
                        if depths[r][c + 1] != 9 and depths[r][c + 1] not in assignments:
                            depths[r][c + 1] = depths[r][c]
                            updates = True
                        if depths[r - 1][c] != 9 and depths[r - 1][c] not in assignments:
                            depths[r - 1][c] = depths[r][c]
                            updates = True
                        if depths[r][c - 1] != 9 and depths[r][c - 1] not in assignments:
                            depths[r][c - 1] = depths[r][c]
                            updates = True
        flattenedMap = [x for y in depths for x in y]
        basinSizes = [flattenedMap.count(x) for x in assignments]
        basinSizes.sort(reverse=True)
        print(basinSizes[0] * basinSizes[1] * basinSizes[2])


assessBasin(depths)

# part 2
assessBasin(depths, partTwo=True)
