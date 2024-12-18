# advent of code 2017
# day 3

file = 'input.txt'

class Spiral:
    def __init__(self, terminus):
        self.terminus = terminus
        self.spiral = {}

    def neighbors(self, coord):
        x, y = coord
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x + 1, y + 1)]
        return [neighbor for neighbor in neighbors if neighbor in self.spiral]
    
    def populateStep(self, coord):
        neighbors = self.neighbors(coord)
        self.spiral[coord] = sum([self.spiral[neighbor] for neighbor in neighbors])

    def findNextStep(self, coord):
        x, y = coord
        if y >= 0 and x <= y and abs(x) <= y:
            x += 1
        elif y < 0 and x > y and x <= abs(y):
            x -= 1
        elif x >= 0 and x > y:
            y -= 1
        elif x < 0 and x <= y:
            y += 1
        return (x, y)
    
    def printSpiral(self):
        x_max = max([key[0] for key in self.spiral.keys()])
        x_min = min([key[0] for key in self.spiral.keys()])
        y_max = max([key[1] for key in self.spiral.keys()])
        y_min = min([key[1] for key in self.spiral.keys()])
        image = ''
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if (x, y) in self.spiral:
                    image += str(self.spiral[(x, y)]).rjust(8, ' ')
                else:
                    image += ' ' * 8
            image += '\n\n'
        print(image)
    
    def fillSpiral(self):
        coord = (0, 0)
        self.spiral[coord] = 1
        while max(self.spiral.values()) < self.terminus:
            coord = self.findNextStep(coord)
            self.populateStep(coord)
        return self.spiral[coord]
    
class DataPoint:
    def __init__(self, point):
        self.point = point

    def calculateDistance(self):
        self.ring = int(-(-(self.point)**(1/2)//1)//2)
        self.carryover = self.point - (self.ring * 2 - 1)**2
        self.segments = self.carryover // (2 * self.ring) if self.ring != 0 else 0
        self.shift = abs(self.carryover - self.ring * (2 * self.segments + 1))
        self.manhattan_distance = self.shift + self.ring
        return self.manhattan_distance

def part_1(dataPoint):
    print('Part 1:', dataPoint.calculateDistance())

def part_2(spiral):
    print('Part 2:', spiral.fillSpiral())

def main():
    dataPoint = DataPoint(265149)
    spiral = Spiral(265149)
    part_1(dataPoint)
    part_2(spiral)

if __name__ == '__main__':
    main()
