# advent of code 2024
# day 06

file = 'input.txt'

class GuardMap:
    def __init__(self, map):
        self.map_dict = {(i, j): map[j][i] for j in range(len(map)) for i in range(len(map[j]))}
        self.guard = list(self.map_dict.keys())[list(self.map_dict.values()).index('^')]

    def takeStep(self, md, g):
        dirs = ['^', '>', 'v', '<']
        paths = ['|', '-']
        steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        try_step = steps[dirs.index(md[g])]
        new_loc = (g[0] + try_step[0], g[1] + try_step[1])
        if new_loc in md:
            if md[new_loc] != '#':
                md[new_loc] = md[g]
                md[g] = paths[dirs.index(md[g]) % 2]
                g = new_loc
            else:
                md[g] = dirs[(dirs.index(md[g]) + 1) % 4]
        else:
            md[g] = paths[dirs.index(md[g]) % 2]
            g = (-1, -1)
        return md, g
    
    def printMap(md):
        minX = min([key[0] for key in md.keys()])
        maxX = max([key[0] for key in md.keys()])
        minY = min([key[1] for key in md.keys()])
        maxY = max([key[1] for key in md.keys()])
        print('\n'.join([''.join([md[(i, j)] for i in range(minX, maxX + 1)]) for j in range(minY, maxY + 1)]))

    def navigateMap(self, md, g, prints=False):
        history = [(g[0], g[1], md[g])]
        counter = 0
        while True:
            if prints:
                print(counter)
                self.printMap(md)
            md, g = self.takeStep(md, g)
            if g == (-1, -1):
                return [key for key in md if md[key] in ('|', '-')]
            map_state = (g[0], g[1], md[g])
            if map_state in history:
                return [(-1, -1)]
            else:
                history.append(map_state)
                counter += 1

    def testCandidate(self, md, g, candidate, prints=False):
        test_map = md.copy()
        test_map[candidate] = '#'
        return self.navigateMap(test_map, g, prints) == [(-1, -1)]

    def findRouteLength(self):
        return len(self.navigateMap(self.map_dict.copy(), self.guard))
    
    def findAllCycles(self):
        candidates = self.navigateMap(self.map_dict.copy(), self.guard)
        candidates.remove(self.guard)
        return sum([self.testCandidate(self.map_dict.copy(), self.guard, candidate) for candidate in candidates])

def part_1(guardMap):
    print('Part 1:', guardMap.findRouteLength())

def part_2(guardMap):
    print('Part 2:', guardMap.findAllCycles())

def main():
    map = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    guardMap = GuardMap(map)
    part_1(guardMap)
    part_2(guardMap)

if __name__ == '__main__':
    main()