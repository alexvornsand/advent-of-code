# advent of code 2015
# day 5

import re

file = 'input.txt'

class String:
    def __init__(self, string):
        self.string = string
        self.vowels = len(re.findall('[aeiou]', self.string)) >= 3
        self.double = any([x == y for x, y in zip(self.string[:-1], self.string[1:])])
        self.exclusions = len(re.findall('(ab)|(cd)|(pq)|(xy)', string)) == 0
        self.nice_string = all([self.vowels, self.double, self.exclusions])
        self.double_double = any([len(re.findall('(' + self.string[i:i+2] + ')', self.string[i+2:])) >= 1 for i in range(len(self.string) - 2)])
        self.skip = any([x == y for x, y in zip(self.string[:-2], self.string[2:])])        
        self.nice_string_two = all([self.double_double, self.skip])

def part_1(strings):
    print('part 1:', sum([String(string).nice_string for string in strings]), sep = '\n')

def part_2(strings):
    print('part 2:', sum([String(string).nice_string_two for string in strings]), sep = '\n')

def main():
    strings = open(file, 'r').read().rstrip().split('\n')
    part_1(strings)
    part_2(strings)

if __name__ == '__main__':
    main()