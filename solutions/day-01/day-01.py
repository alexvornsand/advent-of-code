# advent of code 2024
# day 01

import re

file = 'input.txt'

class PairedLists:
    def __init__(self, lists):
        self.lists = lists
        self.list_a = sorted([x for x, y in lists])
        self.list_b = sorted([y for x, y in lists])

    def cumAbsDiff(self):
        return sum([abs(y - x) for x, y in zip(self.list_a, self.list_b)])
    
    def weightedSum(self):
        return sum([x * self.list_b.count(x) for x in self.list_a])

def part_1(pairedLists):
    print('Part 1:', pairedLists.cumAbsDiff())

def part_2(pairedLists):
    print('Part 2:', pairedLists.weightedSum())

def main():
    lists = [[int(x) for x in re.search('(\d+)\s+(\d+)', line).groups()] for line in open(file, 'r').read().splitlines()]
    pairedLists = PairedLists(lists)
    part_1(pairedLists)
    part_2(pairedLists)

if __name__ == '__main__':
    main()
