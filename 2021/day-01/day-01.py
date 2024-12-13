# advent of code
# day 1

# part 1
numbers = [int(x) for x in open('day-01.txt', 'r').read().split('\n')[:-1]]


def countIncreases(numbers, partTwo=False):
    if(partTwo is False):
        print(sum([i2 > i1 for i2, i1 in zip(numbers[1:], numbers[:-1])]))
    else:
        print(sum([i2 > i1 for i2, i1 in zip(numbers[3:], numbers[:-3])]))


countIncreases(numbers)

# part 2
countIncreases(numbers, partTwo=True)
