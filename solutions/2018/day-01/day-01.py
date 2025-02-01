# advent of code 2018
# day 01

file = 'solutions/2018/day-01/input.txt'

class Calibrator:
    def __init__(self, frequencies):
        self.frequencies = [int(x.strip()) for x in frequencies.splitlines()]
        self.frequency_sum =sum(self.frequencies)

    def totalFrequencies(self):
        return self.frequency_sum
    
    def findDuplicateFrequencies(self):
        totals = [sum(self.frequencies[:i]) for i in range(len(self.frequencies))]
        i = 1
        while True:
            for total in totals:
                if total + self.frequency_sum * i in totals:
                    return total + self.frequency_sum * i
            i += 1

def part_1(calibrator):
    print('Part 1:', calibrator.totalFrequencies())

def part_2(calibrator):
    print('Part 2:', calibrator.findDuplicateFrequencies())

def main():
    frequencies = open(file, 'r').read()
    calibrator = Calibrator(frequencies)
    part_1(calibrator)
    part_2(calibrator)

if __name__ == '__main__':
    main()