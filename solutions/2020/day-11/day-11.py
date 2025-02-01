# advent of code 2020
# day 11

from collections import defaultdict

file = 'solutions/2020/day-11/input.txt'

class ConwayFerry:
    def __init__(self, seat_grid):
        self.seat_grid = {(x, y): seat_grid[y][x] for y in range(len(seat_grid)) for x in range(len(seat_grid[y]))}
        self.current_seat_grid = defaultdict(lambda: '.')
        for key, val in self.seat_grid.items():
            self.current_seat_grid[key] = val
        self.w = len(seat_grid[0])
        self.l = len(seat_grid)
        self.max_dim = max(len(seat_grid), len(seat_grid[0]))

    def seatSummary(self):
        return '\n'.join([''.join([self.current_seat_grid[(x, y)] for x in range(self.w)]) for y in range(self.l)])

    def nextSeatState(self, seat, tolerance=4, view='near'):
        current_state = self.current_seat_grid[seat]
        if current_state == '.':
            return '.'
        x, y = seat
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        if view == 'near':
            neighbors = [self.current_seat_grid[(x + dx, y + dy)] for dx, dy in directions]
        else:
            neighbors = [(''.join([self.current_seat_grid[(x + (dx * n), y + (dy * n))] for n in range(1, self.max_dim)]) + 'L') .strip('.')[0] for dx, dy in directions]
        occupied_neighbors = neighbors.count('#')
        if current_state == 'L' and occupied_neighbors == 0:
            return '#'
        elif current_state == '#' and occupied_neighbors >= tolerance:
            return 'L'
        else:
            return current_state

    def nextSeatPattern(self, tolerance=4, view='near'):
        return {(x, y): self.nextSeatState((x, y), tolerance, view) for x in range(self.w) for y in range(self.l)}
    
    def findStableArrangement(self, tolerance=4, view='near'):
        self.current_seat_grid = defaultdict(lambda: '.')
        for key, val in self.seat_grid.items():
            self.current_seat_grid[key] = val
        prev_state = None
        current_state = self.seatSummary()
        while current_state != prev_state:
            prev_state = current_state
            next_grid = self.nextSeatPattern(tolerance, view)
            self.current_seat_grid = defaultdict(lambda: '.')            
            for key, val in next_grid.items():
                self.current_seat_grid[key] = val
            current_state = self.seatSummary()
        return current_state.count('#')             

def part_1(conwayFerry):
    print('Part 1:', conwayFerry.findStableArrangement())

def part_2(conwayFerry):
    print('Part 2:', conwayFerry.findStableArrangement(tolerance=5, view='distant'))

def main():
    seat_grid = [[x for x in line] for line in open(file, 'r').read().splitlines()]
    conwayFerry = ConwayFerry(seat_grid)
    part_1(conwayFerry)
    part_2(conwayFerry)

if __name__ == '__main__':
    main()