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