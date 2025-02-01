# advent of code 2015
# day 07

from functools import cache

file = 'solutions/2015/day-07/input.txt'

class CircuitBoard:
    def __init__(self, instructions):
        self.nodes = {node: definition for definition, node in [instruction.split(' -> ') for instruction in instructions]}

    @cache
    def getCircuitValue(self, node, log=False, depth=0):
        indent = '\t' * depth
        if log:
            print(indent, 'assessing ', node, sep='')
        if node.isdigit():
            if log:
                print(indent, '\t', node, ' is an integer; returning ', node, sep='')
            return int(node)
        elif node in ['OR', 'AND', 'RSHIFT', 'LSHIFT', 'NOT']:
            if log:
                print(indent, '\t', node, ' is an operator; returning ', ['|', '&', '>>', '<<', '~'][['OR', 'AND', 'RSHIFT', 'LSHIFT', 'NOT'].index(node)], sep='')
            return ['|', '&', '>>', '<<', '~'][['OR', 'AND', 'RSHIFT', 'LSHIFT', 'NOT'].index(node)]
        elif self.nodes[node].isdigit():
            if log:
                print(indent, '\t', node, ' is an populated key; returning ', self.nodes[node], sep='')
            return self.getCircuitValue(self.nodes[node], log=log, depth=depth+1)
        else:
            if log:
                print(indent, '\t', node, ' is not a populated key(', self.nodes[node], '); iterating', sep='')
            args = self.nodes[node].split(' ')
            return eval(''.join([str(self.getCircuitValue(arg, log=log, depth=depth+1)) for arg in args]))
        
def part_1(circuitBoard):
    a = circuitBoard.getCircuitValue('a')
    print('Part 1:', a)
    return a

def part_2(adjustedCircuitBoard):
    print('Part 2:', adjustedCircuitBoard.getCircuitValue('a'))

def main():
    instructions = open(file, 'r').read().splitlines()
    circuitBoard = CircuitBoard(instructions)
    a = part_1(circuitBoard)
    adjustedCircuitBoard = CircuitBoard(instructions + [str(a) + ' -> b'])
    part_2(adjustedCircuitBoard)

if __name__ == '__main__':
    main()
