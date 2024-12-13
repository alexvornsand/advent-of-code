### [--- Day 3: Spiral Memory ---](https://adventofcode.com/2017/day/3)

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked `1` and then counting up while spiraling outward. For example, the first few squares are allocated like this:

```
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
```

While this is very space-efficient (no squares are skipped), requested data must be carried back to square `1` (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the [Manhattan Distance](https://en.wikipedia.org/wiki/Taxicab_geometry) between the location of the data and square `1`.

For example:

 - Data from square `1` is carried `0` steps, since it's at the access port.
 - Data from square `12` is carried `3` steps, such as: down, left, left.
 - Data from square `23` is carried only `2` steps: up twice.
 - Data from square `1024` must be carried `31` steps.

**How many steps** are required to carry the data from the square identified in your puzzle input all the way to the access port?

### --- Part Two ---

As a stress test on the system, the programs here clear the grid and then store the value `1` in square `1`. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

 - Square `1` starts with the value `1`.
 - Square `2` has only one adjacent filled square (with value `1`), so it also stores `1`.
 - Square `3` has both of the above squares as neighbors and stores the sum of their values, `2`.
 - Square `4` has all three of the aforementioned squares as neighbors and stores the sum of their values, `4`.
 - Square `5` only has the first and fourth squares as neighbors, so it gets the value `5`.

Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

```
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
```

What is the **first value written** that is **larger** than your puzzle input?

### [--- Solution ---](day-03.py)

```Python
# advent of code 2017
# day 3

file = 'input.txt'

class Spiral:
    def __init__(self, terminus):
        self.terminus = terminus
        self.spiral = {}

    def neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x + 1, y + 1)]
        return [neighbor for neighbor in neighbors if neighbor in self.spiral]
    
    def populateStep(self, coord):
        neighbors = self.neighbors(coord)
        self.spiral[coord] = sum([self.spiral[neighbor] for neighbor in neighbors])

    def findNextStep(self, coord):
        x, y = coord
        if y >= 0 and x <= y and abs(x) <= y:
            x += 1
        elif y < 0 and x > y and x <= abs(y):
            x -= 1
        elif x >= 0 and x > y:
            y -= 1
        elif x < 0 and x <= y:
            y += 1
        return (x, y)
    
    def printSpiral(self):
        x_max = max([key[0] for key in self.spiral.keys()])
        x_min = min([key[0] for key in self.spiral.keys()])
        y_max = max([key[1] for key in self.spiral.keys()])
        y_min = min([key[1] for key in self.spiral.keys()])
        image = ''
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if (x, y) in self.spiral:
                    image += str(self.spiral[(x, y)]).rjust(8, ' ')
                else:
                    image += ' ' * 8
            image += '\n\n'
        print(image)
    
    def fillSpiral(self):
        coord = (0, 0)
        self.spiral[coord] = 1
        while max(self.spiral.values()) < self.terminus:
            coord = self.findNextStep(coord)
            self.populateStep(coord)
        return self.spiral[coord]
    
class DataPoint:
    def __init__(self, point):
        self.point = point

    def calculateDistance(self):
        self.ring = int(-(-(self.point)**(1/2)//1)//2)
        self.carryover = self.point - (self.ring * 2 - 1)**2
        self.segments = self.carryover // (2 * self.ring) if self.ring != 0 else 0
        self.shift = abs(self.carryover - self.ring * (2 * self.segments + 1))
        self.manhattan_distance = self.shift + self.ring
        return self.manhattan_distance

def part_1(dataPoint):
    print('Part 1:', dataPoint.calculateDistance())

def part_2(spiral):
    print('Part 2:', spiral.fillSpiral())

def main():
    dataPoint = DataPoint(265149)
    spiral = Spiral(265149)
    part_1(dataPoint)
    part_2(spiral)

if __name__ == '__main__':
    main()
```