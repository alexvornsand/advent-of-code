# advent of code 2017
# day 20

file = 'solutions/2017/day-02/input.txt'

class Spreadsheet:
    def __init__(self, rows):
        self.rows = rows

    def checksum(self):
        return sum([max(row) - min(row) for row in self.rows])
    
    def checkdiv(self):
        return sum([int(i / j) for row in self.rows  for i in row for j in row if i % j == 0 and i != j])

def part_1(spreadsheet):
    print('Part 1:', spreadsheet.checksum())

def part_2(spreadsheet):
    print('Part 2:', spreadsheet.checkdiv())

def main():
    rows = [[int(x.strip()) for x in row.split('\t')] for row in open(file, 'r').read().splitlines()]
    spreadsheet = Spreadsheet(rows)
    part_1(spreadsheet)
    part_2(spreadsheet)

if __name__ == '__main__':
    main()