# advent of code 2024
# day 15

file = 'input.txt'

class Warehouse:
    def __init__(self, grid, instructions, expand=False):
        self.grid = [[x for x in line] for line in grid.split('\n')]
        self.expand = expand
        if expand:
            expanded_grid = grid.replace('#', '##').replace('.', '..').replace('@', '@.').replace('O', '[]')
            self.grid = [[x for x in line] for line in expanded_grid.split('\n')]
        self.grid_dict = {}
        for j in range(len(self.grid)):
            for i in range(len(self.grid[j])):
                if self.grid[j][i] in ('O', '['):
                    self.grid_dict[(i, j)] = str(1000 * j + i)
                elif self.grid[j][i] == ']':
                    self.grid_dict[(i, j)] = str(1000 * j + i - 1)
                elif self.grid[j][i] == '@':
                    self.grid_dict[(i, j)] = '@'
                else:
                    self.grid_dict[(i, j)] = self.grid[j][i]
        self.instructions = [x for x in instructions.strip() if x != '\n']
        self.agents = {}
        for coord in self.grid_dict:
            if self.grid_dict[coord] in self.agents:
                self.agents[self.grid_dict[coord]].append(coord)
            else:
                self.agents[self.grid_dict[coord]] = [coord]

    def checkMovement(self, agent, instruction, log=False, depth=0):
        indent = '\t' * (depth + 1)
        if log:
            print(indent, 'checking mobility of ', agent, ' ', self.agents[agent] if agent not in ('#', '.') else '', sep='')
        if agent == '.':
            if log:
                print('\t', indent, 'open space -- doesn\'t move, but open', sep='')
            return True
        elif agent == '#':
            if log:
                print('\t', indent, 'wall -- doesn\'t move, but not open', sep='')
            return False
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)][['^', 'v', '<', '>'].index(instruction)]
        if all([self.grid_dict[(x + dx, y + dy)] == '.' for x, y in self.agents[agent]]):
            if log:
                print('\t', indent, 'all spots ', instruction, ' of ', agent, ' are open', sep='')
            return True
        else:
            if log:
                print('\t', indent, 'at least one spot ', instruction, ' of ', agent, ' is non-empty', sep='')
            clear = all([self.checkMovement(self.grid_dict[(x + dx, y + dy)], instruction, log=log, depth=depth + 1) for x, y in self.agents[agent] if self.grid_dict[(x + dx, y + dy)] != agent])
            if clear:
                if log:
                    print('\t', indent, 'all spots ', instruction, ' of ', agent, ' are open or mobile', sep='')
                return True
        
    def moveAgent(self, agent, instruction, log=False, depth=0):
        indent = '\t' * (depth + 1)
        dx, dy = [(0, -1), (0, 1), (-1, 0), (1, 0)][['^', 'v', '<', '>'].index(instruction)]
        self.agents[agent] = sorted(self.agents[agent], key=lambda x: x[0], reverse=instruction != '<')
        for x, y in self.agents[agent]:
            if log:
                print(indent, 'trying to move ', (x, y), ' of ', agent, ' to the ', instruction, sep='')
            if self.grid_dict[(x + dx, y + dy)] not in ('.', agent):
                if log:
                    print('\t', indent, 'first have to move blocker: ', self.grid_dict[(x + dx, y + dy)], ' at ', (x + dx, y + dy), sep='')
                self.moveAgent(self.grid_dict[(x + dx, y + dy)], instruction, log=log, depth=depth + 1)
            if log:
                print('\t', indent, 'populating ', (x + dx, y + dy), ' with ', agent, sep='')
                print('\t', indent, 'creating a vacuum at ', (x, y), ' where ', agent, ' had been', sep='')
            self.grid_dict[(x + dx, y + dy)] = agent
            self.grid_dict[(x, y)] = '.'
        self.agents[agent] = [(x + dx, y + dy) for x, y in self.agents[agent]]
    
    def printGrid(self, detailed=False):
        min_x = min([key[0] for key in self.grid_dict])
        max_x = max([key[0] for key in self.grid_dict])
        min_y = min([key[1] for key in self.grid_dict])        
        max_y = max([key[1] for key in self.grid_dict])
        if detailed:
            print('\n'.join([''.join([' ' + self.grid_dict[(i, j)].rjust(10, '.') for i in range(min_x, max_x + 1)]) for j in range(min_y, max_y + 1)]))
        else:
            box = '|' if self.expand else 'O'
            print('\n'.join([''.join([self.grid_dict[(i, j)] if len(self.grid_dict[(i, j)]) == 1 else box for i in range(min_x, max_x + 1)]) for j in range(min_y, max_y + 1)]))

    def performRoutine(self, log=False):
        if log:
            print('Initial state:')
            self.printGrid()
            print('\n')
        for instruction in self.instructions:
            if log:
                print('Move ', instruction, ':', sep='')
            if self.checkMovement('@', instruction, log):
                self.moveAgent('@', instruction, log)
            if log:
                self.printGrid()
                print('\n')

    def quantifyPositions(self):
        return sum([min([x for x, y in self.agents[agent]]) + 100 * min([y for x, y in self.agents[agent]]) for agent in self.agents if agent not in ('@', '#', '.')])
    
def part_1(grid, instructions):
    warehouse = Warehouse(grid, instructions)
    warehouse.performRoutine()
    print('Part 1:', warehouse.quantifyPositions())

def part_2(grid, instructions):
    warehouse = Warehouse(grid, instructions, True)
    warehouse.performRoutine()
    print('Part 2:', warehouse.quantifyPositions())

def main():
    grid, instructions = open(file, 'r').read().split('\n\n')
    part_1(grid, instructions)
    part_2(grid, instructions)

if __name__ == '__main__':
    main()