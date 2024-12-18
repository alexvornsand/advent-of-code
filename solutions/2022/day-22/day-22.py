# advent of code 2022
# day 22

# part 1
import re

map = [[d for d in r] for r in open('input.txt', 'r').read()[:-1].split('\n\n')[0].split('\n')]
instructions = open('input.txt', 'r').read()[:-1].split('\n\n')[1]

def navigateMap(map, instructions, partTwo=False):
    def nextTile(position, direction, mapDict, partTwo=False):
        r = position[0]
        c = position[1]
        if direction == 'U':
            if (r - 1, c) in mapDict.keys():
                if mapDict[(r - 1, c)] == 'blocked':
                    return((r, c), 'U')
                else:
                    return((r - 1, c), 'U')
            else:
                if partTwo is False:
                    if mapDict[max([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0])] == 'blocked':
                        return((r, c), 'U')
                    else:
                        return(max([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0]), 'U')
                else:
                    if c <= 50:
                        if mapDict[(c + 50, 51)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((c + 50, 51), 'R')
                    elif c > 100:
                        if mapDict[(200, c - 100)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((200, c - 100), 'U')
                    else:
                        if mapDict[(c + 100, 1)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((c + 100, 1), 'R')
        elif direction == 'D':
            if (r + 1, c) in mapDict.keys():
                if mapDict[(r + 1, c)] == 'blocked':
                    return((r, c), 'D')
                else:
                    return((r + 1, c), 'D')
            else:
                if partTwo is False:
                    if mapDict[min([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0])] == 'blocked':
                        return((r, c), 'D')
                    else:
                        return(min([coord for coord in mapDict.keys() if coord[1] == c], key=lambda c: c[0]), 'D') 
                else:
                    if c <= 50:
                        if mapDict[(1, c + 100)] == 'blocked':
                            return((r, c), 'D')
                        else:
                            return((1, c + 100), 'D')
                    elif c > 100:
                        if mapDict[(c - 50, 100)] == 'blocked':
                            return((r, c), 'D')
                        else:
                            return((c - 50, 100), 'L')
                    else:
                        if mapDict[(c + 100, 50)] == 'blocked':
                            return((r, c), 'U')
                        else:
                            return((c + 100, 50), 'L')
        elif direction == 'L':
            if (r, c - 1) in mapDict.keys():
                if mapDict[(r, c - 1)] == 'blocked':
                    return((r, c), 'L')
                else:
                    return((r, c - 1), 'L')
            else:
                if partTwo is False:
                    if mapDict[max([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1])] == 'blocked':
                        return((r, c), 'L')
                    else:
                        return(max([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1]), 'L')
                else:
                    if r <= 50:
                        if mapDict[(150 - r + 1, 1)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((150 - r + 1, 1), 'R')
                    elif r <= 100:
                        if mapDict[(101, r - 50)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((101, r - 50), 'D')
                    elif r <= 150:
                        if mapDict[(150 - r + 1, 51)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((150 - r + 1, 51), 'R')
                    else:
                        if mapDict[(1, r - 100)] == 'blocked':
                            return((r, c), 'L')
                        else:
                            return((1, r - 100), 'D')
        else:
            if (r, c + 1) in mapDict.keys():
                if mapDict[(r, c + 1)] == 'blocked':
                    return((r, c), 'R')
                else:
                    return((r, c + 1), 'R')
            else:
                if partTwo is False:
                    if mapDict[min([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1])] == 'blocked':
                        return((r, c), 'R')
                    else:
                        return(min([coord for coord in mapDict.keys() if coord[0] == r], key=lambda c: c[1]), 'R')
                else:
                    if r <= 50:
                        if mapDict[(150 - r + 1, 100)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((150 - r + 1, 100), 'L')
                    elif r <= 100:
                        if mapDict[(50, r + 50)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((50, r + 50), 'U')
                    elif r <= 150:
                        if mapDict[(150 - r + 1, 150)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((150 - r + 1, 150), 'L')
                    else:
                        if mapDict[(150, r - 100)] == 'blocked':
                            return((r, c), 'R')
                        else:
                            return((150, r - 100), 'U')
    mapDict = {}
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == '.':
                mapDict[(r + 1, c + 1)] = 'open'
            elif map[r][c] == '#':
                mapDict[(r + 1,c + 1)] = 'blocked'
    directions = re.findall('\d+[UDLR]?', instructions)
    turn = {
        'R': {'R': 'D', 'L': 'U'},
        'U': {'R': 'R', 'L': 'L'},
        'D': {'R': 'L', 'L': 'R'},
        'L': {'R': 'U', 'L': 'D'}
    }
    position = min([coord for coord in mapDict.keys() if coord[0] == 1], key=lambda c: c[1])
    facing = 'R'
    facingKey = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    for direction in directions:
        last = re.fullmatch('\d+', direction) is not None
        if last is True:
            steps = int(direction)
        else:
            steps = int(direction[:-1])
        for i in range(steps):
            nextSpot, facing = nextTile(position, facing, mapDict, partTwo)
            if nextSpot == position:
                break
            else:
                position = nextSpot
        if last is False:
            turnDir = direction[-1]
            facing = turn[facing][turnDir]
    return(1000 * (position[0]) + 4 * (position[1]) + facingKey[facing])

navigateMap(map, instructions)

# part 2
navigateMap(map, instructions, True)
