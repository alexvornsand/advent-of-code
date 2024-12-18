# advent of code 2021
# day 18

# part 1
import numpy as np
import re
import math
import itertools

snailfishNumbers = open('input.txt', 'r').read().splitlines()

def addSnailfishNumbers(snailfishNumbers, partTwo=False):
    def addPair(sf1, sf2):
        return('[' + sf1 + ',' + sf2 + ']')
    def printSF(sf):  
        i = 0
        img = ''
        depth = 0
        maxDepth = 0
        while(i < len(sf)):
            if sf[i] == ']':
                depth -= 1
            img += '\t' * depth
            if sf[i] == '[':
                depth += 1
                maxDepth = max(depth, maxDepth)
            img += sf[i]
            if i == len(sf) - 1:
                break
            while((sf[i] == ']' or re.match('\d', sf[i]) is not None) and (sf[i + 1]  == ',' or re.match('\d', sf[i + 1]) is not None)):
                i += 1
                img += sf[i]
            i += 1
            img += '\n'
        img = '\t'.join([str(i) for i in range(maxDepth + 1)]) + '\n' + img
        print(img)
    def reduceExpression(sf):
        reduced = sf
        unreduced = ''
        while reduced != unreduced:
            unreduced = reduced
            # check for explosions
            depth = list(np.cumsum([1 if d == '[' else -1 if d == ']' else 0 for d in unreduced]))
            if max(depth) == 5:
                depthLoc = depth.index(5)
                interior = re.search('(\[\d+,\d+\])', unreduced[depthLoc:]).groups()[0]
                interiorLen = len(interior)
                l, r = [int(d) for d in interior[1:-1].split(',')]
                prefix = re.sub('(\d+)', lambda d: str(int(d.group(0)[::-1]) + l)[::-1], unreduced[:depthLoc][::-1], 1)[::-1]
                suffix = re.sub('(\d+)', lambda d: str(int(d.group(0)) + r), unreduced[depthLoc + interiorLen:], 1)
                reduced = prefix + '0' + suffix
                continue
            # check for splits
            oversizeNumbers = re.search('\d{2}', unreduced)
            if oversizeNumbers is not None:
                reduced = re.sub('(\d{2})', lambda d: '[' + str(int(math.floor(int(d.group(0)) / 2))) + ',' + str(int(math.ceil(int(d.group(0)) / 2))) + ']', unreduced, 1)
                continue
        return(reduced)
    def calcMagnitude(sf):
        while('[' in sf):
            pairs = re.findall('\[\d+,\d+\]', sf)
            for pair in pairs:
                l, r = [int(d) for d in pair[1:-1].split(',')]
                val = str(3 * l + 2 * r)
                sf = sf.replace(pair, val)
        return(int(sf))
    if partTwo is False:
        total = snailfishNumbers[0]
        for i in range(1, len(snailfishNumbers)):
            total = reduceExpression(addPair(total, snailfishNumbers[i]))
        return(calcMagnitude(total))
    else:
        combinations = list(itertools.permutations(snailfishNumbers, 2))
        return(max([calcMagnitude(reduceExpression(addPair(*combination))) for combination in combinations]))
    
addSnailfishNumbers(snailfishNumbers)

# part 2
addSnailfishNumbers(snailfishNumbers, True)