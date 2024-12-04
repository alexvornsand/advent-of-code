### [--- Day 4: Ceres Search ---](https://adventofcode.com/2024/day/4)

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the [Ceres monitoring station](https://adventofcode.com/2019/day/10)!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her **word search** (your puzzle input). She only has to find one word: `XMAS`.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of `XMAS` - **you need to find all of them**. Here are a few ways `XMAS` might appear, where irrelevant characters have been replaced with `.`:

```
..X...
.SAMX.
.A..A.
XMAS.S
.X....
```

The actual word search will be full of letters instead. For example:

```
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
```

In this word search, `XMAS` occurs a total of **`18`** times; here's the same word search again, but where letters not involved in any `XMAS` have been replaced with `.`:

```
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
```

Take a look at the little Elf's word search. **How many times does `XMAS` appear?**

### --- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an **`XMAS`** puzzle; it's an **`X-MAS`** puzzle in which you're supposed to find two `MAS` in the shape of an `X`. One way to achieve that is like this:

```
M.S
.A.
M.S
```

Irrelevant characters have again been replaced with `.` in the above diagram. Within the `X`, each `MAS` can be written forwards or backwards.

Here's the same example from before, but this time all of the `X-MAS`es have been kept instead:

```
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
```

In this example, an `X-MAS` appears **`9`** times.

Flip the word search from the instructions back over to the word search side and try again. **How many times does an X-MAS appear?**

### [--- Solution ---](day-04.py)
```Python
# advent of code 2024
# day 4

import itertools

file = 'input.txt'

class XMASGrid:
    def __init__(self, grid):
        self.grid = grid
        self.grid_dict = {(i, j): grid[j][i] for j in range(len(grid)) for i in range(len(grid[j]))}

    def findXMAS(self, coord):
        xmas = 0
        x, y = coord
        xdirs = [0]
        ydirs = [0]
        if x >= 3:
            xdirs.append(-1)
        if x <= len(self.grid[0]) - 4:
            xdirs.append(1)
        if y >= 3:
            ydirs.append(-1)
        if y <= len(self.grid) - 4:
            ydirs.append(1)
        shifts = list(itertools.product(xdirs, ydirs))
        shifts.remove((0, 0))
        for shift in shifts:
            for i in range(3):
                if self.grid_dict[(coord[0] + (shift[0] * (i + 1)), coord[1] + (shift[1] * (i + 1)))] != 'XMAS'[i + 1]:
                    break
            else:
                xmas += 1
        return xmas

    def countXMAS(self):
        XStarts = [key for key in self.grid_dict.keys() if self.grid_dict[key] == 'X']
        return sum([self.findXMAS(start) for start in XStarts])

    def findX_MAS(self, coord):
        x, y = coord
        if x >= 1 and x <= len(self.grid[0]) - 2 and y >= 1 and y <= len(self.grid) - 2:
            if (
                self.grid_dict[(x - 1, y - 1)] + 'A' + self.grid_dict[(x + 1, y + 1)] in ('MAS', 'SAM') 
                and self.grid_dict[(x - 1, y + 1)] + 'A' + self.grid_dict[(x + 1, y - 1)] in ('MAS', 'SAM')):
                return True
        return False

    def countX_MAS(self):
        AStarts = [key for key in self.grid_dict.keys() if self.grid_dict[key] == 'A']
        return sum([self.findX_MAS(start) for start in AStarts])
    
def part_1(grid):
    print('Part 1:', grid.countXMAS())

def part_2(grid):
    print('Part 2:', grid.countX_MAS())

def main():
    grid = XMASGrid([[char for char in line] for line in open(file, 'r').read().splitlines()])
    part_1(grid)
    part_2(grid)

if __name__ == '__main__':
    main()
```