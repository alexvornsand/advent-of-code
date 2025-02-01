# advent of code 2018
# day 09

import re
from collections import deque

file = 'solutions/2018/day-09/input.txt'

class MarbleGame:
    def __init__(self, players, marbles):
        self.players = players
        self.marbles = marbles + 1
        self.circle = deque([0])
        self.scores = {i: 0 for i in range(self.players)}

    def playGame(self):
        for marble in range(1, self.marbles + 1):
            if marble % 23 == 0:
                self.circle.rotate(7)
                self.scores[marble % self.players] += marble + self.circle.pop()
                self.circle.rotate(-1)
            else:
                self.circle.rotate(-1)
                self.circle.append(marble)
        return max(self.scores.values()) if self.scores else 0           

def part_1(marbleGame):
    print('Part 1:', marbleGame.playGame())

def part_2(biggerMarbleGame):
    print('Part 2:', biggerMarbleGame.playGame())

def main():
    players, marbles = [int(x) for x in re.findall(r"\d+", open(file, 'r').read())]
    marbleGame = MarbleGame(players, marbles)
    biggerMarbleGame = MarbleGame(players, marbles * 100)
    part_1(marbleGame)
    part_2(biggerMarbleGame)

if __name__ == '__main__':
    main()