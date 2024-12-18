# advent of code 2024
# day 10

file = 'input.txt'

class TrailMap:
    def __init__(self, map):
        self.map = map
        self.map_dict = {(x, y): map[y][x] for y in range(len(self.map)) for x in range(len(self.map[y]))}

    def findTrails(self, seq):
        current_x, current_y = seq[-1]
        current_height = self.map_dict[(current_x, current_y)]
        if current_height == 9:
            return [seq]
        else:
            neighbors = [(current_x + x, current_y + y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)] 
                        if current_x + x >= 0 and current_x + x < len(self.map[0]) and current_y + y >= 0 and current_y + y < len(self.map)]
            next_trails = []
            for neighbor in neighbors:
                if self.map_dict[neighbor] == current_height + 1:
                    final_trails_from_here = self.findTrails(seq + [neighbor])
                    for trail in final_trails_from_here:
                        next_trails.append(trail)
            return next_trails
    
    def findAllTrails(self):
        self.trails = [self.findTrails([head]) for head in [key for key in self.map_dict if self.map_dict[key] == 0]]

    def countDestinations(self):
        return len(set([trail[-1] for trails_from_head in self.trails for trail in trails_from_head]))

    def countTrails(self):
        return len([trail for trails_from_head in self.trails for trail in trails_from_head])
    
def part_1(trailMap):
    print('Part 1:', trailMap.countDestinations())

def part_2(trailMap):
    print('Part 2:', trailMap.countTrails())

def main():
    map = [[int(x) if x != '.' else -1 for x in line] for line in open(file, 'r').read().splitlines()]
    trailMap = TrailMap(map)
    trailMap.findAllTrails()
    part_1(trailMap)
    part_2(trailMap)

if __name__ == '__main__':
    main()