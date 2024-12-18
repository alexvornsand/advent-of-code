# advent of code 2024
# day 03

import re
import math

file = 'input.txt'

class Code:
    def __init__(self, code):
        self.code = code

    def countProds(self):
        return sum([math.prod(eval(segment)) for segment in re.findall(r'mul\((\d+\,\d+)\)', self.code)])
    
    def countActivatedProds(self):
        return sum([math.prod(eval(pair)) for segment in self.code.split('do') for pair in re.findall(r'mul(\(\d+,\d+\))', segment)  if segment[:2] == '()'])
    
def part_1(code):
    print('Part 1:', code.countProds())

def part_2(code):
    print('Part 2:', code.countActivatedProds())

def main():
    code = Code('do()' + open(file, 'r').read())
    part_1(code)
    part_2(code)

if __name__ == '__main__':
    main()
