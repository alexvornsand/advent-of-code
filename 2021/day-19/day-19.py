# advent of code 2021
# day 19

# part 1
import re
import itertools

report = open('input.txt', 'r').read().rstrip()

def assembleMap(report, partTwo=False):
    def parseReport(report):
        def parseScanner(scanner):
            lines = scanner.split('\n')
            name = int(re.search('\d+', lines[0]).group())
            beacons = [eval('(' + line + ')') for line in lines[1:]]
            return(name, beacons)
        scanners = report.split('\n\n')
        return(dict({name: beacons for name, beacons in [parseScanner(scanner) for scanner in scanners]}))
    def transformCoords(coord, transform):
        if transform == 'XYZ':
            return((coord[0], coord[1], coord[2]))
        elif transform == 'zYX':
            return((-coord[2], coord[1], coord[0]))
        elif transform == 'xYz':
            return((-coord[0], coord[1], -coord[2]))
        elif transform == 'ZYx':
            return((coord[2], coord[1], -coord[0]))
        elif transform == 'xyZ':
            return((-coord[0], -coord[1], coord[2]))
        elif transform == 'zyx':
            return((-coord[2], -coord[1], -coord[0]))
        elif transform == 'Xyz':
            return((coord[0], -coord[1], -coord[2]))
        elif transform == 'ZyX':
            return((coord[2], -coord[1], coord[0]))
        elif transform == 'yXZ':
            return((-coord[1], coord[0], coord[2]))
        elif transform == 'zXy':
            return((-coord[2], coord[0], -coord[1]))
        elif transform == 'YXz':
            return((coord[1], coord[0], -coord[2]))
        elif transform == 'ZXY':
            return((coord[2], coord[0], coord[1]))
        elif transform == 'YxZ':
            return((coord[1], -coord[0], coord[2]))
        elif transform == 'zxY':
            return((-coord[2], -coord[0], coord[1]))
        elif transform == 'yzx':
            return((-coord[1], -coord[0], -coord[2]))
        elif transform == 'Zxy':
            return((coord[2], -coord[0], -coord[1]))
        elif transform == 'xZY':
            return((-coord[0], coord[2], coord[1]))
        elif transform == 'yZx':
            return((-coord[1], coord[2], -coord[0]))
        elif transform == 'XZy':
            return((coord[0], coord[2], -coord[1]))
        elif transform == 'YZX':
            return((coord[1], coord[2], coord[0]))
        elif transform == 'XzY':
            return((coord[0], -coord[2], coord[1]))
        elif transform == 'yzX':
            return((-coord[1], -coord[2], coord[0]))
        elif transform == 'xzy':
            return((-coord[0], -coord[2], -coord[1]))
        elif transform == 'Yzx':
            return((coord[1], -coord[2], -coord[0]))
        else:
            print('BROKEN')
    def checkOverlap(s1, s2, scannerDict, transformations):
        for s2Beacon in scannerDict[s2]:
            for s1Beacon in scannerDict[s1]:
                for transformation in transformations:
                    transformedS2 = [transformCoords(coord, transformation) for coord in scannerDict[s2]]
                    shift = [s1coord - s2coord for s1coord, s2coord in zip(s1Beacon, transformCoords(s2Beacon, transformation))]
                    shiftedCoords = [(coord[0] + shift[0], coord[1] + shift[1], coord[2] + shift[2]) for coord in transformedS2]
                    commonBeacons = set(scannerDict[s1]).intersection(shiftedCoords)
                    if len(commonBeacons) >= 12:
                        return(shiftedCoords, shift)
    def calcDistanceApart(s1, s2, scannerLocations):
        l1 = scannerLocations[s1]
        l2 = scannerLocations[s2]
        return(abs(l2[0] - l1[0]) + abs(l2[1] - l1[1]) + abs(l2[2] - l1[2]))
    scannerDict = parseReport(report)
    transformations = [
        'XYZ', 'zYX', 'xYz', 'ZYx',
        'xyZ', 'zyx', 'Xyz', 'ZyX', 
        'yXZ', 'zXy', 'YXz', 'ZXY',
        'YxZ', 'zxY', 'yzx', 'Zxy',
        'xZY', 'yZx', 'XZy', 'YZX',
        'XzY', 'yzX', 'xzy', 'Yzx'
    ]
    unmappedScanners = list(scannerDict.keys())
    uniqueBeacons = set()
    uniqueBeacons |= set(scannerDict[0])
    unmappedScanners.remove(0)
    mappedScanners = [0]
    unmappedScanners.sort()
    scannerLocations = {0: [0, 0, 0]}
    while(len(unmappedScanners) > 0):
        i = 0
        while(True):
            target = unmappedScanners[i]
            for source in mappedScanners:
                comparisonResult = checkOverlap(source, target, scannerDict, transformations)
                if comparisonResult is not None:
                    uniqueBeacons |= set(comparisonResult[0])
                    scannerDict[target] = comparisonResult[0]
                    unmappedScanners.remove(target)
                    mappedScanners.append(target)
                    scannerLocations[target] = comparisonResult[1]
                    break
            else:
                i += 1
                continue
            break
    if partTwo is False:
        return(len(uniqueBeacons))
    else:
        pairs = itertools.combinations(list(scannerLocations.keys()), 2)
        maxDistance = max([calcDistanceApart(*pair, scannerLocations) for pair in pairs])
        return(maxDistance)

assembleMap(report)

# part 2
assembleMap(report, True)
