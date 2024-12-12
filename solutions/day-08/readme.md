### [--- Day 8: Resonant Collinearity ---](https://adventofcode.com/2024/day/8)

You find yourselves on the [roof](https://adventofcode.com/2016/day/25) of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar **huge antenna**. Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific **frequency** indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

```
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
```

The signal only applies its nefarious effect at specific **antinodes** based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

So, for these two antennas with frequency `a`, they create the two antinodes marked with `#`:

```
..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........
```

Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, but two are off the right side of the map, so instead it adds only two:

```
..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........
```

Antennas with different frequencies don't create antinodes; `A` and `a` count as different frequencies. However, antinodes **can** occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital `A` creates no antinodes but has a lowercase-`a`-frequency antinode at its location:

```
..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........
```

The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an antinode overlapping the topmost `A`-frequency antenna:

```
......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
```

Because the topmost `A`-frequency antenna overlaps with a `0`-frequency antinode, there are **`14`** total unique locations that contain an antinode within the bounds of the map.

Calculate the impact of the signal. **How many unique locations within the bounds of the map contain an antinode?**

### --- Part Two ---

Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at **any grid position** exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three `T`-frequency antennas now create many antinodes:

```
T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
```

In fact, the three `T`-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to **`9`**.

The original example now has **`34`** antinodes, including the antinodes that appear on every antenna:

```
##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
```

Calculate the impact of the signal using this updated model. **How many unique locations within the bounds of the map contain an antinode?**

### [--- Solution ---](day-08.py)
```Python
# advent of code 2024
# day 08

file = 'input.txt'

class SignalMap:
    def __init__(self, grid):
        self.grid = grid
        self.grid_dict = {(i, j): self.grid[j][i] for j in range(len(self.grid)) for i in range(len(self.grid[j]))}
        self.grid_values = {'.': []}
        for j in range(len(self.grid)):
            for i in range(len(grid[j])):
                self.grid_values['.'].append((i, j))
                if grid[j][i] != '.':
                    if grid[j][i] in self.grid_values:
                        self.grid_values[grid[j][i]].append((i, j))
                    else:
                        self.grid_values[grid[j][i]] = [(i, j)]
        self.frequencies = [val for val in self.grid_values if val != '.']

    def printMap(self, md):
        minX = min([key[0] for key in md.keys()])
        maxX = max([key[0] for key in md.keys()])
        minY = min([key[1] for key in md.keys()])
        maxY = max([key[1] for key in md.keys()])
        print('\n'.join([''.join([md[(i, j)] for i in range(minX, maxX + 1)]) for j in range(minY, maxY + 1)]))

    def testSpace(self, space, antinodes=False):
        x, y = space
        for frequency in self.frequencies:
            for i in self.grid_values[frequency]:
                if antinodes and space == i:
                    self.grid_dict[(x, y)] = '#'
                    return True
                for j in self.grid_values[frequency]:
                    if antinodes and space == j:
                        self.grid_dict[(x, y)] = '#'
                        return True
                    if i != j:
                        if antinodes:
                            if (x == i[0] and x == j[0]) and (y == i[1] and y == j[1]):
                                self.grid_dict[(x, y)] = '#'
                                return True
                            elif (y == i[1] or y == j[1]):
                                pass
                            elif (x == i[0] or x == j[0]):
                                pass
                            else:                            
                                if (i[0] - x) / (j[0] - x) == (i[1] - y) / (j[1] - y):
                                    self.grid_dict[(x, y)] = '#'
                                    return True
                        else:
                            if i[0] - x == 2 * (j[0] - x) and i[1] - y == 2 * (j[1] - y):
                                self.grid_dict[(x, y)] = '#'
                                return True
        return False
    
    def countNodes(self, antinodes=False):
        return sum([self.testSpace(space, antinodes) for space in self.grid_values['.']])

def part_1(signalMap):
    print('Part 1:', signalMap.countNodes())

def part_2(signalMap):
    print('Part 2:', signalMap.countNodes(True))

def main():
    grid = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    signalMap = SignalMap(grid)
    part_1(signalMap)
    part_2(signalMap)

if __name__ == '__main__':
    main()
```