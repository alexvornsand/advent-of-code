# advent of code
# day 10

# part 1
import statistics
syntaxes = open('day-10.txt', 'r').read().split('\n')[:-1]


def debugSyntax(syntaxes, partTwo=False):
    def removePairs(syntax):
        newSyntax = syntax.replace('()', '')
        newSyntax = newSyntax.replace('[]', '')
        newSyntax = newSyntax.replace('{}', '')
        newSyntax = newSyntax.replace('<>', '')
        if newSyntax == syntax:
            return(syntax)
        else:
            return(removePairs(newSyntax))
    corruptionValues = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corruptedLines = []
    incompleteLines = []
    for syntax in syntaxes:
        simplifiedSyntax = removePairs(syntax)
        if any([sym in corruptionValues for sym in simplifiedSyntax]):
            corruptedLines.append(simplifiedSyntax)
        else:
            incompleteLines.append(simplifiedSyntax)
    if partTwo is False:
        firstBreak = [[sym for sym in syntax if sym in corruptionValues][0]
                      for syntax in corruptedLines]
        print(sum([corruptionValues[sym] * firstBreak.count(sym)
              for sym in corruptionValues]))
    else:
        def calculateScore(syntax):
            completionValues = {')': 1, ']': 2, '}': 3, '>': 4}
            partners = {'(': ')', '[': ']', '{': '}', '<': '>'}
            complements = [partners[sym] for sym in syntax][::-1]
            x = 0
            for sym in complements:
                x = x * 5 + completionValues[sym]
            return(x)
        print(statistics.median([calculateScore(syntax)
              for syntax in incompleteLines]))


debugSyntax(syntaxes)

# part 2
debugSyntax(syntaxes, partTwo=True)
