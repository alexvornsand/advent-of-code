# advent of code
# day 12

# part 1

corridors = open('day-12.txt', 'r').read().split('\n')[:-1]


def countPaths(corridors, partTwo=False):
    corridorsDict = {}
    for corridor in corridors:
        if corridor.split('-')[0] in corridorsDict:
            corridorsDict[corridor.split(
                '-')[0]].append(corridor.split('-')[1])
        else:
            corridorsDict[corridor.split('-')[0]] = [corridor.split('-')[1]]
        if corridor.split('-')[1] in corridorsDict:
            corridorsDict[corridor.split(
                '-')[1]].append(corridor.split('-')[0])
        else:
            corridorsDict[corridor.split('-')[1]] = [corridor.split('-')[0]]

    def findNextLeg(paths, corridorsDict, partTwo):
        completePaths = []
        incompletePaths = []
        for path in paths:
            if path[-1] == 'end':
                completePaths.append(path)
            else:
                possibleNextLegs = corridorsDict[path[-1]]
                if partTwo is False:
                    validNextLegs = [
                        leg for leg in possibleNextLegs if leg.lower() != leg or leg not in path]
                else:
                    validNextLegs = []
                    for leg in possibleNextLegs:
                        if leg.lower() != leg:
                            validNextLegs.append(leg)
                        elif leg not in path:
                            validNextLegs.append(leg)
                        else:
                            if 2 not in [path.count(pastLeg) for pastLeg in list(set(path)) if pastLeg.lower() == pastLeg] and leg not in ['end', 'start']:
                                validNextLegs.append(leg)
                if len(validNextLegs) > 0:
                    for leg in validNextLegs:
                        incompletePaths.append(path + [leg])
        if len(incompletePaths) > 0:
            return(findNextLeg(completePaths + incompletePaths, corridorsDict, partTwo))
        else:
            return(completePaths)
    print(len(findNextLeg([['start']], corridorsDict, partTwo)))


countPaths(corridors)

# part 2
countPaths(corridors, partTwo=True)
