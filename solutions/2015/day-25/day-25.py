# advent of code 2015
# day 25

# part 1
import re

prompt = open('solutions/2015/day-25/input.txt', 'r').read()

def getCode(prompt):
    r, c = [int(x) for x in re.findall(r"\d+", prompt)]
    order = r + c - 1
    orderIndex = (order) * (order - 1) / 2 + 1
    targetIndex = orderIndex + c - 1
    i = 1
    v = 20151125
    while i < targetIndex:
        v = (v * 252533) % 33554393
        i += 1
    return(v)

getCode(prompt)