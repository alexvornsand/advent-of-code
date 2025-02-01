# advent of code 2020
# day 03

import numpy as np
import math

file = 'solutions/2020/day-03/input.txt'

class Forest:
    def __init__(self, map):
        self.forest = map
        self.routes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

    def countTrees(self, route_id=0):    
        dx, dy = self.routes[route_id]
        rows, cols = self.forest.shape
        steps = int(rows / dy)
        return sum([self.forest[dy * s, (dx * s) % cols] == '#' for s in range(steps)])

    def countAllTrees(self):
        return math.prod(self.countTrees(i) for i in range(len(self.routes)))

def part_1(forest):
    print('Part 1:', forest.countTrees())

def part_2(forest):
    print('Part 2:', forest.countAllTrees())

def main():
    map = np.array([[c for c in row] for row in open(file, 'r').read().splitlines()])
    forest = Forest(map)
    part_1(forest)
    part_2(forest)

if __name__ == '__main__':
    main()