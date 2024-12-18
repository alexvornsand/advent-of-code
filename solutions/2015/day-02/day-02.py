# advent of code 2015
# day 2

file = 'input.txt'

class Present:
    def __init__(self, input):
        self.width, self.length, self.height = (int(x) for x in input.split('x'))
        self.bottom = self.width*self.length
        self.front = self.width*self.height
        self.side = self.length*self.height
        self.smallest_surface = min(self.bottom, self.front, self.side)
        self.surface_area = 2*self.bottom + 2*self.front + 2*self.side
        self.paper_required = self.surface_area + self.smallest_surface
        self.ribbon_circ = 2*sum(sorted([self.width, self.length, self.height])[:2])
        self.ribbon_bow = self.width*self.length*self.height
        self.ribbon_required = self.ribbon_circ + self.ribbon_bow

def part_1(file):
    print('Part 1:', sum([Present(x).paper_required for x in open(file, 'r').read().rstrip().split('\n')]), sep='\n')

def part_2(file):
    print('Part 2:', sum([Present(x).ribbon_required for x in open(file, 'r').read().rstrip().split('\n')]), sep='\n')

def main():
    part_1(file)
    part_2(file)

if __name__ == '__main__':
    main()