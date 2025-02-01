# advent of code 2020
# day 09

from collections import deque

file = 'solutions/2020/day-09/input.txt'

class XMASEncryptedData:
    def __init__(self, data):
        self.data = data

    def findFailurePoint(self, n=25):
        for i in range(n, len(self.data) + 1):
            if not any([self.data[j] + self.data[k] == self.data[i] for j in range(i - n, i - 1) for k in range(j, i)]):
                self.failure_point = self.data[i]
                return self.failure_point
            
    def findWeakness(self):
        window = deque([])
        window_sum = 0
        i = 0
        while True:
            if window_sum < self.failure_point:
                window.append(self.data[i])
                window_sum += self.data[i]
                i += 1
            elif window_sum > self.failure_point:
                window_sum -= window.popleft()
            else:
                return min(window) + max(window)
            
def part_1(xmasEncryptedData):
    print('Part 1:', xmasEncryptedData.findFailurePoint())

def part_2(xmasEncryptedData):
    print('Part 2:', xmasEncryptedData.findWeakness())

def main():
    data = [int(x) for x in open(file, 'r').read().splitlines()]
    xmasEncryptedData = XMASEncryptedData(data)
    part_1(xmasEncryptedData)
    part_2(xmasEncryptedData)

if __name__ == '__main__':
    main()