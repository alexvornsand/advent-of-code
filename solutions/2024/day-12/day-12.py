# advent of code 2024
# day 12

file = 'input.txt'

class GardenMap:
    def __init__(self, map):
        self.map = map
        self.unvisited_tiles = []
        self.map_dict = {}
        for j in range(len(self.map)):
            for i in range(len(self.map[j])):
                self.unvisited_tiles.append((i, j))
                self.map_dict[(i, j)] = self.map[j][i]      
        self.regions = {} 

    def explorePlot(self, seed):
        seed_value = self.map_dict[seed]
        self.regions[seed] = {'points': [seed], 'perimeter': 0}
        queue = [seed]
        while len(queue) > 0:
            cx, cy = queue.pop(0)
            self.unvisited_tiles.remove((cx, cy))
            self.regions[seed]['perimeter'] += 4
            for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (cx + nx, cy + ny) in self.map_dict:
                    if self.map_dict[(cx + nx, cy + ny)] == seed_value:
                        self.regions[seed]['perimeter'] -= 1
                        if (cx + nx, cy + ny) in self.unvisited_tiles:
                            if (cx + nx, cy + ny) not in queue:
                                queue.append((cx + nx, cy + ny)) 
                                self.regions[seed]['points'].append((cx + nx, cy + ny))

    def exploreMap(self):
        while len(self.unvisited_tiles) > 0:
            self.explorePlot(self.unvisited_tiles[0])

    def countEdges(self, plot):
        self.regions[plot]['edges'] = 0
        minX = min([point[0] for point in self.regions[plot]['points']])
        maxX = max([point[0] for point in self.regions[plot]['points']])
        minY = min([point[1] for point in self.regions[plot]['points']])
        maxY = max([point[1] for point in self.regions[plot]['points']])
        for cx in range(minX - 1, maxX + 1):
            for cy in range(minY - 1, maxY + 1):
                neighbors_in_region = 0
                for nx, ny in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                    if (cx + nx, cy + ny) in self.regions[plot]['points']:
                        neighbors_in_region += 1
                if neighbors_in_region in [1, 3]:
                    self.regions[plot]['edges'] += 1
                elif neighbors_in_region == 2:
                    if ((cx + 0, cy + 0) in self.regions[plot]['points']) == ((cx + 1, cy + 1) in self.regions[plot]['points']):
                        self.regions[plot]['edges'] += 2
        return self.regions[plot]['edges']

    def calcPerimeterCost(self):
            return sum([len(self.regions[plot]['points']) * self.regions[plot]['perimeter'] for plot in self.regions])

    def calcSideCost(self):
            return sum([len(self.regions[plot]['points']) * self.countEdges(plot) for plot in self.regions])

def part_1(gardenMap):
    print('Part 1:', gardenMap.calcPerimeterCost())

def part_2(gardenMap):
    print('Part 2:', gardenMap.calcSideCost())

def main():
    map = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    gardenMap = GardenMap(map)
    gardenMap.exploreMap()
    part_1(gardenMap)
    part_2(gardenMap)

if __name__ == '__main__':
    main()