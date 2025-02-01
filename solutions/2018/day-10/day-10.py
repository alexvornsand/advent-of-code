# advent of code 2018
# day 10

import numpy as np
import re

file = 'solutions/2018/day-10/input.txt'

class StarMap:
    def __init__(self, stars):
        self.stars = stars

    def positionsAtTime(self, time):
        return [(x + (dx * time), y + (dy * time)) for x, y, dx, dy in self.stars]

class StarMap:
    def __init__(self, stars):
        self.stars = stars

    def positionsAtTime(self, time):
        return [(x + (dx * time), y + (dy * time)) for x, y, dx, dy in self.stars]

    def printMap(self, positions):
        min_x = min([x for x, _ in positions])
        max_x = max([x for x, _ in positions])
        min_y = min([y for _, y in positions])
        max_y = max([y for _, y in positions])
        print('\n'.join([''.join(['#' if (x, y) in positions else ' ' for x in range(min_x, max_x + 1)]) for y in range(min_y, max_y + 1)]))

    def findMessage(self):
        x_stds = []
        y_stds = []
        time = 0
        while time < 100000:
            positions = self.positionsAtTime(time)
            x_stds.append(np.std([x for x, _ in positions]))
            y_stds.append(np.std([y for _, y in positions]))
            if time >= 2 and x_stds[-1] > min(x_stds) and y_stds[-1] > min(y_stds):
                self.alignment_time = time - 1
                self.printMap(self.positionsAtTime(time - 1))
                break
            else:
                time += 1

def part_1(starMap):
    print('Part 1:')
    starMap.findMessage()

def part_2(starMap):
    print('Part 2:', starMap.alignment_time)

def main():
    stars = [[int(x) for x in re.findall(r"-?\d+", star)] for star in open(file, 'r').read().splitlines()]
    starMap = StarMap(stars)
    part_1(starMap)
    part_2(starMap)

if __name__ == '__main__':
    main()

    