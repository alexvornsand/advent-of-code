# advent of code
# day 2

# part 1
import pandas as pd

binaries = pd.DataFrame([[int(d) for d in b]
                        for b in open('day-03.txt', 'r').read().split('\n')[:-1]])


def calcPowerConsumption(binaries, partTwo=False):
    if(partTwo is False):
        gammaBin = [round(m) for m in binaries.mean(axis=0)]
        epsilonBin = [abs(1 - d) for d in gammaBin]
        gamma = int(''.join([str(d) for d in gammaBin]), 2)
        epsilon = int(''.join([str(d) for d in epsilonBin]), 2)
        print(gamma * epsilon)
    else:
        oxygenBin = binaries
        for i in range(len(oxygenBin.columns)):
            prevailingDigit = 0 if oxygenBin[i].mean() < .5 else 1
            oxygenBin = oxygenBin[oxygenBin[i] == prevailingDigit]
        carbonBin = binaries
        for i in range(len(carbonBin.columns)):
            if len(carbonBin.index) == 1:
                break
            prevailingDigit = 1 if carbonBin[i].mean() < .5 else 0
            carbonBin = carbonBin[carbonBin[i] == prevailingDigit]
        oxygen = int(''.join([str(d)
                     for d in oxygenBin.values.flatten().tolist()]), 2)
        carbon = int(''.join([str(d)
                     for d in carbonBin.values.flatten().tolist()]), 2)
        print(oxygen * carbon)


calcPowerConsumption(binaries)

# part 2
calcPowerConsumption(binaries, partTwo=True)
