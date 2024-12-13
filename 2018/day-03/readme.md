### [--- Day 3: No Matter How You Slice It ---](https://adventofcode.com/2018/day/3)

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to **cut** the fabric.

The whole piece of fabric they're working on is a very large square - at least `1000` inches on each side.

Each Elf has made a **claim** about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

 - The number of inches between the left edge of the fabric and the left edge of the rectangle.
 - The number of inches between the top edge of the fabric and the top edge of the rectangle.
 - The width of the rectangle in inches.
 - The height of the rectangle in inches.

A claim like `#123 @ 3,2: 5x4` means that claim ID `123` specifies a rectangle `3` inches from the left edge, `2` inches from the top edge, `5` inches wide, and `4` inches tall. Visually, it claims the square inches of fabric represented by `#` (and ignores the square inches of fabric represented by `.`) in the diagram below:

```
...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........
```

The problem is that many of the claims **overlap**, causing two or more claims to cover part of the same areas. For example, consider the following claims:

```
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
```

Visually, these claim the following areas:

```
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
```

The four square inches marked with X are claimed by **both `1` and `2`**. (Claim `3`, while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough fabric. **How many square inches of fabric are within two or more claims?**

### --- Part Two ---

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim `3` is intact after all claims are made.

**What is the ID of the only claim that doesn't overlap?**

### [--- Solution ---](day-03.py)
```Python
# advent of code 2018
# day 3

import re

file = 'input.txt'

class Bolt:
    def __init__(self, cuts):
        self.cuts = {}
        for cut in cuts:
            id, x, y, width, length = re.search('#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', cut).groups()
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
```