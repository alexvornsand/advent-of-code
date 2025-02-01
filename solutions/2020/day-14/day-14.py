# advent of code 2020
# day 14

from itertools import product

file = 'solutions/2020/day-14/test_1.txt'

class DockData:
    def __init__(self, instructions):
        self.instructions = instructions

    def maskBits(self, mask, number):
        return [int(''.join([m if m != 'X' else n for m, n in zip(mask, bin(number)[2:].rjust(32, '0'))]), 2)]
    
    def maskBitsV2(self, mask, number):
        answers = []
        replacements = product(['0', '1'], repeat=mask.count('X'))
        for q in replacements:
            q = list(q)
            masked_number = ''
            for m, n in zip(mask, bin(number)[2:].rjust(32, '0')):
                masked_number += '1' if m == 1 else n if m == 0 else q.pop()
            answers.append(int(masked_number, 2))
        return answers
    
    def maskData(self, version=1):
        self.memory = {}
        maskFunction = self.maskBits if version == 1 else self.maskBitsV2
        for op, val in self.instructions:
            if op == 'mask':
                mask = val
            else:
                self.memory[int(op[4:-1])] = maskFunction(mask, int(val))
        return sum([val for reg in self.memory for val in self.memory[reg]])
    
def part_1(dockData):
    print('Part 1:', dockData.maskData())
    print(dockData.memory)

def part_2(dockData):
    print('Part 2:', dockData.maskData(version=2))

def main():
    instructions = [line.split(' = ') for line in open(file, 'r').read().splitlines()]
    dockData = DockData(instructions)
    part_1(dockData)
    # part_2(dockData)

if __name__ == '__main__':
    main()  