# advent of code 2022
# day 6

# part 1
signal = open('input.txt', 'r').read()[:-1]

def findSignalContents(signal, partTwo=False):
    if partTwo is False:
        n = 4
    else:
        n = 14
    for i in range(n - 1, len(signal)):
        if len(set(signal[(i - n):i])) == n:
            return(i)

findSignalContents(signal)

# part 2
findSignalContents(signal, True)
