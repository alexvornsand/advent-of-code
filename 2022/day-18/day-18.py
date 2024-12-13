# advent of code 2022
# day 18

# part 1
cubes = [tuple([int(x) for x in coords.split(',')]) for coords in open('input.txt', 'r').read()[:-1].split('\n')]

def countSurfaceArea(cubes, partTwo=False):
    def countFaces(cubes):
        exposedSides = 0
        for cube in cubes:
            cubeFaces = 6
            if (cube[0] + 1, cube[1], cube[2]) in cubes:
                cubeFaces -= 1
            if (cube[0] - 1, cube[1], cube[2]) in cubes:
                cubeFaces -= 1
            if (cube[0], cube[1] + 1, cube[2]) in cubes:
                cubeFaces -= 1
            if (cube[0], cube[1] - 1, cube[2]) in cubes:
                cubeFaces -= 1
            if (cube[0], cube[1], cube[2] + 1) in cubes:
                cubeFaces -= 1
            if (cube[0], cube[1], cube[2] - 1) in cubes:
                cubeFaces -= 1
            exposedSides += cubeFaces
        return(exposedSides)
    def identifyStructures(cubes, lava=True):
        cubeClumps = {}
        i = 0
        uncommittedCubes = cubes.copy()
        while(len(uncommittedCubes) > 0):
            cube = uncommittedCubes[0]
            cubeClumps[i] = [cube]
            cubeQueue = [cube]
            uncommittedCubes.remove(cube)
            while(len(cubeQueue) > 0):
                cube = cubeQueue[0]
                cubeQueue.remove(cube)
                adjacentCubes = []
                if lava is True:
                    for xDelta in range(-1,2):
                        for yDelta in range(-1,2):
                            for zDelta in range(-1,2):
                                if xDelta != 0 or yDelta != 0 or zDelta != 0:
                                    if (cube[0] + xDelta, cube[1] + yDelta, cube[2] + zDelta) in uncommittedCubes:
                                        adjacentCubes.append((cube[0] + xDelta, cube[1] + yDelta, cube[2] + zDelta))
                                        uncommittedCubes.remove((cube[0] + xDelta, cube[1] + yDelta, cube[2] + zDelta))
                                        cubeClumps[i].append((cube[0] + xDelta, cube[1] + yDelta, cube[2] + zDelta))
                else:
                    if (cube[0] + 1, cube[1], cube[2]) in uncommittedCubes:
                            adjacentCubes.append((cube[0] + 1, cube[1], cube[2]))
                            uncommittedCubes.remove((cube[0] + 1, cube[1], cube[2]))
                            cubeClumps[i].append((cube[0] + 1, cube[1], cube[2]))
                    if (cube[0] - 1, cube[1], cube[2]) in uncommittedCubes:
                            adjacentCubes.append((cube[0] - 1, cube[1], cube[2]))
                            uncommittedCubes.remove((cube[0] - 1, cube[1], cube[2]))
                            cubeClumps[i].append((cube[0] - 1, cube[1], cube[2]))
                    if (cube[0], cube[1] + 1, cube[2]) in uncommittedCubes:
                            adjacentCubes.append((cube[0], cube[1] + 1, cube[2]))
                            uncommittedCubes.remove((cube[0], cube[1] + 1, cube[2]))
                            cubeClumps[i].append((cube[0], cube[1] + 1, cube[2]))
                    if (cube[0], cube[1] - 1, cube[2]) in uncommittedCubes:
                            adjacentCubes.append((cube[0], cube[1] - 1, cube[2]))
                            uncommittedCubes.remove((cube[0], cube[1] - 1, cube[2]))
                            cubeClumps[i].append((cube[0], cube[1] - 1, cube[2]))
                    if (cube[0], cube[1], cube[2] + 1) in uncommittedCubes:
                            adjacentCubes.append((cube[0], cube[1], cube[2] + 1))
                            uncommittedCubes.remove((cube[0], cube[1], cube[2] + 1))
                            cubeClumps[i].append((cube[0], cube[1], cube[2] + 1))
                    if (cube[0], cube[1], cube[2] - 1) in uncommittedCubes:
                            adjacentCubes.append((cube[0], cube[1], cube[2] - 1))
                            uncommittedCubes.remove((cube[0], cube[1], cube[2] - 1))
                            cubeClumps[i].append((cube[0], cube[1], cube[2] - 1))                
                cubeQueue += adjacentCubes
            i += 1
        if lava is False:
            maxX = max([cube[0] for cube in cubes])
            maxY = max([cube[1] for cube in cubes])
            maxZ = max([cube[2] for cube in cubes])
            cubeClumps = {k: v for k,v in cubeClumps.items() if (maxX, maxY, maxZ) not in v}
        return(cubeClumps)
    def invertStructure(structure):
        invertedStructure = []
        xCoords = [cube[0] for cube in structure]
        yCoords = [cube[1] for cube in structure]
        zCoords = [cube[2] for cube in structure]
        for x in range(min(xCoords), max(xCoords) + 2):
            for y in range(min(yCoords), max(yCoords) + 2):
                for z in range(min(zCoords), max(zCoords) + 2):
                    if (x,y,z) not in structure:
                        invertedStructure.append((x,y,z))        
        return(invertedStructure)
    if partTwo is True:
        externalSurface = 0
        structures = identifyStructures(cubes)
        for structure in structures:
            if len(structures[structure]) < 6:
                externalSurface += countFaces(structures[structure])
            else:
                externalSurface += countFaces(structures[structure])
                airInStructure = invertStructure(structures[structure])
                airPockets = identifyStructures(airInStructure, False)
                for pocket in airPockets:
                    externalSurface -= countSurfaceArea(airPockets[pocket])
        return(externalSurface)
    else:
        return(countFaces(cubes))

countSurfaceArea(cubes)

# part 2
countSurfaceArea(cubes, True)