# advent of code 2018
# day 25

import re

file = 'solutions/2018/day-25/input.txt'

class Constellations:
    def __init__(self, points):
        self.points = points
        self.constellations = {}

    def mapPoint(self, point):
        w, x, y, z = point
        if len(self.constellations) == 0:
            self.constellations[1] = [point]
        else:
            nearby_constellations = []
            for constellation in self.constellations:
                if any(sum([abs(w - cw), abs(x - cx), abs(y - cy), abs(z - cz)]) <= 3 for cw, cx, cy, cz in self.constellations[constellation]):
                    nearby_constellations.append(constellation)
            if len(nearby_constellations) == 0:
                self.constellations[max(list(self.constellations)) + 1] = [point]
            elif len(nearby_constellations) == 1:
                self.constellations[nearby_constellations[0]].append(point)
            else:
                self.constellations[nearby_constellations[0]].append(point)
                for i in nearby_constellations[1:]:
                    self.constellations[nearby_constellations[0]] += self.constellations[i]
                    del self.constellations[i]
    
    def countConstellations(self):
        for point in self.points:
            self.mapPoint(point)
        return len(self.constellations)
    
def part_1(constellations):
    print('Part 1:', constellations.countConstellations())


def main():
    points = [[int(x) for x in re.findall(r"-?\d+", line)] for line in open(file, 'r').read().splitlines()]
    constellations = Constellations(points)
    part_1(constellations)

if __name__ == '__main__':
    main()
