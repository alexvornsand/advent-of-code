# advent of code
# day 4

# part 1
lines = open('day-05.txt', 'r').read().split('\n')[:-1]


def countOverlappingLines(lines, partTwo=False):
    coords = {}

    def determineCoords(x1, y1, x2, y2, partTwo):
        if(x1 == x2):
            if(y1 < y2):
                ys = list(range(y1, y2 + 1))
            else:
                ys = list(range(y2, y1 + 1))[::-1]
            xs = [x1] * len(ys)
        elif(y1 == y2):
            if(x1 < x2):
                xs = list(range(x1, x2 + 1))
            else:
                xs = list(range(x2, x1 + 1))[::-1]
            ys = [y1] * len(xs)
        elif(partTwo is True):
            if(x1 < x2):
                xs = list(range(x1, x2 + 1))
            else:
                xs = list(range(x2, x1 + 1))[::-1]
            if(y1 < y2):
                ys = list(range(y1, y2 + 1))
            else:
                ys = list(range(y2, y1 + 1))[::-1]
        else:
            return([])
        return([str(x) + '-' + str(y) for x, y in zip(xs, ys)])

    def updateCell(coord, coords):
        if(coord in coords):
            coords[coord] += 1
        else:
            coords[coord] = 1
        return(coords)
    for line in lines:
        start = line.split(' -> ')[0]
        end = line.split(' -> ')[1]
        xStart = int(start.split(',')[0])
        yStart = int(start.split(',')[1])
        xEnd = int(end.split(',')[0])
        yEnd = int(end.split(',')[1])
        for coord in determineCoords(xStart, yStart, xEnd, yEnd, partTwo):
            coords = updateCell(coord, coords)
    print(len([coords[x] for x in coords if coords[x] >= 2]))


countOverlappingLines(lines)

# part 2
countOverlappingLines(lines, partTwo=True)
