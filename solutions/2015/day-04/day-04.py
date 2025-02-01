# advent of code 2015
# day 4

from hashlib import md5 as md5

file = 'solutions/2015/day-04/input.txt'

class Key:
    def __init__(self, key):
        self.key = key
        self.index = 0

    def leading_five(self):
        while(True):
            test_key = self.key + str(self.index)
            if md5(test_key.encode()).hexdigest()[0:5] == '00000':
                return(self.index)
            else:
                self.index += 1

    def leading_six(self):
        while(True):
            test_key = self.key + str(self.index)
            if md5(test_key.encode()).hexdigest()[0:6] == '000000':
                return(self.index)
            else:
                self.index += 1

def part_1(key):
    print('Part 1:', key.leading_five(), sep = '\n')

def part_2(key):
    print('Part 2:', key.leading_six(), sep = '\n')
            
def main():
    key = Key(open(file, 'r').read().rstrip())
    part_1(key)
    part_2(key)

if __name__ == '__main__':
    main()