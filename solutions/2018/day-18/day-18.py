# advent of code 2018
# day 18

file = 'solutions/2018/day-18/input.txt'

class ConwayForest:
    def __init__(self, forest_map):
        self.original_grid = {(x, y): forest_map[y][x] for y in range(len(forest_map)) for x in range(len(forest_map[y]))}
        self.grid = {(x, y): forest_map[y][x] for y in range(len(forest_map)) for x in range(len(forest_map[y]))}
        self.grid_history = {0: self.grid}

    def evolveTile(self, tile):
        x, y = tile
        neighbors = [self.grid[(x + dx, y + dy)] for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0) and (x + dx, y + dy) in self.grid]
        if self.grid[tile] == '.' and neighbors.count('|') >= 3:
            return '|'
        elif self.grid[tile] == '|' and neighbors.count('#') >= 3:
            return '#'
        elif self.grid[tile] == '#' and (neighbors.count('#') == 0 or neighbors.count('|') == 0):
            return '.' 
        else:
            return self.grid[tile]
        
    def printGrid(self, buffer=0, label_frequency=None):
        if isinstance(buffer, int):
            buffer = [buffer] * 4
        x_min = min([x for x, _ in self.grid]) - buffer[0]
        x_max = max([x for x, _ in self.grid]) + buffer[1] + 1
        y_min = min([y for _, y in self.grid]) - buffer[2]
        y_max = max([y for _, y in self.grid]) + buffer[3] + 1
        if label_frequency:
            for d in range(max(len(str(x_max)), len(str(x_min)))):
                print(' ' * (len(str(y_max)) + 1) + ''.join([(str(x).rjust(max(len(str(x_max)), len(str(x_min))), ' '))[d] if x % label_frequency == 0 else ' ' for x in range(x_min, x_max)]))
        print('\n'.join([('' if label_frequency is None else str(y).rjust(len(str(y_max)), ' ') if y % label_frequency == 0 else ' ' * len(str(y_max))) + ' ' + ''.join([self.grid[(x, y)] if (x, y) in self.grid else '.' for x in range(x_min, x_max)]) for y in range(y_min, y_max)]))

    def simulateMinute(self):
        self.grid = {tile: self.evolveTile(tile) for tile in self.grid}

    def simulateMinutes(self, minutes, log=False):
        self.grid = {key: value for key, value in self.original_grid.items()}
        self.grid_history = {0: self.grid}
        if log:
            print('Initial State:')
            self.printGrid()
            print('')
        for t in range(1, minutes + 1):
            if self.grid in list(self.grid_history.values())[:-1]:
                repetition_start = min([key for key in self.grid_history if self.grid_history[key] == self.grid])
                repetition_length = t - 1 - repetition_start
                break
            else:
                self.simulateMinute()
                self.grid_history[t] = self.grid
                if log:
                    print('After', t, 'minute(s):')
                    self.printGrid()
                    print('')
        else:
            return list(self.grid.values()).count('#') * list(self.grid.values()).count('|')
        self.grid = self.grid_history[repetition_start + ((minutes - repetition_start) % repetition_length)]
        return list(self.grid.values()).count('#') * list(self.grid.values()).count('|')

def part_1(conwayForest):
    print('Part 1:', conwayForest.simulateMinutes(10))

def part_2(conwayForest):
    print('Part 2:', conwayForest.simulateMinutes(1000000000))

def main():
    forest_map = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    conwayForest = ConwayForest(forest_map)
    part_1(conwayForest)
    part_2(conwayForest)

if __name__ == '__main__':
    main()