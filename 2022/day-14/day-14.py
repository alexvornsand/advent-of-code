# advent of code 2022
# day 14

# part 1
structures = [structure.split(' -> ') for structure in open('input.txt', 'r').read().split('\n')[:-1]]

def analyzeCave(structures, partTwo=False):
    caveSlice = {}
    maxX = 0
    maxY = 0
    for structure in structures:
        for i in range(len(structure) - 1):
            xMin = min(int(structure[i].split(',')[0]), int(structure[i + 1].split(',')[0]))
            xMax = max(int(structure[i].split(',')[0]), int(structure[i + 1].split(',')[0])) + 1
            yMin = min(int(structure[i].split(',')[1]), int(structure[i + 1].split(',')[1]))
            yMax = max(int(structure[i].split(',')[1]), int(structure[i + 1].split(',')[1])) + 1
            for x in range(xMin, xMax):
                for y in range(yMin, yMax):
                    maxX = x if x > maxX else maxX
                    maxY = y if y > maxY else maxY
                    caveSlice[(x, y)] = '#'

    def enactGravity(caveSlice, coord, maxY):
        x = coord[0]
        y = coord[1]
        if y == maxY + 1:
            return(coord)
        elif (x, y + 1) not in caveSlice.keys(): # can fall down
            return(enactGravity(caveSlice, (x, y + 1), maxY))
        elif (x - 1, y + 1) not in caveSlice.keys(): # can fall diagonal left
            return(enactGravity(caveSlice, (x - 1, y + 1), maxY))
        elif (x + 1, y + 1) not in caveSlice.keys(): # can fall diagonal right
            return(enactGravity(caveSlice, (x + 1, y + 1), maxY))
        else: # stuck
            return(coord)
    while(True):
        landing = enactGravity(caveSlice, (500, 0), maxY)
        if partTwo is False and landing[1] > maxY:
            break
        elif partTwo is True and landing == (500, 0):
            caveSlice[landing] = 'o'
            break
        else:
            caveSlice[landing] = 'o'
    return(sum([value == 'o' for value in caveSlice.values()]))

analyzeCave(structures)

# part 2
analyzeCave(structures, True)