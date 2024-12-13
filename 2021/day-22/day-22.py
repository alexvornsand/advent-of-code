# advent of code 2021
# day 22

# part 1
import re

instructions = open('input.txt', 'r').read().rstrip().splitlines()

def rebootSystem(instructions, partTwo=False):
    def parseInstruction(instruction):
        state, xMin, xMax, yMin, yMax, zMin, zMax = re.search('([a-z]*)\sx=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)', instruction).groups()
        return(1 if state == 'on' else 0, int(xMin), int(xMax), int(yMin), int(yMax), int(zMin), int(zMax))
    def findCubeIntersection(c1, c2):
        xMax = min(c1[2], c2[2])
        xMin = max(c1[1], c2[1])
        yMax = min(c1[4], c2[4])
        yMin = max(c1[3], c2[3])
        zMax = min(c1[6], c2[6])
        zMin = max(c1[5], c2[5])
        if xMin <= xMax and yMin <= yMax and zMin <= zMax:
            return(-c2[0], xMin, xMax, yMin, yMax, zMin, zMax)
        else:
            return(None)
    def findAllCubes(fills):
        cubes = []
        for fill in fills:
            newFills = []
            if fill[0] == 1:
                newFills.append(fill)
            for cube in cubes:
                intersection = findCubeIntersection(fill, cube)
                if intersection:
                    newFills.append(intersection)
            cubes += newFills
        return(cubes)
    def countCubeVols(cubes):
        fillVol = 0
        for cube in cubes:
            state, xMin, xMax, yMin, yMax, zMin, zMax = cube
            if partTwo is False:
                xMin = max(xMin, -50)
                xMax = min(xMax, 50)
                yMin = max(yMin, -50)
                yMax = min(yMax, 50)
                zMin = max(zMin, -50)
                zMax = min(zMax, 50)
            if xMin <= xMax and yMin <= yMax and zMin <= zMax:
                fillVol += state * (xMax - xMin + 1) * (yMax - yMin + 1) * (zMax - zMin + 1)
        return(fillVol)
    fills = [parseInstruction(instruction) for instruction in instructions]
    cubes = findAllCubes(fills)
    fillVol = countCubeVols(cubes)
    return(fillVol)

rebootSystem(instructions)

# part 2

rebootSystem(instructions, True)