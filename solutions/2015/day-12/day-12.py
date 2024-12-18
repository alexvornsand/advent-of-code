# advent of code 2015
# day 12

# part 1
import json

input = open('day-12.txt', 'r').read()

def sumNumbers(input, partTwo = False):
    def getNumbersFromObj(obj):
        if type(obj) == dict:
            if partTwo == False or 'red' not in obj.values():
                return(sum([getNumbersFromObj(obj[x]) for x in obj.keys()]))
            else:
                return(0)
        elif type(obj) == list:
            return(sum([getNumbersFromObj(x) for x in obj]))
        elif type(obj) == int:
            return(obj)
        else:
            return(0)
    return(getNumbersFromObj(json.loads(input)))

sumNumbers(input)

# part 2
sumNumbers(input, partTwo = True)
