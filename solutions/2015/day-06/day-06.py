# advent of code 2015
# day 6

import re

file = 'solutions/2015/day-06/input.txt'

class LightGrid:
    def __init__(self):
        self.lights = {}
        self.brightness = {}

    def instructions(self, instr):
        dir, xmin, ymin, xmax, ymax = re.search('([a-z,\s]+)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)', instr).groups()
        if dir == 'turn on':
            for x in range(int(xmin), int(xmax) + 1):
                for y in range(int(ymin), int(ymax) + 1):
                    self.lights[(x, y)] = 1
                    if (x, y) in self.brightness.keys():
                        self.brightness[(x, y)] += 1
                    else:
                        self.brightness[(x, y)] = 1
        elif dir == 'turn off':
            for x in range(int(xmin), int(xmax) + 1):
                for y in range(int(ymin), int(ymax) + 1):
                    if (x, y) in self.lights.keys():
                        self.lights.pop((x, y))
                    if (x, y) in self.brightness.keys():
                        self.brightness[(x, y)] = max(0, self.brightness[(x, y)] - 1)
        else:
            for x in range(int(xmin), int(xmax) + 1):
                for y in range(int(ymin), int(ymax) + 1):
                    if (x, y) in self.lights.keys():
                        self.lights.pop((x, y))
                    else:
                        self.lights[(x, y)] = 1
                    if (x, y) in self.brightness.keys():
                         self.brightness[(x, y)] += 2
                    else:
                         self.brightness[(x, y)] = 2

    def countLights(self):
        return(sum(list(self.lights.values())))

    def countBrightness(self):
        return(sum(list(self.brightness.values())))
    
def main():
    instructions = open(file, 'r').read().rstrip().split('\n')
    grid = LightGrid()
    for instruction in instructions:
        grid.instructions(instruction)
    print('part 1:', grid.countLights(), sep = '\n')
    print('part 2:', grid.countBrightness(), sep = '\n')
    
if __name__ == '__main__':
    main()
