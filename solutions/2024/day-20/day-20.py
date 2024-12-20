# advent of code 2024
# day 20

file = 'input.txt'

class CPUMap:
    def __init__(self, grid):
        self.grid = grid
        self.original_grid = {(i, j): self.grid[j][i] for j in range(len(self.grid)) for i in range(len(self.grid[j]))}
        self.grid_dict = {(i, j): self.grid[j][i] for j in range(len(self.grid)) for i in range(len(self.grid[j]))}
        self.start = [(i, j) for j in range(len(self.grid)) for i in range(len(self.grid[j])) if self.grid[j][i] == 'S'][0]
        self.end = [(i, j) for j in range(len(self.grid)) for i in range(len(self.grid[j])) if self.grid[j][i] == 'E'][0]
        self.path_progress = []
        self.cheats = []

    def navigateMap(self):
        current_node = self.start
        self.grid_dict[current_node] = 0
        self.path_progress.append(current_node)
        while current_node != self.end:
            x, y = current_node
            neighbor = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if (x + dx, y + dy) in self.grid_dict and self.grid_dict[(x + dx, y + dy)] in ('.', 'E')][0]
            self.grid_dict[neighbor] = self.grid_dict[current_node] + 1
            current_node = neighbor
            self.path_progress.append(current_node)

    def findCheat(self, start_time, n=2, log=False):
        if log:
            print('looking for cheat at time', start_time, self.path_progress[start_time] )
        x, y = self.path_progress[start_time]
        if (x, y) == self.end:
            if log:
                print('\talready at the destination')
            return [((x, y), (x, y), 0)]
        min_x = max(0, x - n)
        max_x = min(x + n + 1, len(self.grid[x]))
        min_y = max(0, y - n)
        max_y = min(y + n + 1, len(self.grid))
        dest_times = [self.grid_dict[(dx, dy)] for dx in range(min_x, max_x) for dy in range (min_y, max_y) if self.grid_dict[(dx, dy)] != '#']
        valid_cheats = []
        for dest_time in dest_times:
            dx, dy = self.path_progress[dest_time]
            if log:
                print('\tcandidate destination time:', dest_time, self.path_progress[dest_time])
            if abs(dx - x) + abs(dy - y) > n:
                if log:
                    print('\t\tdestination not reachable')
            else:
                if log:
                    print('\t\tvalid destination time')
                valid_cheats.append(((x, y), (dx, dy), dest_time - start_time - (abs(dx - x) + abs(dy - y))))
        if len(valid_cheats) > 0:
            if log:
                print('\n'.join(['\t     ' + ' '.join([str(i) for i in range(min_x, max_x)]) ] + ['\t' + str(j).rjust(3, ' ') + '  ' + ' '.join(['@' if (x, y) == (i, j) else '+' if (i, j) in [self.grid_dict[cheat[1]] for cheat in valid_cheats] else '-' if self.grid_dict[(i, j)] != '#' and self.grid_dict[(i, j)] not in self.available_cheat_destinations else self.original_grid[(i, j)] for i in range(min_x, max_x)]) for j in range(min_y, max_y)]))
            return valid_cheats
        else:
            if log:
                print('\tno valid destinations')
                print('\n'.join(['\t     ' + ' '.join([str(i) for i in range(min_x, max_x)]) ] + ['\t' + str(j).rjust(3, ' ') + '  ' + ' '.join(['@' if (x, y) == (i, j) else '-' if self.grid_dict[(i, j)] != '#' and self.grid_dict[(i, j)] not in self.available_cheat_destinations else self.original_grid[(i, j)] for i in range(min_x, max_x)]) for j in range(min_y, max_y)]))
                print('')
            return []
            
    def countCheatSavings(self, s=100):
        if len(self.cheats) > 0:
            return sum([cheat[2] >= s for cheat in self.cheats])
    
    def findCheats(self, n=2, log=False):
        self.available_cheat_destinations = list(range(len(self.path_progress)))
        self.cheats = [cheat for t in range(len(self.path_progress)) for cheat in self.findCheat(t, n, log)]
        return self.countCheatSavings()

def part_1(cpuMap):
    print('Part 1:', cpuMap.findCheats())

def part_2(cpuMap):
    print('Part 2:', cpuMap.findCheats(n=20))

def main():
    grid = [[x for x in line] for line in open(file, 'r').read().splitlines()]    
    cpuMap = CPUMap(grid)
    cpuMap.navigateMap()
    part_1(cpuMap)
    part_2(cpuMap)

if __name__ == '__main__':
    main()