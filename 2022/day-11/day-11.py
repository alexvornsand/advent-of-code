# advent of code 2022
# day 11

# part 1

import math

monkeys = open('input.txt', 'r').read()[:-1].split('\n\n')

def tallyMonkeyBusiness(monkeys, partTwo=False):
    def parseMonkeys(monkeys):
        monkeyDict = {}
        for monkey in monkeys:
            monkeyInfo = parseMonkey(monkey)
            monkeyDict[monkeyInfo['id']] = monkeyInfo
        return(monkeyDict)

    def parseMonkey(monkey):
        monkeyLine = monkey.split('\n')
        monkeyInfo = {}
        monkeyInfo['id'] = int(monkeyLine[0][-2])
        monkeyInfo['items'] = [int(x) for x in monkeyLine[1][18:].split(',')]
        monkeyInfo['operation'] = monkeyLine[2][19:]
        monkeyInfo['test'] = int(monkeyLine[3][21:])
        monkeyInfo['true'] = int(monkeyLine[4][-1])
        monkeyInfo['false'] = int(monkeyLine[5][-1])
        monkeyInfo['inspections'] = 0
        return(monkeyInfo)

    monkeyDict = parseMonkeys(monkeys)

    modulo = math.prod([monkeyDict[monkey]['test'] for monkey in monkeyDict.keys()])

    r = 10000 if partTwo else 20

    for round in range(r):
        for monkey in sorted(monkeyDict.keys()):
            items = monkeyDict[monkey]['items'].copy()
            for item in items:
                monkeyDict[monkey]['inspections'] += 1
                monkeyDict[monkey]['items'] = monkeyDict[monkey]['items'][1:]
                old = item
                new = eval(monkeyDict[monkey]['operation'])
                if partTwo is False:
                    new = math.floor(new / 3)
                else:
                    new = new % modulo
                if new % monkeyDict[monkey]['test'] == 0:
                    monkeyDict[monkeyDict[monkey]['true']]['items'].append(new)
                else:
                    monkeyDict[monkeyDict[monkey]['false']]['items'].append(new)
                    
    totalInspections = [monkeyDict[monkey]['inspections'] for monkey in monkeyDict.keys()]
    return(math.prod(sorted(totalInspections)[-2:]))
                    
tallyMonkeyBusiness(monkeys)

# part 2
tallyMonkeyBusiness(monkeys, True)
