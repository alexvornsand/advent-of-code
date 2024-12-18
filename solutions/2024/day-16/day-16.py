# advent of code 2024
# day 16

file = 'input.txt'

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.grid_dict = {(i, j): '#' if self.grid[j][i] == '#' else '.' for j in range(len(self.grid)) for i in range(len(self.grid[j]))}
        self.node_distances = {}
        self.goodSeats = set()

    def navigateMaze(self):
        current_node = (1, len(self.grid) - 2, 1, 0)
        terminal_node = (len(self.grid[0]) - 2, 1)
        self.node_distances = {(x, y, dx, dy): 999999 for x, y in self.grid_dict for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if self.grid_dict[(x, y)] == '.'}
        self.node_distances[current_node] = 0
        unvisited_nodes = [key for key in self.node_distances]
        queue = [current_node]
        while len(queue) > 0:
            queue = sorted(queue, key=lambda x: self.node_distances[x])
            x, y, dx, dy = queue.pop(0)
            neighbors = [(x + dx, y + dy, dx, dy)] + [(x, y, ndx, ndy) for ndx, ndy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if abs(ndx - dx) == 1]
            for neighbor in neighbors:
                movement_cost = self.node_distances[(x, y, dx, dy)]
                nx, ny, ndx, ndy = neighbor
                if neighbor in unvisited_nodes:
                    if dx != ndx:
                        movement_cost += 1000
                    else:
                        movement_cost += 1
                    self.node_distances[neighbor] = min([self.node_distances[neighbor], movement_cost])
                    if neighbor not in queue:
                        queue.append(neighbor)
            unvisited_nodes.remove((x, y, dx, dy))
        self.min_distances = min([self.node_distances[node] for node in self.node_distances if node[0] == terminal_node[0] and node[1] == terminal_node[1]])
        return self.min_distances

    def countGoodSeats(self, log=False):
        self.goodSeats.add((len(self.grid) - 2, 1))
        for term in self.node_distances.keys():
            if term[0] == len(self.grid) - 2 and term[1] == 1 and self.node_distances[term] == self.min_distances:
                self.traceReturnPaths(term, log)
        return len(self.goodSeats)

    def traceReturnPaths(self, node, log=False, depth=0):
        indent = '\t' * depth
        if log:
            print(indent, 'at node ', node, ' (', self.node_distances[node], ')', sep='')
        x, y, dx, dy = node
        if node == (1, len(self.grid) - 2, 1, 0):
            if log:
                print(indent, '\treached the starting point!')
            return True
        else:
            neighbors = [(x - dx, y - dy, dx, dy)] + [(x, y, ndx, ndy) for ndx, ndy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if abs(ndx - dx) == 1]
            if log:
                print(indent, '\tneighbors: ', neighbors, sep='')
            neighbors_on_path = []
            for neighbor in neighbors:
                if log:
                    print(indent, '\t\tchecking neighbor ', neighbor, ' (', self.node_distances[neighbor] if neighbor in self.node_distances else ' X ', ')', sep='')
                nx, ny, ndx, ndy = neighbor
                delta = 1000 if abs(ndx - dx) == 1 else 1
                if neighbor in self.node_distances and self.node_distances[node] - self.node_distances[neighbor] == delta:
                    if log:
                        print(indent, '\t\t\tneighbor on the path!!!', sep='')
                    self.goodSeats.add((nx, ny))
                    neighbors_on_path.append(neighbor)
            return any([self.traceReturnPaths(neighbor, log, depth=depth + 1) for neighbor in neighbors_on_path])
        
    def printPaths(self):
        min_x = min([key[0] for key in self.grid_dict])
        max_x = max([key[0] for key in self.grid_dict])
        min_y = min([key[1] for key in self.grid_dict])        
        max_y = max([key[1] for key in self.grid_dict])
        print('\n'.join([''.join([self.grid_dict[(i, j)] if (i, j) not in self.goodSeats else 'O' for i in range(min_x, max_x + 1)]) for j in range(min_y, max_y + 1)]))

def part_1(maze):
    print('Part 1:', maze.min_distances)

def part_2(maze):
    print('Part 2:', maze.countGoodSeats())

def main():
    grid = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    maze = Maze(grid)
    maze.navigateMaze()
    part_1(maze)
    part_2(maze)

if __name__ == '__main__':
    main()