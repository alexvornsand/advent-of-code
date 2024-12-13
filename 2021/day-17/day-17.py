# advent of code 2021
# day 17

# part 1
import re
import math

targetRange = [int(d) for d in re.findall('-?\d+', open('input.txt', 'r').read().rstrip())]

def launchProbe(targetRange, partTwo=False):
    xMin, xMax, yMin, yMax = targetRange
    hMin = math.floor(max((1 + math.sqrt(1 + 8 * xMin)) / 2, (1 - math.sqrt(1 + 8 * xMin)) / 2))
    hMax = xMax
    vMin = yMin
    vMax = -yMin - 1
    maxHeight = []
    for v in range(vMin, vMax + 1):
        for h in range(hMin, hMax + 1):
            vert = v
            hor = h
            localMax = 0
            x = y = 0
            while y >= yMin:
                if xMin <= x <= xMax and yMin <= y <= yMax:
                    maxHeight.append(localMax)
                    break
                else:
                    y += vert
                    x += hor
                    localMax = max(localMax, y)
                    hor = hor - 1 if hor > 0 else 0
                    vert -= 1
    if partTwo is False:
        return(max(maxHeight))
    else:
        return(len(maxHeight))

launchProbe(targetRange)

# part 2
launchProbe(targetRange, True)