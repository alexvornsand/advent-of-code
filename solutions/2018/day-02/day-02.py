# advent of code 2018
# day 02

file = 'solutions/2018/day-02/input.txt'

class Warehouse:
    def __init__(self, boxes):
        self.boxes = boxes
        self.twos = set()
        self.threes = set()
        for box in boxes:
            for char in list(set(box)):
                count = box.count(char)
                if count == 2:
                    self.twos.add(''.join(box))
                elif count == 3:
                    self.threes.add(''.join(box))

    def checksum(self):
        return len(self.twos) * len(self.threes)
    
    def findSisters(self):
        for box_a in self.boxes:
            for box_b in self.boxes:
                commonalities = [a for a, b in zip(box_a, box_b) if a == b]
                if len(commonalities) == len(box_a) - 1:
                    return ''.join(commonalities)

def part_1(warehouse):
    print('Part 1:', warehouse.checksum())

def part_2(warehouse):
    print('Part 2:', warehouse.findSisters())

def main():
    boxes = [[x for x in box] for box in open(file, 'r').read().splitlines()]
    warehouse = Warehouse(boxes)
    part_1(warehouse)
    part_2(warehouse)

if __name__ == '__main__':
    main()