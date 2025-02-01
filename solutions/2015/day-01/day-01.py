# advent of code 2015
# day 1

import itertools

file = 'solutions/2015/day-01/input.txt'

class Directions:
    def __init__(self, input):
        self.directions = [{'(': 1, ')': -1}[i] for i in open(input, 'r').read().rstrip()]
        self.position = list(itertools.accumulate(self.directions))
    
def part_1(directions):
    endPosition = directions.position[-1]
    print('Part 1:', endPosition, sep='\n')

def part_2(directions):
    firstBasement = min(
        [i for i in range(len(directions.position)) if directions.position[i] < 0 ]
    ) + 1
    print('Part 2:', firstBasement, sep='\n')

def main():
    directions = Directions(file)
    part_1(directions)
    part_2(directions)

if __name__ == '__main__':
    main()