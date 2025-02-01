# advent of code 2018
# day 11

import numpy as np

file = 'solutions/2018/day-11/input.txt'

class PowerGrid:
    def __init__(self, serial_number, size = 300):
        self.serial_number = serial_number
        self.matrix = np.array([[(((((x + 11) * (y + 1)) + self.serial_number) * (x + 11) % 1000) // 100) - 5 for x in range(size)] for y in range(size)])
        self.local_power = np.array([[[int(self.matrix[x:x + n, y:y + n].sum()) if x <= size - n and y <= size - n else -5 * (n ** 2) for y in range(size)] for x in range(size)] for n in range(1, size + 1)])

    def findLocalMaximum(self, n=None):
        if n is not None:
            return ','.join([str(list(x)[0] + 1) for x in np.where(self.local_power[n-1, :, :] == self.local_power[n-1, :, :].max())[1::-1]])
        else:
            return ','.join([str(list(x)[0] + 1) for x in np.where(self.local_power == self.local_power.max())[::-1]])
        
def part_1(powerGrid):
    print('Part 1:', powerGrid.findLocalMaximum(3))

def part_2(powerGrid):
    print('Part 2:', powerGrid.findLocalMaximum())

def main():
    serial_number = int(open(file, 'r').read())
    powerGrid = PowerGrid(serial_number)
    part_1(powerGrid)
    part_2(powerGrid)

if __name__ == '__main__':
    main()