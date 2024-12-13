# advent of code 2022
# day 17

# part 1
import time
import os

wind = open('input.txt', 'r').read()[:-1]

def playTetris(wind, partTwo=False, n=2022):
    def checkCollisions(stack, currentRock, wind):
        rock = currentRock.copy()
        crashed = False
        if rock['shape'] == '-':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 4:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 4, rock['pos'][1]) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 2, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 3, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        elif rock['shape'] == '+':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0], rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0], rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 5:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 2, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 2, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collision with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collision with the stack
            elif (rock['pos'][0], rock['pos'][1]) in stack:
                # crashed
                crashed = True
            # check for vertical collision with the stack
            elif (rock['pos'][0] + 2, rock['pos'][1]) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        elif rock['shape'] == 'L':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 5:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 3, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 2, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        elif rock['shape'] == 'I':
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1] + 3) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 7:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 2) in stack:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 1, rock['pos'][1] + 3) in stack:
                    # crashed
                    pass

                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        else:
            # check for collisions on the side
            if wind == '<':
                # check for horizontal collision with wall
                if rock['pos'][0] == 1:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] - 1, rock['pos'][1]) in stack:
                    # crashed
                    pass
                elif (rock['pos'][0] - 1, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] - 1, rock['pos'][1])
            else:
                # check for horizontal collision with wall
                if rock['pos'][0] == 6:
                    # crashed
                    pass
                # check for horiztonal collision with the stack
                elif (rock['pos'][0] + 2, rock['pos'][1]) in stack:
                    # crashed
                    pass
                elif (rock['pos'][0] + 2, rock['pos'][1] + 1) in stack:
                    # crashed
                    pass
                else:
                    # update rock position
                    rock['pos'] = (rock['pos'][0] + 1, rock['pos'][1])

            # check for collisions with the ground
            if rock['pos'][1] == 1:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0], rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            # check for vertical collisions with the stack
            elif (rock['pos'][0] + 1, rock['pos'][1] - 1) in stack:
                # crashed
                crashed = True
            else:
                # update rock position
                rock['pos'] = (rock['pos'][0], rock['pos'][1] - 1)
        return(rock, crashed)
    def generateNextRock(maxHeight, rockIndex):
        rocks = ['-', '+', 'L', 'I', 'o']
        rockType = rocks[rockIndex % 5]
        position = (3, maxHeight + 4)
        rock = {
            'shape': rockType,
            'pos': position
        }
        return(rock)
    def rockCoordinates(rock):
        if rock['shape'] == '-':
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0] + 2, rock['pos'][1]),
                (rock['pos'][0] + 3, rock['pos'][1]),
            ])
        elif rock['shape'] == '+':
            return([
                (rock['pos'][0], rock['pos'][1] + 1),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1] + 1),
                (rock['pos'][0] + 1, rock['pos'][1] + 2),
                (rock['pos'][0] + 2, rock['pos'][1] + 1),
            ])
        elif rock['shape'] == 'L':
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0] + 2, rock['pos'][1]),
                (rock['pos'][0] + 2, rock['pos'][1] + 1),
                (rock['pos'][0] + 2, rock['pos'][1] + 2),
            ])
        elif rock['shape'] == 'I':
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0], rock['pos'][1] + 1),
                (rock['pos'][0], rock['pos'][1] + 2),
                (rock['pos'][0], rock['pos'][1] + 3),
            ])
        else:
            return([
                (rock['pos'][0], rock['pos'][1]),
                (rock['pos'][0] + 1, rock['pos'][1]),
                (rock['pos'][0], rock['pos'][1] + 1),
                (rock['pos'][0] + 1, rock['pos'][1] + 1)
            ])
    def printStack(stack, i, rock=[], m=0, rate=0.25):
        m = max(0, m)
        image = ''
        for r in range(m, m + 9)[::-1]:
            if r == m + 8:
                image += str(i + 1).ljust(10, ' ')
            elif r == m + 7:
                image += str(wind[w % modularity] + ' (' + str(w) + ')').ljust(10, ' ')
            else:
                image += '          '
            if r == 0:
                image += '+-'
            else:
                image += '| '
            for c in range(1, 8):
                if (c,r) in stack:
                    image += '# '
                elif (c,r) in rock:
                    image += '@ '
                elif r == 0:
                    image += '--'
                else:
                    image += '. '
            if r == 0:
                image += '+'
            else:
                image += '|'
            if r % 5 == 0:
                image += str(r).rjust(5, ' ')
            else:
                image += '     '
            image += '\n'
        image += '\n'
        os.system('cls')
        print(image)
        time.sleep(rate)
    modularity = len(wind)
    maxHeight = 0
    stack = []
    w = 0
    i = 0
    positionsHistory = []
    while (True):
        currentRock = generateNextRock(maxHeight, i)
        crashed = False
        while(crashed is False):
            currentRock, crashed = checkCollisions(stack, currentRock, wind[w % modularity])
            if crashed is True:
                stack += rockCoordinates(currentRock)
                currentState = ''
                for r in range(maxHeight - 64, maxHeight + 4):
                    for c in range(1, 8):
                        if (c,r) in stack:
                            currentState += '#'
                        else:
                            currentState += '.'
                maxHeight = max([coord[1] for coord in stack])
                if currentState in positionsHistory and partTwo is True:
                    cycleStart = positionsHistory.index(currentState)
                    cycleEnd = i
                    cycleLength = cycleEnd - cycleStart
                    extraRocks = (1000000000000 - cycleStart) % cycleLength
                    cycles = int((1000000000000 - cycleStart - extraRocks) / cycleLength)
                    oldMaxHeight = maxHeight
                    preamble = playTetris(wind, n = cycleStart + 1)
                    cycleHeight = oldMaxHeight - preamble
                    postamble = playTetris(wind, n = extraRocks + cycleStart) - preamble
                    return(preamble + (cycles * cycleHeight) + postamble)
                positionsHistory.append(currentState)
                w += 1
                stack = [coord for coord in stack if coord[1] >= maxHeight - 64]
            else:
                w += 1
        i += 1
        if partTwo is False and i == n:
            return(maxHeight)

playTetris(wind)

# part 2
playTetris(wind, True)
