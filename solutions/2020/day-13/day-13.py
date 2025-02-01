# advent of code 2020
# day 13

import math

file = 'solutions/2020/day-13/input.txt'

class BusStop:
    def __init__(self, time, shuttles):
        self.time = int(time)
        self.shuttles = [int(shuttle) if shuttle.isdigit() else shuttle for shuttle in shuttles.split(',')]

    def findNextBus(self):
        return math.prod(min([(shuttle, shuttle - (self.time % shuttle)) for shuttle in self.shuttles if isinstance(shuttle, int)], key=lambda x: x[1]))

    def findFirstSynchronizedTime(self):
        N = math.lcm(*[shuttle for shuttle in self.shuttles if isinstance(shuttle, int)])
        Ms = [int(N / shuttle) if isinstance(shuttle, int) else None for shuttle in self.shuttles]
        ys = [pow(M, -1, shuttle) if isinstance(shuttle, int) else None for M, shuttle in zip(Ms, self.shuttles)]
        return sum([(((shuttle - self.shuttles.index(shuttle)) % shuttle) * M * y) % N for shuttle, M, y in zip(self.shuttles, Ms, ys) if isinstance(shuttle, int)]) % N

def part_1(busStop):
    print('Part 1:', busStop.findNextBus())

def part_2(busStop):
    print('Part 2:', busStop.findFirstSynchronizedTime())

def main():
    time, shuttles = open(file, 'r').read().splitlines()
    busStop = BusStop(time, shuttles)
    part_1(busStop)
    part_2(busStop)

if __name__ == '__main__':
    main()