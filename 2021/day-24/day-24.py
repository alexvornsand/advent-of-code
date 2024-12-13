# advent of code 2021
# day 24

# part 1
import re

instructions = open('input.txt', 'r').read().rstrip().splitlines()

def checkModelNumbers(instructions, partTwo=False):
    divs = [int(instructions[i].split(' ')[-1]) for i in range(len(instructions)) if i % 18 == 4]
    checks = [int(instructions[i].split(' ')[-1]) for i in range(len(instructions)) if i % 18 == 5]
    offsets = [int(instructions[i].split(' ')[-1]) for i in range(len(instructions)) if i % 18 == 15]
    cycles = [(x, y, z) for x, y, z in zip(divs, checks, offsets)]
    pairings = []
    queue = []
    for c in range(len(cycles)):
        if cycles[c][1] > 0:
            queue.append(c)
            pairings.append(c)
        else:
            pairings.append(queue[-1])
            queue.pop(-1)
    contenders = {}
    for p in range(max(pairings) + 1):
        if p in pairings:
            i, o = [s for s in range(len(pairings)) if pairings[s] == p]
            diff = cycles[o][1] + cycles[i][2]
            if diff < 0:
                contenders[o] = list(range(1, 10 + diff))
                contenders[i] = list(range(1 - diff, 10))
            elif diff > 0:
                contenders[i] = list(range(1, 10 - diff))
                contenders[o] = list(range(1 + diff, 10))
            else:
                contenders[i] = list(range(1, 10))
                contenders[o] = list(range(1, 10))
    num = ''
    for i in range(14):
        if partTwo is False:
            num += str(max(contenders[i]))
        else:
            num += str(min(contenders[i]))
    return(int(num))

checkModelNumbers(instructions)

# part 2
checkModelNumbers(instructions, True)