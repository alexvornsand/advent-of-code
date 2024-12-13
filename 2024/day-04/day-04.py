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