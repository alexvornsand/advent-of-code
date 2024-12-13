### [--- Day 6: Probably a Fire Hazard ---](https://adventofcode.com/2015/day/6)

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at `0,0`, `0,999`, `999,999`, and `999,0`. The instructions include whether to `turn on`, `turn off`, or `toggle` various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like `0,0 through 2,2` therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

- `turn on 0,0 through 999,999` would turn on (or leave on) every light.
- `toggle 0,0 through 999,0` would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
- `turn off 499,499 through 500,500` would turn off (or leave off) the middle four lights.

After following the instructions, **how many lights are lit**?

### --- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase `turn on` actually means that you should increase the brightness of those lights by `1`.

The phrase `turn off` actually means that you should decrease the brightness of those lights by `1`, to a minimum of zero.

The phrase `toggle` actually means that you should increase the brightness of those lights by `2`.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

- `turn on 0,0 through 0,0` would increase the total brightness by `1`.
- `toggle 0,0 through 999,999` would increase the total brightness by `2000000`.

### [--- Solution ---](day-06.py)
```Python
# advent of code 2015
# day 6

import re

file = 'input.txt'

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
```
