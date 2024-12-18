# advent of code 2018
# day 4

import re
from datetime import datetime

file = 'input.txt'

class GuardLog:
    def __init__(self, log):
        self.log = log
        self.guards_minutes = {}
        self.guards_total = {}
        
    def strategy_1(self):
        for line in self.log:
            date_time, event = re.search('\[(.*)\]\s(.*)', line).groups()
            if '#' in event:
                guard = int(re.search('\#(\d*)', event).groups()[0])
                if guard not in self.guards_minutes:
                    self.guards_minutes[guard] = {}
                    self.guards_total[guard] = 0
                    for i in range(60):
                        self.guards_minutes[guard][i] = 0
            elif event == 'falls asleep':
                falls_asleep = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
            else:
                wakes_up = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
                minutes_asleep = wakes_up - falls_asleep
                self.guards_total[guard] += int(minutes_asleep.total_seconds() / 60)
                for minute in range(int(minutes_asleep.total_seconds() / 60)):
                    self.guards_minutes[guard][(falls_asleep.minute + minute) % 60] += 1

        sleepiest_guard = max(self.guards_total, key=self.guards_total.get)
        sleepiest_minute =  max(self.guards_minutes[sleepiest_guard], key=self.guards_minutes[sleepiest_guard].get)
        return(sleepiest_guard * sleepiest_minute)
    
    def strategy_2(self):
        max = 0
        max_guard = 0
        max_min = 0
        for guard in self.guards_minutes:
            for minute in range(60):
                if self.guards_minutes[guard][minute] > max:
                    max = self.guards_minutes[guard][minute]
                    max_guard = guard
                    max_min = minute
        return(max_guard * max_min)
    
def part_1(guardLog):
    print('Part 1:', guardLog.strategy_1())

def part_2(guardLog):
    print('Part 2:', guardLog.strategy_2())

def main():
    log = open(file, 'r').read().splitlines()
    log.sort()
    guardLog = GuardLog(log)
    part_1(guardLog)
    part_2(guardLog)

if __name__ == '__main__':
    main()
