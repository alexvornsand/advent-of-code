# advent of code 2024
# day 21

from functools import cache

file = 'input.txt'

class DoorControl:
    def __init__(self, sequences):
        self.sequences = sequences

    @cache
    def encodeStep(self, start, end, max_depth, recursion=0, log=False, depth=0):
        indent = '\t' * depth
        if log:
            print(indent, start, ' --> ', end, ' (depth ', depth, ')', sep='')
        if recursion == max_depth:
            if log:
                print(indent, '\tpunch number directly', sep='')
            return 1
        else:
            d_pad = start in ['^', '<', 'v', '>'] or end in ['^', '<', 'v', '>']
            if d_pad:
                coords = {
                    '<': (0, 1),
                    'v': (1, 1),
                    '>': (2, 1),
                    'X': (0, 0),
                    '^': (1, 0),
                    'A': (2, 0)
                }
                dead_spot = (0, 0)
            else:
                coords = {
                    'X': (0, 3),
                    '0': (1, 3),
                    'A': (2, 3),
                    '1': (0, 2),
                    '2': (1, 2),
                    '3': (2, 2),
                    '4': (0, 1),
                    '5': (1, 1),
                    '6': (2, 1),
                    '7': (0, 0),
                    '8': (1, 0),
                    '9': (2, 0)
                }            
                dead_spot = (0, 3)
            x, y = coords[start]
            i, j = coords[end]
            if start == end:
                return 1
            else:
                x_dir = '<' if i < x else '>'
                y_dir = '^' if j < y else 'v'
                options = []
                if (i, y) != dead_spot:
                    if log:
                        print(indent, 'option: ', x_dir * abs(i - x), y_dir * abs(j - y), 'A', sep='')
                    option = ['A'] + [x_dir] * abs(i - x) + [y_dir] * abs(j - y) + ['A']
                    options.append(sum([self.encodeStep(option[i], option[i +1], max_depth, recursion=recursion+1, log=log, depth=depth+1) for i in range(len(option) - 1)]))
                if (x, j) != dead_spot:
                    if log:
                        print(indent, 'option: ', y_dir * abs(j - y), x_dir * abs(i - x), 'A', sep='')
                    option = ['A'] + [y_dir] * abs(j - y) + [x_dir] * abs(i - x) + ['A']
                    options.append(sum([self.encodeStep(option[i], option[i + 1], max_depth, recursion=recursion+1, log=log, depth=depth+1) for i in range(len(option) - 1)]))
                if log:
                    print(indent, min(options), sep='')
                    print('\n')
                return min(options)
            
    def encodeSequence(self, seq, robots, log=False):
        if robots == 0:
            return len(seq)
        else:
            steps = [x for x in 'A' + seq]
            return sum([self.encodeStep(steps[i], steps[i + 1], max_depth=robots, log=log) for i in range(len(steps) - 1)])
        
    def calculateTotalComplexity(self, robots, log=False):
       return sum([int(seq[:-1]) * self.encodeSequence(seq, robots, log=log) for seq in self.sequences])

def part_1(doorControl):
    print('Part 1:', doorControl.calculateTotalComplexity(3))

def part_2(doorControl):
    print('Part 2:', doorControl.calculateTotalComplexity(26))

def main():
    sequences = open(file, 'r').read().splitlines()
    doorControl = DoorControl(sequences)
    part_1(doorControl)
    part_2(doorControl)

if __name__ == '__main__':
    main()