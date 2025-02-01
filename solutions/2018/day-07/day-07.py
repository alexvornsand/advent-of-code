# advent of code 2018
# day 07

import re
import networkx as nx

file = 'solutions/2018/day-07/input.txt'

class Manual:
    def __init__(self, instructions):
        self.instructions = instructions
        self.g = nx.DiGraph()
        self.g.add_edges_from(instructions)

    def followInstructions(self, agents=1, delay=0, log=False):
        g = self.g.copy()
        string = ''
        slots = [None] * agents
        time_remaining = [None] * agents
        time = 0
        while len(g) > 0:
            unblocked_instructions = sorted([node for node in self.g if g.in_degree(node) == 0 and node not in slots])
            if log:
                print('time ', time, sep='')
                print('\tworkers: ', [slot if slot is not None else 'No Job' + ' (' + str(time if time is not None else '-') + ')' for slot, time in zip(slots, time_remaining)], sep='')
                print('\tavailable jobs: ', unblocked_instructions, sep='')
            for i in range(agents):
                if slots[i] is None and len(unblocked_instructions) > 0:
                    slots[i] = unblocked_instructions.pop(0)
                    time_remaining[i] = delay + ord(slots[i]) - 64
                    if log:
                       print('\t\tworker ', i, ' is assigned ', slots[i], ' (', str(time_remaining[i]), ')', sep='')
            time_advance = min([time for time in time_remaining if time is not None])
            time_remaining = [time - time_advance if time is not None else None for time in time_remaining]
            time += time_advance
            for i in range(agents):
                if time_remaining[i] == 0:
                    g.remove_node(slots[i])
                    string += slots[i]
                    time_remaining[i] = None
                    slots[i] = None
        return string, time
    
def part_1(manual):
    print('Part 1:', manual.followInstructions()[0])

def part_2(manual):
    print('Part 2:', manual.followInstructions(agents=5, delay=60)[1])

def main():
    instructions = [re.findall('[A-Z]', x)[1:] for x in open(file, 'r').read().splitlines()]
    manual = Manual(instructions)
    part_1(manual)
    part_2(manual)

if __name__ == '__main__':
    main()
