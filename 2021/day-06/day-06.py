# advent of code
# day 6

# part 1

import pandas as pd
fish = [int(x) for x in open('day-06.txt', 'r').read().split(',')]


def breedFish(fish, partTwo=False):
    if(partTwo is True):
        n = 256
    else:
        n = 80

    def nextDay(previousDay, day):
        def ageClass(cohort):
            wholeNumbers = []
            partialNumbers = []
            for part in cohort.split('.'):
                if '-' not in part:
                    wholeNumbers.append(int(part))
                else:
                    if int(part.split('-')[1]) > 0:
                        partialNumbers.append(part.split(
                            '-')[0] + '-' + str(int(part.split('-')[1]) - 1))
                    else:
                        wholeNumbers.append(int(part.split('-')[0]))
            if len(partialNumbers) > 0:
                return(str(sum(wholeNumbers)) + '.' + '.'.join(partialNumbers))
            else:
                return(str(sum(wholeNumbers)))

        def addOffspring(id, classSize, day):
            if day % 7 == int(id):
                fertileClassSize = int(classSize.split('.')[0])
                return(str(fertileClassSize) + '-2' if fertileClassSize > 0 else '')
            else:
                return('')
        agedClass = [ageClass(x)
                     for x in previousDay.values.flatten().tolist()]
        classGrowth = [addOffspring(x, y, z) for x, y, z in zip(
            list(previousDay.columns), agedClass, [day] * 7)]
        classGrowth = classGrowth[-2:] + classGrowth[:-2]
        return([age + '.' + growth if growth != '' else age for age, growth in zip(agedClass, classGrowth)])

    def calculateTotalFish(generation):
        return(sum([sum([int(p) if '-' not in p else int(p.split('-')[0]) for p in f.split('.')]) for f in generation]))
    fishGenerations = pd.DataFrame([[str(fish.count(x)) for x in range(7)]])
    fishGenerations.columns = [str((x + 1) % 7) for x in range(7)]
    for day in range(1, n + 1):
        fishGenerations = fishGenerations.append(pd.Series(nextDay(
            fishGenerations.loc[[day - 1]], day), index=fishGenerations.columns), ignore_index=True)
    print(calculateTotalFish(
        fishGenerations.iloc[[-1]].values.flatten().tolist()))


breedFish(fish)

# part 2
breedFish(fish, partTwo=True)
