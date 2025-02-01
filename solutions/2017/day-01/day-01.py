# advent of code 2017
# day 01

file = 'solutions/2017/day-01/input.txt'

class Captcha:
    def __init__(self, digits):
        self.digits = digits

    def findSumOfMatching(self, shift=1):
        return sum([self.digits[i] for i in range(len(self.digits)) if self.digits[i] == self.digits[(i + shift) % len(self.digits)]])
    
def part_1(captcha):
    print('Part 1:', captcha.findSumOfMatching())

def part_2(captcha):
    print('Part 2:', captcha.findSumOfMatching(int(len(captcha.digits) / 2)))

def main():
    digits = [int(x) for x in open(file, 'r').read().strip()]
    captcha = Captcha(digits)
    part_1(captcha)
    part_2(captcha)

if __name__ == '__main__':
    main()