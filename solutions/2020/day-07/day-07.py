# advent of code 2020
# day 07

import re
from functools import cache

file = 'solutions/2020/day-07/input.txt'

class MatryoshkaBags:
    def __init__(self, bags):
        self.bags = bags

    @cache
    def checkForShinyGold(self, bag):
        if len(self.bags[bag]) == 0:
            return False
        elif 'shiny gold' in self.bags[bag]:
            return True
        else:
            return any(self.checkForShinyGold(child_bag) for child_bag in self.bags[bag])
        
    def countShinyGoldParents(self):
        return sum([self.checkForShinyGold(bag) for bag in self.bags])
    
    @cache
    def countBagContents(self, bag):
        if len(self.bags[bag]) == 0:
            return 1
        else:
            return 1 + sum([self.countBagContents(child_bag) * self.bags[bag][child_bag] for child_bag in self.bags[bag]])
        
def part_1(matryoshkaBags):
    print('Part 1:', matryoshkaBags.countShinyGoldParents())

def part_2(matryoshkaBags):
    print('Part 2:', matryoshkaBags.countBagContents('shiny gold'))

def main():
  bags = {bag: {sub_bag: int(num) for num, sub_bag in contents} for bag, contents in [[re.search(r"^(.*?)\sbags", line).groups()[0], re.findall(r"(\d+)\s(.*?)\sbags?", line)] for line in open(file, 'r').read().splitlines()]}
  matryoshkaBags = MatryoshkaBags(bags)
  part_1(matryoshkaBags)
  part_2(matryoshkaBags)

if __name__ == '__main__':
    main()