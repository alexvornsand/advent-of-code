# advent of code 2024
# day 18

file = 'input.txt'

class MemoryMap:
    def __init__(self, bytes, size=71):
        self.bytes = bytes
        self.obstacles = []
        self.grid_dict = {}
        self.node_distances = {}
        self.size = size

    def navigateMap(self, start=1024):
        self.obstacles = self.bytes[:start]
        self.grid_dict = {(i, j): '#' if (i, j) in self.obstacles else '.' for i in range(self.size) for j in range(self.size)}
        unvisited_nodes = [key for key in self.grid_dict.keys() if self.grid_dict[key] == '.']
        queue = [(0,0)]
        self.node_distances = {node: 999999 for node in unvisited_nodes}
        self.node_distances[(0,0)] = 0
        while len(queue) > 0:
            x, y = queue.pop(0)
            if (x, y) == (self.size - 1, self.size - 1):
                return self.node_distances[(x, y)]
            neighbors = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] if (x + dx, y + dy) in unvisited_nodes]
            for neighbor in neighbors:
                self.node_distances[neighbor] = min(self.node_distances[neighbor], self.node_distances[(x, y)] + 1)
                if neighbor not in queue:
                    queue.append(neighbor)
            unvisited_nodes.remove((x, y))

    def printMap(self, t):
        dict_at_t = {(i, j): '#' if (i, j) in self.bytes[:t] else '.' for i in range(self.size) for j in range(self.size)}
        min_x = min([key[0] for key in self.grid_dict])
        max_x = max([key[0] for key in self.grid_dict])
        min_y = min([key[1] for key in self.grid_dict])        
        max_y = max([key[1] for key in self.grid_dict])
        print('\n'.join([''.join([dict_at_t[(i, j)] for i in range(min_x, max_x + 1)]) for j in range(min_y, max_y + 1)]))

    def tryTime(self, t):
        self.node_distances = {}
        self.obstacles = self.bytes[:t]
        self.grid_dict = {(i, j): '#' if (i, j) in self.obstacles else '.' for i in range(self.size) for j in range(self.size)}
        result = self.navigateMap(start=t)
        if result is not None:
            return True
        else:
            return False
        
    def findFatalByte(self, start=1024):
        t = start
        delta = 512
        stillNavigable = True
        while stillNavigable:
            t += delta
            stillNavigable = self.tryTime(t)
            if not stillNavigable:
                if delta == 1:
                    return ','.join([str(x) for x in self.bytes[t-1]])
                else:
                    t -= delta
                    delta = int(delta / 2)
                    stillNavigable = True

def part_1(memoryMap):
    print('Part 1:', memoryMap.navigateMap())

def part_2(memoryMap):
    print('Part 2:', memoryMap.findFatalByte())

def main():
    bytes = [eval(x) for x in open(file, 'r').read().splitlines()]
    memoryMap = MemoryMap(bytes)
    part_1(memoryMap)
    part_2(memoryMap)

if __name__ == '__main__':
    main()