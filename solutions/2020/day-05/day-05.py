# advent of code 2020
# day 05

file = 'solutions/2020/day-05/input.txt'

class Manifest:
    def __init__(self, tickets):
        self.tickets = tickets
        self.seat_ids = []

    def seatID(self, ticket):
        row = int(ticket[:-3].replace('B', '1').replace('F', '0'), 2)
        seat = int(ticket[-3:].replace('R', '1').replace('L', '0'), 2)
        seat_id = row * 8 + seat
        self.seat_ids.append(seat_id)
        return seat_id
    
    def identifySeats(self):
        for ticket in self.tickets:
            self.seatID(ticket)
        self.first_seat = min(self.seat_ids)
        self.last_seat = max(self.seat_ids)
    
    def findMissingSeat(self):
        for id in range(self.first_seat, self.last_seat + 1):
            if id not in self.seat_ids and id + 1 in self.seat_ids and id - 1 in self.seat_ids:
                return id

def part_1(manifest):
    print('Part 1:', manifest.last_seat)

def part_2(manifest):
    print('Part 2:', manifest.findMissingSeat())

def main():
    tickets = open(file, 'r').read().splitlines()
    manifest = Manifest(tickets)
    manifest.identifySeats()
    part_1(manifest)
    part_2(manifest)

if __name__ == '__main__':
    main()
