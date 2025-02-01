# advent of code 2015
# day 24

# part 1
import operator
import itertools
import functools

input = open('solutions/2015/day-24/input.txt', 'r').read()

def arrangePackages(input, partTwo = False):
    nums = [int(x) for x in input.split('\n')]
    if partTwo == False:
        parts = 3
    else:
        parts = 4
    tot = sum(nums) / parts
    def hasSum(lst, sub):
        for y in range(1,len(lst)):
            for x in (z for z in itertools.combinations(lst, y) if sum(z) == tot):
                if sub == 2:
                    return True
                elif sub < parts:
                    return hasSum(list(set(lst) - set(x)), sub - 1)
                elif hasSum(list(set(lst) - set(x)), sub - 1):
                    return(functools.reduce(operator.mul, x, 1))
    return(hasSum(nums, parts))

print(arrangePackages(input))

# part 2
print(arrangePackages(input, partTwo = True))
