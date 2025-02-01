# advent of code 2018
# day 03

import re

file = 'solutions/2018/day-03/input.txt'

class Bolt:
    def __init__(self, cuts):
        self.cuts = {}
        for cut in cuts:
            id, x, y, width, length = re.search(r"#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)", cut).groups()
            self.cuts[id] = {'x': int(x), 'y': int(y), 'width': int(width), 'length': int(length)}
        self.fabric_in_use = {}

    def findOverlaps(self):
        for cut in self.cuts:
            for x in range(self.cuts[cut]['x'], self.cuts[cut]['x'] + self.cuts[cut]['width']):
                for y in range(self.cuts[cut]['y'], self.cuts[cut]['y'] + self.cuts[cut]['length']):
                    if (x, y) in self.fabric_in_use:
                        self.fabric_in_use[(x, y)].append(cut)
                    else:
                        self.fabric_in_use[(x, y)] = [cut]
        return sum([len(self.fabric_in_use[x]) > 1 for x in self.fabric_in_use])

    def findSingleton(self):
        cuts = list(self.cuts.keys()).copy()
        while cuts:
            cut_a = cuts.pop(0)
            for cut_b in self.cuts.keys():
                if cut_b != cut_a:
                    ax1 = self.cuts[cut_a]['x']
                    ax2 = self.cuts[cut_a]['x'] + self.cuts[cut_a]['width'] - 1
                    bx1 = self.cuts[cut_b]['x']
                    bx2 = self.cuts[cut_b]['x'] + self.cuts[cut_b]['width'] - 1
                    ay1 = self.cuts[cut_a]['y']
                    ay2 = self.cuts[cut_a]['y'] + self.cuts[cut_a]['length'] - 1
                    by1 = self.cuts[cut_b]['y']
                    by2 = self.cuts[cut_b]['y'] + self.cuts[cut_b]['length'] - 1
                    if (ax1 <= bx1 <= ax2 or bx1 <= ax1 <= bx2) and (ay1 <= by1 <= ay2 or by1 <= ay1 <= by2):
                        if cut_b in cuts:
                            cuts.remove(cut_b)
                        break
            else:
                return cut_a

def part_1(bolt):
    print('Part 1:', bolt.findOverlaps())

def part_2(bolt):
    print('Part 2:', bolt.findSingleton())

def main():
    cuts = open(file, 'r').read().splitlines()
    bolt = Bolt(cuts)
    part_1(bolt)
    part_2(bolt)

if __name__ == '__main__':
    main()