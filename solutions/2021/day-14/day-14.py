# advent of code
# day 14

# part 1
template = open('day-14.txt', 'r').read().split('\n\n')[0]
insertions = open('day-14.txt', 'r').read().split('\n\n')[1].split('\n')[:-1]


def buildPolymer(template, insertions, partTwo=False):
    if partTwo is True:
        n = 40
    else:
        n = 10
    insertionsDict = dict([(insertion.split(
        ' -> ')[0], insertion.split(' -> ')[1]) for insertion in insertions])
    counterDict = dict([(key, 0) for key in insertionsDict])
    for i in range(1, len(template)):
        counterDict[template[i - 1] + template[i]] += 1
    for i in range(n):
        newCounterDict = dict([(key, 0) for key in counterDict])
        for pair in counterDict:
            front = pair[0] + insertionsDict[pair]
            back = insertionsDict[pair] + pair[1]
            newCounterDict[front] += counterDict[pair]
            newCounterDict[back] += counterDict[pair]
        counterDict = newCounterDict
    elements = dict([(element, 0) for element in list(
        set([e for pair in counterDict for e in pair]))])
    for pair in counterDict:
        elements[pair[0]] += counterDict[pair]
        elements[pair[1]] += counterDict[pair]
    elements[template[0]] += 1
    elements[template[len(template) - 1]] += 1
    for element in elements:
        elements[element] = elements[element] / 2
    print(max(elements.values()) - min(elements.values()))


buildPolymer(template, insertions)

# part 2
buildPolymer(template, insertions, partTwo=True)
