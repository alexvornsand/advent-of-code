# advent of code 2015
# day 7

# part 1
input = open('day-07.txt', 'r').read()

def findAValue(input, partTwo = False):
    assignments = input.split('\n')
    map = {}
    while(len(assignments) > 0):
        for assgn in assignments:
            if 'AND' in assgn:
                if assgn.split(' ')[0].isnumeric():
                    if assgn.split(' ')[2].isnumeric():
                        map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) & int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[2] in map.keys():
                        map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) & map[assgn.split(' ')[2]]
                        assignments.pop(assignments.index(assgn))
                elif assgn.split(' ')[0] in map.keys():
                    if assgn.split(' ')[2].isnumeric():
                        map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] & int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[2] in map.keys():
                        map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] & map[assgn.split(' ')[2]]
                        assignments.pop(assignments.index(assgn))
            elif 'OR' in assgn:
                if assgn.split(' ')[0].isnumeric():
                    if assgn.split(' ')[2].isnumeric():
                        map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) | int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[2] in map.keys():
                        map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) | map[assgn.split(' ')[2]]
                        assignments.pop(assignments.index(assgn))
                elif assgn.split(' ')[0] in map.keys():
                    if assgn.split(' ')[2].isnumeric():
                        map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] | int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[2] in map.keys():
                        map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] | map[assgn.split(' ')[2]]
                        assignments.pop(assignments.index(assgn))
            elif 'LSHIFT' in assgn:
                if assgn.split(' ')[0].isnumeric():
                    map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) << int(assgn.split(' ')[2])
                    assignments.pop(assignments.index(assgn))
                elif assgn.split(' ')[0] in map.keys():
                    map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] << int(assgn.split(' ')[2])
                    assignments.pop(assignments.index(assgn))
            elif 'RSHIFT' in assgn:
                if assgn.split(' ')[0].isnumeric():
                    map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) >> int(assgn.split(' ')[2])
                    assignments.pop(assignments.index(assgn))
                elif assgn.split(' ')[0] in map.keys():
                    map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] >> int(assgn.split(' ')[2])
                    assignments.pop(assignments.index(assgn))
            elif 'NOT' in assgn:
                if assgn.split(' ')[1].isnumeric():
                    map[assgn.split(' ')[3]] = ~int(assgn.split(' ')[1])
                    assignments.pop(assignments.index(assgn))
                elif assgn.split(' ')[1] in map.keys():
                    map[assgn.split(' ')[3]] = ~map[assgn.split(' ')[1]]
                    assignments.pop(assignments.index(assgn))
            else:
                if assgn.split(' ')[0].isnumeric():
                    map[assgn.split(' ')[2]] = int(assgn.split(' ')[0])
                    assignments.pop(assignments.index(assgn))
                elif assgn.split(' ')[0] in map.keys():
                    map[assgn.split(' ')[2]] = map[assgn.split(' ')[0]]
                    assignments.pop(assignments.index(assgn))
    if partTwo == True:
        bVal = map['a']
        map = {'b': bVal}
        assignments = input.split('\n')
        while(len(assignments) > 0):
            for assgn in assignments:
                if assgn.split(' ')[-1] == 'b':
                    assignments.pop(assignments.index(assgn))
                elif 'AND' in assgn:
                    if assgn.split(' ')[0].isnumeric():
                        if assgn.split(' ')[2].isnumeric():
                            map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) & int(assgn.split(' ')[2])
                            assignments.pop(assignments.index(assgn))
                        elif assgn.split(' ')[2] in map.keys():
                            map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) & map[assgn.split(' ')[2]]
                            assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[0] in map.keys():
                        if assgn.split(' ')[2].isnumeric():
                            map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] & int(assgn.split(' ')[2])
                            assignments.pop(assignments.index(assgn))
                        elif assgn.split(' ')[2] in map.keys():
                            map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] & map[assgn.split(' ')[2]]
                            assignments.pop(assignments.index(assgn))
                elif 'OR' in assgn:
                    if assgn.split(' ')[0].isnumeric():
                        if assgn.split(' ')[2].isnumeric():
                            map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) | int(assgn.split(' ')[2])
                            assignments.pop(assignments.index(assgn))
                        elif assgn.split(' ')[2] in map.keys():
                            map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) | map[assgn.split(' ')[2]]
                            assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[0] in map.keys():
                        if assgn.split(' ')[2].isnumeric():
                            map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] | int(assgn.split(' ')[2])
                            assignments.pop(assignments.index(assgn))
                        elif assgn.split(' ')[2] in map.keys():
                            map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] | map[assgn.split(' ')[2]]
                            assignments.pop(assignments.index(assgn))
                elif 'LSHIFT' in assgn:
                    if assgn.split(' ')[0].isnumeric():
                        map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) << int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[0] in map.keys():
                        map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] << int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                elif 'RSHIFT' in assgn:
                    if assgn.split(' ')[0].isnumeric():
                        map[assgn.split(' ')[4]] = int(assgn.split(' ')[0]) >> int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[0] in map.keys():
                        map[assgn.split(' ')[4]] = map[assgn.split(' ')[0]] >> int(assgn.split(' ')[2])
                        assignments.pop(assignments.index(assgn))
                elif 'NOT' in assgn:
                    if assgn.split(' ')[1].isnumeric():
                        map[assgn.split(' ')[3]] = ~int(assgn.split(' ')[1])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[1] in map.keys():
                        map[assgn.split(' ')[3]] = ~map[assgn.split(' ')[1]]
                        assignments.pop(assignments.index(assgn))
                else:
                    if assgn.split(' ')[0].isnumeric():
                        map[assgn.split(' ')[2]] = int(assgn.split(' ')[0])
                        assignments.pop(assignments.index(assgn))
                    elif assgn.split(' ')[0] in map.keys():
                        map[assgn.split(' ')[2]] = map[assgn.split(' ')[0]]
                        assignments.pop(assignments.index(assgn))
    return(map['a'])

findAValue(input)

# part 2
findAValue(input, partTwo = True)

