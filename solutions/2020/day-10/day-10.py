# advent of code 2020
# day 10

from functools import cache

file = 'solutions/2020/day-10/input.txt'

class JoltChain:
    def __init__(self, adapters):
        self.adapters = sorted(adapters)
        self.largest_adapter = max(adapters)

    def describeDistribution(self):
        adapters = [0] + self.adapters + [self.largest_adapter + 3]
        changes = [adapters[i + 1] - adapters[i] for i in range(len(adapters) - 1)]
        return changes.count(1) * changes.count(3)
    
    @cache
    def findAllChains(self, joltage=0, remaining_adapters=None, log=False, depth=0):
        indent = '\t' * depth
        if remaining_adapters is None:
            remaining_adapters = tuple(self.adapters)
        if joltage == self.largest_adapter:
            if log:
                print(indent, ' reached the desired joltage', sep='')
            return 1
        else:
            next_adapter_options = [adapter for adapter in remaining_adapters if 1 <= adapter - joltage <= 3]
            if log:
                print(indent, ' joltage is at ', joltage, ' with ', remaining_adapters, ' left in the bag', sep='')
                print(indent, ' available next steps are ', next_adapter_options, sep='')
            return sum([self.findAllChains(joltage=next_adapter, remaining_adapters=tuple([adapter for adapter in remaining_adapters if adapter > next_adapter]), log=log, depth=depth+1) for next_adapter in next_adapter_options])        

def part_1(joltChain):
    print('Part 1:', joltChain.describeDistribution())

def part_2(joltChain):
    print('Part 2:', joltChain.findAllChains())

def main():
    adapters = [int(x) for x in open(file, 'r').read().splitlines()]
    joltChain = JoltChain(adapters)
    part_1(joltChain)
    part_2(joltChain)

if __name__ == '__main__':
    main()