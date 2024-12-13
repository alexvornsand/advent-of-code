# advent of code 2024
# day 11

from functools import cache

file = 'input.txt'

class Stones:
    def __init__(self, stones):
        self.stones = tuple(stones)
        self.memo = dict()

    def processStone(self, stone):
        if stone in self.memo:
            return self.memo[stone]
        if stone == 0:
            self.memo[stone] = tuple([1])
        elif len(str(stone)) % 2 == 0:
            self.memo[stone] = tuple([int(str(stone)[:int(len(str(stone)) / 2)]), int(str(stone)[int(len(str(stone)) / 2):])])
        else:
            self.memo[stone] = tuple([stone * 2024])
        return self.memo[stone]

    @cache    
    def blinkRepeat(self, stones, n):
        if n == 0:
            return len(stones)
        return sum([self.blinkRepeat(self.processStone(stone), n - 1) for stone in stones])

def part_1(stones):
    print('Part 1:', stones.blinkRepeat(stones.stones, 25))

def part_2(stones):
    print('Part 2:', stones.blinkRepeat(stones.stones, 75))

def main():
    stones = Stones([int(x) for x in open(file, 'r').read().split()])
    part_1(stones)
    part_2(stones)

if __name__ == '__main__':
    main()