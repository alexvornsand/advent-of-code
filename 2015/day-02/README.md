### [--- Day 2: I Was Told There Would Be No Math ---](https://adventofcode.com/2015/day/2)

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length `l`, width `w`, and height `h`) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect [right rectangular prism](https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid)), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is `2*l*w + 2*w*h + 2*h*l`. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

- A present with dimensions `2x3x4` requires `2*6 + 2*12 + 2*8 = 52` square feet of wrapping paper plus `6` square feet of slack, for a total of `58` square feet.
- A present with dimensions `1x1x10` requires `2*1 + 2*10 + 2*10 = 42` square feet of wrapping paper plus `1` square foot of slack, for a total of `43` square feet.

All numbers in the elves' list are in feet. How many total **square feet of wrapping paper** should they order?

### --- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

- A present with dimensions `2x3x4` requires `2+2+3+3 = 10` feet of ribbon to wrap the present plus `2*3*4 = 24` feet of ribbon for the bow, for a total of `34` feet.
- A present with dimensions `1x1x10` requires `1+1+1+1 = 4` feet of ribbon to wrap the present plus `1*1*10 = 10` feet of ribbon for the bow, for a total of `14` feet.

How many total **feet of ribbon** should they order?

# [--- Solution ---](day-02.py)
```Python
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
```