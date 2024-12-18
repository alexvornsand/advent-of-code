# advent of code 2024
# day 14

import re
import math
import numpy as np

file = 'input.txt'

class BotBallet:
    def __init__(self, bots):
        self.bots = bots

    def moveBot(self, bot, n):
        x, y, dx, dy = bot
        new_x = (x + (dx * n)) % 101
        new_y = (y + (dy * n)) % 103
        return(new_x, new_y)
    
    def identifyQuadrant(self, pos):
        x, y = pos
        if x < 50:
            if y < 51:
                return 1
            elif y > 51:
                return 3
            else:
                return 0
        elif x > 50:
            if y < 51:
                return 2
            elif y > 51:
                return 4
            else:
                return 0
        else:
            return 0
        
    def summarizeBotState(self, n=100):
        quadrants = [self.identifyQuadrant(self.moveBot(bot, n)) for bot in self.bots]
        return math.prod([quadrants.count(x) for x in range(1, 5)])
        
    def printImage(self, bot_state):
        min_x = min([bot[0] for bot in bot_state])
        max_x = max([bot[0] for bot in bot_state])
        min_y = min([bot[1] for bot in bot_state])
        max_y = max([bot[1] for bot in bot_state])
        print('\n'.join([''.join(['#' if (x, y) in bot_state else '.' for x in range(min_x, max_x + 1)]) for y in range(min_y, max_y + 1)]))

    def findEasterEgg(self):
        stds = [np.std([self.moveBot(bot, i) for bot in self.bots]) for i in range(1, 10001)]
        return stds.index(min(stds)) + 1
    
def part_1(botBallet):
    print('Part 1:', botBallet.summarizeBotState())

def part_2(botBallet):
    print('Part 2:', botBallet.findEasterEgg())

def main():
    bots = [[int(x) for x in re.findall(r'\-?\d+', line)] for line in open(file, 'r').read().splitlines()]
    botBallet = BotBallet(bots)
    part_1(botBallet)
    part_2(botBallet)

if __name__ == '__main__':
    main()