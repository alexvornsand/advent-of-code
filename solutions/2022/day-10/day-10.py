# advent of code 2022
# day 10

# part 1
import numpy as np

instructions = open('input.txt', 'r').read().split('\n')[:-1]

def runProgram(instructions, partTwo=False):
    t = 0 # should be 1 but to make modular arithmetic easier, shifting down
    X = 1
    ledger = []
    for line in instructions:
        if line[0] == 'n':
            ledger.append([t, X])
            t += 1
        else:
            delta = int(line[5:])
            ledger.append([t, X])
            t += 1
            ledger.append([t, X])
            t += 1
            X += delta
    if partTwo is False:
        return(sum([np.prod([l]) for l in ledger if l[0] in [19, 59, 99, 139, 179, 219]])) # checkpoints shifted down
    else:
        pixels = ['#' if abs((l[0] % 40) - l[1]) <= 1 else ' ' for l in ledger] # convert ledger to pixels if mod(t, 40) ~= X
        pixelMap = [pixels[40 * i: 40 * i + 40] for i in range(int(len(pixels) / 40))] # shift to list of lists
        print('\n'.join([''.join([p for p in x]) for x in pixelMap])) # concatenate into a grid

runProgram(instructions)

# part 2
runProgram(instructions, True)