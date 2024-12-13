# advent of code 2024
# day 13

import re

file = 'input.txt'

class Machines:
    def __init__(self, configs):
        self.configs = configs

    def solveSystem(self, equation, adjust=False):
        x1, y1, x2, y2, xt, yt = equation
        if adjust:
            xt += 10000000000000
            yt += 10000000000000
        a = (yt * x2 - y2 * xt) / (x2 * y1 - y2 * x1)
        b = (xt - x1 * a) / x2
        cost = 3 * a + b
        if int(cost) == cost:
            return int(cost)
        return 0
    
    def findTotalCost(self, adjust=False):
        return sum([self.solveSystem(equation, adjust) for equation in self.configs])
    
def part_1(machines):
    print('Part 1:', machines.findTotalCost())

def part_2(machines):
    print('Part 2:', machines.findTotalCost(True))

def main():
    machine_configs = [[int(x) for x in re.findall('\d+', line)] for line in open(file, 'r').read().split('\n\n')]
    machines = Machines(machine_configs)
    part_1(machines)
    part_2(machines)

if __name__ == '__main__':
    main()