# advent of code 2018
# day 06

file = 'input.txt'

class CoordinateMap:
    def __init__(self, points):
        self.points = points
        self.map_dict = {coord: chr(65 + id) for id, coord in enumerate(self.points)}
        self.point_counts = {chr(65 + id): [coord] for id, coord in enumerate(self.points)}

    def printMap(self):
        x_min = min([coord[0] for coord in self.map_dict])
        x_max = max([coord[0] for coord in self.map_dict]) + 1
        y_min = min([coord[1] for coord in self.map_dict])
        y_max = max([coord[1] for coord in self.map_dict]) + 1
        print('\n'.join([''.join([str(self.map_dict[(x, y)]) if (x, y) in self.map_dict else ' ' for x in range(x_min, x_max)]) for y in range(y_min, y_max)]))

    def floodFillMap(self, log=False):
        queue = [self.points.copy()]
        iterations = max([max([abs(xa - xb) + abs(ya - yb) for xb, yb in self.points if (xa, ya) != (xb, yb)]) for xa, ya in self.points])
        for _ in range((iterations // 2) + 1):
            if log:
                self.printMap()
                print('')
            current_layer = queue.pop(0)
            next_layer = set()
            new_points = {}
            for x, y in current_layer:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (x + dx, y +dy) not in self.map_dict:
                        if (x + dx, y + dy) in new_points and new_points[(x + dx, y + dy)] != self.map_dict[(x, y)]:
                            new_points[(x + dx, y + dy)] = '.'
                        else:
                            new_points[(x + dx, y + dy)] = self.map_dict[(x, y)]
                            next_layer.add((x + dx, y + dy))
            for point in new_points:
                if new_points[point] in self.point_counts:
                    self.point_counts[new_points[point]].append(point)
            queue.append(list(next_layer))
            self.map_dict.update(new_points)
        return max([len(points) for keys, points in self.point_counts.items() if keys not in new_points.values()])
    
    def countCentralPoints(self, n=10000):
        x_min = max([coord[0] for coord in self.points]) - n
        x_max = min([coord[0] for coord in self.points]) + n
        y_min = max([coord[1] for coord in self.points]) - n
        y_max = min([coord[1] for coord in self.points]) + n
        return sum([sum([abs(x - i) + abs(y - j) for i, j in self.points]) < n for x in range(x_min, x_max) for y in range(y_min, y_max)])
    
def part_1(coordinateMap):
    print('Part 1:', coordinateMap.floodFillMap())

def part_2(coordinateMap):
    print('Part 2:', coordinateMap.countCentralPoints())

def main():
    points = [eval(x) for x in open(file, 'r').read().splitlines()]
    coordinateMap = CoordinateMap(points)
    part_1(coordinateMap)
    part_2(coordinateMap)

if __name__ == '__main__':
    main()
