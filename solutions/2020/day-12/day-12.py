# advent of code 2020
# day 12

file = 'solutions/2020/day-12/input.txt'

class Directions:
    def __init__(self, steps):
        self.steps = steps
    
    def followInstructions(self):
        x = y = r = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for movement, quantity in self.steps:
            if movement in ['L', 'R']:
                r = (r + int((quantity / 90) * [-1, 1][['L', 'R'].index(movement)])) % 4
            else:
              if movement in ['N', 'S', 'E', 'W']:
                  dx, dy = directions[['E', 'S', 'W', 'N'].index(movement)]
              else:
                  dx, dy = directions[r]
              x += dx * quantity
              y += dy * quantity
        return x + y

    def followWaypointInstructions(self):
        x = y = 0
        (i, j) = (10, -1)
        for movement, quantity in self.steps:
            if movement == 'F':
                x += i * quantity
                y += j * quantity
            else:
              if movement in ['N', 'S']:
                  j += [-1, 1][['N', 'S'].index(movement)] * quantity              
              elif movement in ['E', 'W']:
                  i += [1, -1][['E', 'W'].index(movement)] * quantity              
              else:
                  for _ in range(int(quantity / 90)):
                      (i, j) = [(-j, i), (j, -i)][['R', 'L'].index(movement)]
        return abs(x) + abs(y)

def part_1(directions):
    print('Part 1:', directions.followInstructions())

def part_2(directions):
    print('Part 2:', directions.followWaypointInstructions())

def main():
    steps = [[line[0], int(line[1:])] for line in open(file, 'r').read().splitlines()]
    directions = Directions(steps)
    part_1(directions)
    part_2(directions)

if __name__ == '__main__':
    main()